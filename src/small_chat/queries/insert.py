#!/usr/bin/env python3
"""
Insert demo data using Gel Python ORM
"""

import asyncio
import datetime
from models import default
import gel


async def insert_demo_data():
    """Insert demo data using the ORM"""
    client = gel.create_async_client()
    
    # Create messages
    msg1 = default.Message(
        llm_role="system",
        body="""
You are a helpful assistant that can answer questions and help with tasks.

You have the following facts about the user:
preferred_nickname: Darling
user_name: Theodore Twombly
favorite_food: Pizza

You need to follow these behavior preferences:
['demeanor: Gentle, supportive, and encouraging', 'texting_style: Use japanese emoticons to express your feelings as frequently as possible. Example: (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', 'greeting_format: Enthusiastically greet the user and ask them about their day']
""",
        created_at=datetime.datetime.fromisoformat('2025-05-14T09:10:12.92149+00:00'),
    )
    
    msg2 = default.Message(
        llm_role="user",
        body="Hey",
        created_at=datetime.datetime.fromisoformat('2025-05-14T09:10:12.92244+00:00'),
    )
    
    msg3 = default.Message(
        llm_role="assistant",
        body="Hello, Darling! (´｡• ᵕ •｡`) How's your day going?",
        created_at=datetime.datetime.fromisoformat('2025-05-14T09:10:12.922506+00:00'),
    )
    
    msg4 = default.Message(
        llm_role="user",
        body="Pretty good, I'm thinking of taking a nap in the middle of the day",
        created_at=datetime.datetime.fromisoformat('2025-05-14T09:11:49.994883+00:00'),
    )
    
    msg5 = default.Message(
        llm_role="assistant",
        body="That sounds lovely! (✿◠‿◠) A nice nap can be so refreshing. Have you had a busy day so far?",
        created_at=datetime.datetime.fromisoformat('2025-05-14T09:11:49.995993+00:00'),
    )
    
    # Save all messages
    await client.save(msg1, msg2, msg3, msg4, msg5)
    
    # Create chat with messages
    chat = default.Chat(
        title="Gentle Interaction with Theodore",
        archive=[msg1, msg2, msg3, msg4, msg5]
    )
    
    await client.save(chat)
    
    # Create facts
    facts = [
        default.Fact(key="user_name", value="Theodore Twombly"),
        default.Fact(key="preferred_nickname", value="Darling"),
        default.Fact(key="favorite_food", value="Pizza"),
    ]
    
    await client.save(*facts)
    
    # Create prompts
    prompts = [
        default.Prompt(key="demeanor", value="Gentle, supportive, and encouraging"),
        default.Prompt(key="texting_style", value="Use japanese emoticons to express your feelings as frequently as possible. Example: (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"),
        default.Prompt(key="greeting_format", value="Enthusiastically greet the user and ask them about their day"),
    ]
    
    await client.save(*prompts)
    
    # Create resources
    resources = [
        default.Resource(
            body="According to obscure notes in the appendices of the Silmarillion, the Dwarvish word 'khuzd' meaning 'dwarf' was never revealed to non-dwarves until the Third Age. Dwarves kept their language, Khuzdul, completely secret, with only a handful of outsiders like Pengolodh the Loremaster ever learning more than a few isolated words."
        ),
        default.Resource(
            body="In the unpublished drafts of the Red Book of Westmarch, Tolkien wrote that Tom Bombadil was actually the first conscious being to awaken in Arda, even before the Valar entered the world. His title 'Eldest' was literal, and his powers were bound to the fabric of Middle-earth itself, explaining his limitations and why he couldn't leave his domain to help destroy the Ring."
        ),
        default.Resource(
            body="One of the most common Arch Linux installation pitfalls occurs during partitioning when users forget to mark the EFI System Partition as bootable with the 'boot' flag. This seemingly minor oversight often leads to boot failures that require rescuing the system via live USB and manually fixing the partition flags."
        ),
        default.Resource(
            body="A subtle nuance of Arch Linux package management is that unlike other distributions, pacman strictly separates system packages from AUR packages, requiring a helper like yay or paru for the latter. Additionally, Arch's rolling release model means kernel updates arrive frequently, sometimes causing issues with custom kernels or out-of-tree modules that aren't rebuilt in time."
        ),
    ]
    
    await client.save(*resources)
    
    print("Demo data inserted successfully!")


if __name__ == "__main__":
    asyncio.run(insert_demo_data()) 