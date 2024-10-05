from fastapi import FastAPI
from src.shared.database.index  import init, shutdown

app = FastAPI()

async def lifespan(app: FastAPI):
    await init()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)
    
@app.get("/")
def read_root():
    return {"Bem vindo a API de contatos 🚀🚀🚀"}
