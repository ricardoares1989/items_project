import pytest

from app.src.shared.application.main_container import MainContainer


@pytest.fixture
async def main_container():
    main_container = MainContainer()
    await main_container.init_resources()
    yield main_container
    await main_container.shutdown_resources()