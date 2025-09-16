from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from app.db.base import Base
from config import settings
import asyncio

# Alembic config
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

DATABASE_URL = settings.DATABASE_URL

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations_online():
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async def run():
        async with connectable.begin() as conn:
            await conn.run_sync(lambda sync_conn: context.configure(connection=sync_conn, target_metadata=target_metadata))
            await conn.run_sync(lambda sync_conn: context.run_migrations())
    asyncio.run(run())

if context.is_offline_mode():
    run_migrations_offline()
else:
    do_run_migrations_online()
