from contextlib import asynccontextmanager

import asyncpg


@asynccontextmanager
async def init_db(settings: dict):
    pool = await asyncpg.create_pool(
        host=settings.get("db_host"),
        database=settings.get("db_name"),
        user=settings.get("db_user"),
        password=settings.get("db_pass"),
        port=settings.get("db_port"),
        min_size=1,
        max_size=10,
    )
    yield pool
    await pool.close()
