import os

if os.getenv("APP_ENV", "development") != "production":
    from dotenv import load_dotenv

    load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.auth import router as AuthRouter
from controllers.collections import router as CollectionsRouter
from controllers.notes import router as NotesRouter

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter, prefix="/api/v1/auth")
app.include_router(CollectionsRouter, prefix="/api/v1/collections")
app.include_router(NotesRouter, prefix="/api/v1/notes")
