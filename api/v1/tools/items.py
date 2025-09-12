from typing import Optional
from datetime import datetime

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
    planned_purchase_date: Optional[datetime] = None,
) -> dict:
    """
    Create an item
    :param name:
    :param quantity:
    :param description:
    :param planned_purchase_date:
    :return:
    """
    request: Request = get_http_request()
    container = request.app.state.container
    item_repository = container.item_repository()
    use_case = CreateItemUseCase(repository=item_repository)
    item: Item = await use_case(
        name=name,
        quantity=quantity,
        description=description,
        planned_purchase_date=planned_purchase_date,
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
