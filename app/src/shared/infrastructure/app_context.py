from dataclasses import dataclass

from app.src.shared.application.main_container import MainContainer


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    container: MainContainer
