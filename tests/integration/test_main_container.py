import pytest
import uuid

from src.items.domain.item import Item
from src.items.domain.item_repository import ItemRepository


@pytest.mark.asyncio
async def test_main_container(main_container):
    item_repository: ItemRepository = main_container.item_repository()
    await item_repository.save(Item(uuid_=uuid.uuid4(), name="test_item"))
