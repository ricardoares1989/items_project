from yoyo import read_migrations
from yoyo import get_backend

from app.src.shared.settings import Settings


def run_migrations():
    settings = Settings()
    backend = get_backend(
        f"postgresql://{settings.db_user}:{settings.db_pass}@{settings.db_host}/{settings.db_name}"
    )
    migrations = read_migrations("./app/migrations")
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))


if __name__ == "__main__":
    run_migrations()
