from contextlib import asynccontextmanager

from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from starlette.middleware.base import BaseHTTPMiddleware

from api.depends.middlewares import get_main_container_middleware
from src.shared.application.main_container import MainContainer

mcp = FastMCP("Demo")

# Import the tools to register them


@asynccontextmanager
async def lifespan(app: FastAPI):
    main_container = MainContainer()
    await main_container.init_resources()
    app.state.container = main_container
    yield
    await main_container.shutdown_resources()


app = FastAPI(
    title="Demo",
    description="Demo server",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(BaseHTTPMiddleware, dispatch=get_main_container_middleware)

app.mount("/", mcp.sse_app())
