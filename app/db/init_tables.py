from app.db.session import engine
from app.db.base import Base

from app.db.models.user import User

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)