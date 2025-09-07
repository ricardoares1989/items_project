import asyncpg
from typing import Optional


class BaseRepositoryPostgres:
    _instance: Optional["BaseRepositoryPostgres"] = None
    _pool: Optional[asyncpg.pool.Pool] = None

    @classmethod
    async def init(cls, settings: dict):
        if cls._pool is None:
            cls._pool = await asyncpg.create_pool(
                host=settings.get("db_host"),
                database=settings.get("db_name"),
                user=settings.get("db_user"),
                password=settings.get("db_pass"),
                port=settings.get("db_port"),
                min_size=1,
                max_size=10,
            )

    def get_pool(self) -> asyncpg.pool.Pool:
        if self._pool is None:
            raise Exception(
                "Connection pool not initialized. Call 'await init()' first."
            )
        return self._pool
