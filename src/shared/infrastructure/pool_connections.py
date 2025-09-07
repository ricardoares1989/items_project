import asyncpg

from src.shared.settings import Settings


async def create_pool_connection(settings: Settings):
    await asyncpg.create_pool(
        host=settings.db_host,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_pass,
        port=settings.db_port,
        min_size=1,
        max_size=10,
    )
