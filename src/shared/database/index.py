from tortoise import Tortoise
import os
from dotenv import load_dotenv

#Load the environment variables
load_dotenv()

async def init():
    await Tortoise.init(
        # If you want to use other database, you can change the DATABASE_URL on the .env file
        db_url=os.getenv('DATABASE_URL'),
        modules={"models": ["src.shared.database.models"]},
    )
    # Generate the schema
    await Tortoise.generate_schemas()

async def shutdown():
    await Tortoise.close_connections()
