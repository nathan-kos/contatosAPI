from fastapi import FastAPI
from src.shared.database.index  import init, shutdown
from src.modules.Contact.controller import ContactController

app = FastAPI()

async def lifespan(app: FastAPI):
    await init()
    yield # Runnig the application
    await shutdown()

app = FastAPI(lifespan=lifespan)

# Include the routes
app.include_router(ContactController.router, prefix="/contacts")

@app.get("/")
def read_root():
    return {"Bem vindo a API de contatos 🚀🚀🚀"}
