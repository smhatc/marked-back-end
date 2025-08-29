from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from controllers.auth import router as AuthRouter

app = FastAPI()

app.include_router(AuthRouter, prefix="/api/v1/auth")
