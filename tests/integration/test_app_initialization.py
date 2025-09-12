from fastapi.testclient import TestClient

from api.main import app
from src.shared.infrastructure.base_repository_postgres import BaseRepositoryPostgres


def test_app_initialization():
    with TestClient(app) as client:
        assert client.app.state.container is not None
        pool = BaseRepositoryPostgres().get_pool()
        assert pool is not None
