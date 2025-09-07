import os
import asyncpg
from typing import Optional


class BaseRepositoryPostgres:
    _instance: Optional["BaseRepositoryPostgres"] = None
    _pool: Optional[asyncpg.pool.Pool] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseRepositoryPostgres, cls).__new__(cls)
        return cls._instance

    async def init(
        self,
    ):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                host=os.getenv("DB_HOST", "localhost"),
                database=os.getenv("DB_NAME", "postgres"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASS", "postgres"),
                port=int(os.getenv("DB_PORT", 5432)),
                min_size=1,
                max_size=10,
            )

    def get_pool(self) -> asyncpg.pool.Pool:
        if self._pool is None:
            raise Exception(
                "Connection pool not initialized. Call 'await init()' first."
            )
        return self._pool
