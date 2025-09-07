from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


app = FastAPI(
    title="Demo",
    description="Demo server",
    version="0.1.0",
)

app.mount("/", mcp.sse_app())


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    :param a:
    :param b:
    :return int:
    """
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Get a greeting
    :param name:
    :return: str
    """
    return f"Hello {name}!"
