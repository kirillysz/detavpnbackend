from fastapi import FastAPI
from app.api.server.server import router as api_router

app = FastAPI()

app.include_router(api_router)
