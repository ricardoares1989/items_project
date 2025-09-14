from datetime import datetime
from typing import Optional

from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

from api.main import mcp
from src.items.application.create_item_use_case import CreateItemUseCase
from src.items.domain.item import Item


@mcp.tool()
async def create_item(
    name: str,
    quantity: Optional[int] = None,
    description: Optional[str] = None,
    planned_purchase_date: Optional[str] = None,
) -> dict:
    """
    Create an item
    :param name:
    :param quantity:
    :param description:
    :param planned_purchase_date:
    :return:
    """
    planned_date = None
    if planned_purchase_date:
        try:
            planned_date = datetime.fromisoformat(planned_purchase_date)
        except ValueError:
            raise ValueError(
                "planned_purchase_date must be in ISO format, e.g. '2025-09-14T00:00:00'"
            )

    request: Request = get_http_request()
    container = request.state.container
    use_case: CreateItemUseCase = container.create_item_use_case()
    item: Item = await use_case(
        name=name,
        quantity=quantity,
        description=description,
        planned_purchase_date=planned_date,
    )
    return {
        "uuid": str(item.uuid_),
        "name": item.name,
        "quantity": item.quantity,
        "description": item.description,
        "planned_purchase_date": str(item.planned_purchase_date),
        "created_datetime": str(item.created_datetime),
        "modified_datetime": str(item.modified_datetime),
    }
