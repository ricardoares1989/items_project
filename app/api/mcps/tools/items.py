from contextlib import asynccontextmanager
from datetime import datetime
from typing import Optional

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from app.src.items.application.create_item_use_case import CreateItemUseCase
from app.src.items.domain.item import Item
from app.src.shared.application.main_container import MainContainer
from app.src.shared.infrastructure.app_context import AppContext


@asynccontextmanager
async def lifespan_mcp(server: FastMCP):
    main_container = MainContainer()
    await main_container.init_resources()
    yield AppContext(container=main_container)
    await main_container.shutdown_resources()


api_mcp = FastMCP("API Server", lifespan=lifespan_mcp)


@api_mcp.tool("create_item")
async def create_item(
    ctx: Context[ServerSession, AppContext],
    name: str,
    quantity: Optional[int] = None,
    description: Optional[str] = None,
    planned_purchase_date: Optional[datetime] = None,
) -> dict:
    """
    Create an item
    :param ctx:
    :param name:
    :param quantity:
    :param description:
    :param planned_purchase_date:
    :return:
    """

    container = ctx.request_context.lifespan_context.container
    use_case: CreateItemUseCase = await container.create_item_use_case()
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
