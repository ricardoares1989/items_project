from dependency_injector import containers, providers

from src.shared.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])
