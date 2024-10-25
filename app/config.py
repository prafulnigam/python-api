import motor.motor_asyncio
from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_db_url: str = "mongodb://localhost:27017"
    mongo_db_name: str = "school_blog"

    class Config:
        env_file = ".env"

settings = Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongo_db_url)
database = client[settings.mongo_db_name]
blog_collection = database.get_collection("blogs")
