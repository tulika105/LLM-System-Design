from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LLM System Design API")

app.include_router(router)