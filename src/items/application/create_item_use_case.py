import uuid
from datetime import datetime
from typing import Optional

from src.items.domain.item import Item
from src.items.domain.item_repository import ItemRepository


class CreateItemUseCase:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def __call__(
        self,
        name: str,
        quantity: Optional[int] = None,
        description: Optional[str] = None,
        planned_purchase_date: Optional[datetime] = None,
    ) -> Item:
        item = Item(
            uuid_=uuid.uuid4(),
            name=name,
            quantity=quantity,
            description=description,
            planned_purchase_date=planned_purchase_date,
            created_datetime=datetime.now(),
            modified_datetime=datetime.now(),
        )
        await self.repository.save(item)
        return item
