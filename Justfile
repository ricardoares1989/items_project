# Justfile configurado para usar PowerShell como shell
# Usa PowerShell (clásico) con opciones para ejecución no interactiva.
set shell := ["powershell", "-NoProfile", "-NonInteractive", "-Command"]

# Ejecuta el comando uv run mcp dev server.py dentro del entorno de just
mcp-dev:
    uv run mcp dev ./app/api/main.py


mcp-sse:
    uv run python -m uvicorn app.api.main:app --reload

run-migrations:
    uv run python -m app.src.shared.infrastructure.run_migrations