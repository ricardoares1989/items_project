from src.items.domain.item import Item
from src.items.domain.item_repository import ItemRepository
from src.shared.infrastructure.base_repository_postgres import BaseRepositoryPostgres
from datetime import datetime


class ItemPostgresRepository(BaseRepositoryPostgres, ItemRepository):

    def __init__(self):
        super().__init__()
        self._connection_pool = self.get_pool()

    async def save(self, item: Item):
        query = """
            INSERT INTO items (uuid, name, quantity, description, created_datetime, modified_datetime, planned_purchase_date)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
            ON CONFLICT (name) DO UPDATE SET
                quantity = EXCLUDED.quantity,
                description = EXCLUDED.description,
                modified_datetime = NOW(),
                planned_purchase_date = EXCLUDED.planned_purchase_date;
        """
        async with self._connection_pool.acquire() as conn:
            await conn.execute(
                query,
                str(item.uuid_),
                item.name,
                item.quantity,
                item.description,
                item.created_datetime,
                datetime.now(),
                item.planned_purchase_date,
            )

    async def delete(self, item: Item):
        query = "DELETE FROM items WHERE uuid = $1;"
        async with self._connection_pool.acquire() as conn:
            await conn.execute(query, item.uuid_)

    async def purchased(self, item: Item):
        query = "UPDATE items SET modified_datetime = $1 WHERE uuid = $2;"
        async with self._connection_pool.acquire() as conn:
            await conn.execute(query, datetime.now(), item.uuid_)
