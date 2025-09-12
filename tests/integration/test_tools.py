import pytest
from unittest.mock import patch, Mock

from api.v1.tools.items import create_item


@pytest.mark.asyncio
async def test_create_item_tool(main_container):
    # Arrange
    item_name = "Test Item from Tool"
    item_quantity = 10

    mock_request = Mock()
    mock_request.app.state.container = main_container

    with patch('api.v1.tools.items.get_http_request', return_value=mock_request):
        # Act
        created_item_dict = await create_item(
            name=item_name,
            quantity=item_quantity,
        )

    # Assert
    assert created_item_dict is not None
    assert created_item_dict["name"] == item_name
    assert created_item_dict["quantity"] == item_quantity

    # Verify from database
    item_repository = main_container.item_repository()
    item_uuid = created_item_dict["uuid"]
    item_from_db = await item_repository.get_by_uuid(item_uuid)

    assert item_from_db is not None
    assert str(item_from_db.uuid_) == item_uuid
    assert item_from_db.name == item_name
    assert item_from_db.quantity == item_quantity
