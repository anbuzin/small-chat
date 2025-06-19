from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from pydantic_ai import Agent
from gel import AsyncIOClient
import gel.ai

import uuid
import json

from small_chat.agents.talker import get_talker_agent, TalkerContext
from small_chat.common.types import CommonChat, CommonMessage
from small_chat.db import get_gel
from models import default, std
from models.ext import ai


router = APIRouter()


class MessageRequest(BaseModel):
    chat_id: uuid.UUID
    message: CommonMessage


@router.get("/chat/{chat_id}")
async def get_chat(chat_id: uuid.UUID, gel_client=Depends(get_gel)) -> CommonChat:
    q = default.Chat.select(
        '*',
        archive=lambda c: c.archive.select('*').order_by(created_at=True),
        history=lambda c: c.history.select('*').order_by(created_at=True)
    ).filter(lambda c: c.id == chat_id)
    
    result = await gel_client.get(q)
    return CommonChat.from_gel_result(result.__dict__)


@router.get("/chats")
async def get_chats(gel_client=Depends(get_gel)) -> list[CommonChat]:
    q = default.Chat.select(
        '*',
        history=lambda c: c.history.select('*').order_by(created_at=True),
        archive=lambda c: c.archive.select('*').order_by(created_at=True)
    ).order_by(created_at='desc')
    
    results = await gel_client.query(q)
    return [CommonChat.from_gel_result(chat.__dict__) for chat in results]


@router.post("/chat")
async def create_chat(gel_client=Depends(get_gel)) -> uuid.UUID:
    chat = default.Chat()
    await gel_client.save(chat)
    return chat.id


@router.post("/message")
async def handle_message(
    request: MessageRequest,
    talker_agent: Agent = Depends(get_talker_agent),
    gel_client: AsyncIOClient = Depends(get_gel),
) -> StreamingResponse:
    chat = await get_chat(request.chat_id, gel_client)

    async def stream_response():
        yield "*Fetching facts...*\n"

        gel_ai_client = await gel.ai.create_async_rag_client(
            gel_client, model="gpt-4o-mini"
        )
        embedding_vector = await gel_ai_client.generate_embeddings(
            request.message.content,
            model="text-embedding-3-small",
        )

        user_facts_q = ai.search(default.Fact, embedding_vector).select(
            lambda result: result.object.body
        ).order_by(lambda result: result.distance).limit(5)
        
        user_facts = await gel_client.query(user_facts_q)

        behavior_prompt_q = default.Prompt.select(body=True)
        behavior_prompt = await gel_client.query(behavior_prompt_q)

        yield "*Gathering context...*\n"

        full_response = ""

        async with talker_agent.run_stream(
            request.message.content,
            message_history=chat.to_pydantic_ai_messages(),
            deps=TalkerContext(
                gel_client=gel_client,
                user_facts=[fact.body for fact in user_facts],
                behavior_prompt=[prompt.body for prompt in behavior_prompt],
            ),
        ) as result:
            async for text in result.stream_text(delta=True):
                full_response += text
                yield text

        new_messages = []
        for message in result.new_messages():
            for part in message.parts:
                common_message = CommonMessage.from_pydantic_ai_message_part(part)
                new_messages.append(common_message.model_dump())

        # Create Message objects using ORM
        chat_obj = await gel_client.get(default.Chat.filter(lambda c: c.id == request.chat_id))
        
        message_objects = []
        for msg_data in new_messages:
            message = default.Message(
                llm_role=msg_data['role'],
                body=msg_data.get('content'),
                tool_name=msg_data.get('tool_name'),
                tool_args=json.dumps(msg_data.get('tool_args')) if msg_data.get('tool_args') else None,
            )
            message_objects.append(message)
        
        await gel_client.save(*message_objects)
        
        # Update chat archive with new messages
        chat_obj.archive.extend(message_objects)
        await gel_client.save(chat_obj)

    return StreamingResponse(
        stream_response(),
        media_type="text/plain",
    )
