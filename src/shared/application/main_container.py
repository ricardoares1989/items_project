from dependency_injector import containers, providers

from src.items.application.create_item_use_case import CreateItemUseCase
from src.items.infrastructure.item_postgres_repository import ItemPostgresRepository
from src.shared.infrastructure.base_repository_postgres import BaseRepositoryPostgres
from src.shared.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])
    init_pool_connections = providers.Resource(BaseRepositoryPostgres().init, config)
    item_repository = providers.Singleton(
        ItemPostgresRepository,
        # Espera que el pool esté inicializado antes de crear el repositorio
    )
    create_item_use_case = providers.Factory(
        CreateItemUseCase,
        repository=item_repository,
    )
