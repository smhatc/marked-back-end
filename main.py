from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from controllers.auth import router as AuthRouter
from controllers.collections import router as CollectionsRouter

app = FastAPI()

app.include_router(AuthRouter, prefix="/api/v1/auth")
app.include_router(CollectionsRouter, prefix="/api/v1/collections")
