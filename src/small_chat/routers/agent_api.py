from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import httpx
import os

from small_chat.db import get_gel
from small_chat.agents.summarizer import get_summarizer_agent
from small_chat.agents.extractor import get_extractor_agent, ExtractorContext
from small_chat.common.types import CommonChat
from models import default, std


router = APIRouter()


class SummarizeRequest(BaseModel):
    chat_id: str
    messages: list[str]
    cutoff: str
    summary_datetime: str


@router.post("/summarize")
async def summarize(
    request: SummarizeRequest,
    summarizer_agent=Depends(get_summarizer_agent),
    gel_client=Depends(get_gel),
):
    formatted_messages = "\n\n".join([m for m in request.messages])

    response = await summarizer_agent.run(
        f"""
        Summarize the following messages:
        {formatted_messages}
        Only respond with the summary, no other text.
        """
    )

    summary = response.output

    # Use the insert_summary function from the schema
    result = await gel_client.query(
        default.insert_summary(
            chat_id=request.chat_id,
            cutoff=request.cutoff,
            summary=summary,
            summary_datetime=request.summary_datetime,
        )
    )

    return {"summary": summary}


class ExtractRequest(BaseModel):
    chat_id: str


@router.post("/extract")
async def extract(
    request: ExtractRequest,
    gel_client=Depends(get_gel),
    extractor_agent=Depends(get_extractor_agent),
):
    q = default.Chat.select(
        '*',
        archive=lambda c: c.archive.select('*').order_by(created_at=True),
        history=lambda c: c.history.select('*').order_by(created_at=True)
    ).filter(lambda c: c.id == request.chat_id)
    
    result = await gel_client.get(q)
    chat = CommonChat.from_gel_result(result.__dict__)

    formatted_messages = "\n\n".join([f"{m.role}: {m.content}" for m in chat.history])

    response = await extractor_agent.run(
        f"""
        Conversation history:
        {formatted_messages}
        """,
        deps=ExtractorContext(
            gel_client=gel_client,
        ),
    )

    return {"response": response.output}


class GetTitleRequest(BaseModel):
    chat_id: str
    messages: list[str]


@router.post("/get_title")
async def get_title(
    request: GetTitleRequest,
    gel_client=Depends(get_gel),
    summarizer_agent=Depends(get_summarizer_agent),
):
    formatted_messages = "\n\n".join([m for m in request.messages])

    response = await summarizer_agent.run(
        f"""
        Generate a concise descriptive title (5 words or less) for the following conversation.
        {formatted_messages}
        Only respond with the title, no other text.
        """
    )

    title = response.output

    # Use ORM to update the chat
    chat = await gel_client.get(default.Chat.filter(lambda c: c.id == request.chat_id))
    chat.title = title
    await gel_client.save(chat)

    return {"title": title}
