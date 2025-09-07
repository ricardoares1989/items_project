from dependency_injector import containers, providers

from src.shared.infrastructure.base_repository_postgres import BaseRepositoryPostgres
from src.shared.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])
    init_pool_connections = providers.Resource(BaseRepositoryPostgres().init)
