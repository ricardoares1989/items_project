from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.mcps.tools.items import api_mcp
from app.src.shared.application.main_container import MainContainer


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


app.mount("/items/", api_mcp.sse_app())
