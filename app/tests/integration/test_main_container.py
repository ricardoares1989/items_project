import pytest
import uuid

from app.src.items.domain.item import Item
from app.src.items.domain.item_repository import ItemRepository


@pytest.mark.asyncio
async def test_main_container(main_container):
    item_repository: ItemRepository = await main_container.item_repository()
    await item_repository.save(Item(uuid_=uuid.uuid4(), name="test_item"))
