import pytest
from unittest.mock import Mock

from app.api.mcps.tools.items import create_item
from app.src.shared.application.main_container import MainContainer
from app.src.shared.infrastructure.app_context import AppContext
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession


@pytest.mark.asyncio
async def test_create_item_tool(main_container: MainContainer):
    # Arrange
    item_name = "Test Item from Tool"
    item_quantity = 10

    # Create a mock AppContext
    app_context = AppContext(container=main_container)

    # Create a mock request_context that has a lifespan_context attribute
    mock_request_context = Mock()
    mock_request_context.lifespan_context = app_context

    # Create a mock ServerSession
    mock_session = Mock(spec=ServerSession)

    # Create a mock Context
    mock_ctx = Context(session=mock_session, request_context=mock_request_context)

    # Act
    created_item_dict = await create_item(
        ctx=mock_ctx,
        name=item_name,
        quantity=item_quantity,
    )

    # Assert
    assert created_item_dict is not None
    assert created_item_dict["name"] == item_name
    assert created_item_dict["quantity"] == item_quantity

    # Verify from database
    item_repository = await main_container.item_repository()
    item_uuid = created_item_dict["uuid"]
    item_from_db = await item_repository.get_by_uuid(item_uuid)

    assert item_from_db is not None
    assert str(item_from_db.uuid_) == item_uuid
    assert item_from_db.name == item_name
    assert item_from_db.quantity == item_quantity
