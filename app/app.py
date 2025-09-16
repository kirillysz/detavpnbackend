from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.server.server import router as api_router
from app.db.init_tables import init_db

@asynccontextmanager
async def lifespan(app):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)