from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.db import init_db
import os
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app starts
    init_db()
    yield
    # after app stops

app = FastAPI(lifespan=lifespan)

app.include_router(chat_router, prefix="/api/chats")

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("'API_KEY' was not set")

@app.get("/")
def read_index():
    return {"message": "Hello World from FastAPI"}

