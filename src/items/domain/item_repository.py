from abc import ABC, abstractmethod

from src.items.domain.item import Item


class ItemRepository(ABC):
    @abstractmethod
    async def save(self, item: Item):
        raise NotImplementedError("Save method must be implemented.")

    @abstractmethod
    async def delete(self, item: Item):
        raise NotImplementedError("Delete method must be implemented.")

    @abstractmethod
    async def purchased(self, item: Item):
        raise NotImplementedError("Purchased method must be implemented.")
