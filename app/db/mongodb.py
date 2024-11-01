from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import config

client: AsyncIOMotorClient = None

async def connect_db():
    global client
    client = AsyncIOMotorClient(config.mongodb_url)
    print("Connected to MongoDB")

async def close_db():
    client.close()
    print("Disconnected from MongoDB")

def get_db():
    return client[config.mongodb_name]