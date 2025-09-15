from dependency_injector import containers, providers

from app.src.items.application.create_item_use_case import CreateItemUseCase
from app.src.items.infrastructure.item_postgres_repository import ItemPostgresRepository
from app.src.shared.infrastructure.pool_connections import (
    init_db,
)
from app.src.shared.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])
    init_pool_connections = providers.Resource(init_db, config)
    item_repository = providers.Singleton(
        ItemPostgresRepository,
        pool_db=init_pool_connections,
        # Espera que el pool esté inicializado antes de crear el repositorio
    )
    create_item_use_case = providers.Factory(
        CreateItemUseCase,
        repository=item_repository,
    )
