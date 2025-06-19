#!/usr/bin/env python3
"""
Delete all data using Gel Python query builder
"""

import asyncio
from models import default
import gel


async def delete_all_data():
    """Delete all data from the database"""
    client = gel.create_async_client()
    
    # Delete all records from each table
    # Order matters due to foreign key constraints - delete referencing tables first
    await client.query(default.Resource.delete())
    await client.query(default.Prompt.delete())
    await client.query(default.Fact.delete())
    await client.query(default.Chat.delete())
    await client.query(default.Message.delete())
    
    print("All data deleted successfully!")


if __name__ == "__main__":
    asyncio.run(delete_all_data()) 