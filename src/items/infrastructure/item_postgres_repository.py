from src.items.domain.item import Item
from src.items.domain.item_repository import ItemRepository
from src.shared.infrastructure.base_repository_postgres import BaseRepositoryPostgres
from datetime import datetime


class ItemPostgresRepository(ItemRepository, BaseRepositoryPostgres):

    def __init__(self):
        super().__init__()
        self._connection_pool = self.get_pool()

    async def save(self, item: Item):
        query = """
            INSERT INTO items (uuid, name, quantity, description, created_datetime, modified_datetime, planned_purchase_date)
            VALUES ($1, $2, $3, $4, $5, $6, $7);
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

    async def get_by_uuid(self, uuid: str) -> Item:
        query = "SELECT * FROM items WHERE uuid = $1;"
        async with self._connection_pool.acquire() as conn:
            row = await conn.fetchrow(query, uuid)
            if row:
                return Item(
                    uuid_=row['uuid'],
                    name=row['name'],
                    quantity=row['quantity'],
                    description=row['description'],
                    planned_purchase_date=row['planned_purchase_date'],
                    created_datetime=row['created_datetime'],
                    modified_datetime=row['modified_datetime'],
                )
