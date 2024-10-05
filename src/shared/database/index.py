from tortoise import Tortoise
import os
from dotenv import load_dotenv

#Carrega as variáveis de ambiente
load_dotenv()

async def init():
    await Tortoise.init(
        db_url=os.getenv('DATABASE_URL'),
        modules={"models": ["src.shared.database.models"]},  # Ajuste o caminho para os modelos 
    )
    await Tortoise.generate_schemas()

async def shutdown():
    await Tortoise.close_connections()