from typing import Optional
from datetime import datetime
from src.shared.domain.aggregate_root import AggregateRoot
from src.shared.domain.event import CloudEvent


class Item(AggregateRoot):
    def __init__(
        self,
        name: str,
        quantity: Optional[int] = None,
        description: Optional[str] = None,
        planned_purchase_date: Optional[datetime] = None,
        created_datetime: Optional[datetime] = datetime.now(),
        modified_datetime: Optional[datetime] = datetime.now(),
    ):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.created_datetime = created_datetime
        self.modified_datetime = modified_datetime
        self.planned_purchase_date = planned_purchase_date

    def on_save_event(self) -> CloudEvent:
        return CloudEvent(
            source="items",
            type="purchased.items.item_saved",
            datacontenttype="application/json",
            data={
                "name": self.name,
                "quantity": self.quantity,
                "description": self.description,
                "planned_purchase_date": str(self.planned_purchase_date),
                "created_datetime": str(self.created_datetime),
            },
        )
