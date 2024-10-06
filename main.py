from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.shared.database.index  import init, shutdown
from src.modules.Contact.controller import ContactController

app = FastAPI()

async def lifespan(app: FastAPI):
    await init()
    yield # Runnig the application
    await shutdown()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(ContactController.router, prefix="/contacts")

@app.get("/")
def read_root():
    return {"Bem vindo a API de contatos 🚀🚀🚀"}
