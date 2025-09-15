from fastapi.testclient import TestClient

from app.api.main import app


def test_app_initialization():
    with TestClient(app) as client:
        assert client.app.state.container is not None
        pool = client.app.state.container.init_pool_connections()
        assert pool is not None
