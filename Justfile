# Justfile configurado para usar PowerShell como shell
# Usa PowerShell (clásico) con opciones para ejecución no interactiva.
set shell := ["powershell", "-NoProfile", "-NonInteractive", "-Command"]

# Ejecuta el comando uv run mcp dev server.py dentro del entorno de just
mcp-dev:
    uv run mcp dev ./api/main.py


mcp-sse:
    uv run uvicorn api.main:app