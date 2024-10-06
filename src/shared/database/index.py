from tortoise import Tortoise
import os
from dotenv import load_dotenv

#Load the environment variables
load_dotenv()

async def init():
    # Configurações individuais do banco de dados
    db_config = {
        "connections": {
            "default": {
                "engine": os.getenv('DB_ENGINE'),
                "credentials": {
                    "host": os.getenv('DB_HOST'),
                    "port": os.getenv('DB_PORT'),
                    "user": os.getenv('DB_USER'),
                    "password": os.getenv('DB_PASSWORD'),
                    "database": os.getenv('DB_NAME'),
                }
            }
        },
        "apps": {
            "models": {
                "models": ["src.shared.database.models"],
                "default_connection": "default",
            }
        }
    }

    # Inicializa o Tortoise ORM com a configuração em forma de dicionário
    await Tortoise.init(config=db_config)
    await Tortoise.generate_schemas()

async def shutdown():
    await Tortoise.close_connections()
