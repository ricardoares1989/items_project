from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

mcp = FastMCP("Demo")

app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app())
    ]
)

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    :param a:
    :param b:
    :return int:
    """
    return a + b

@mcp.resource(
    "greeting://{name}"
)
def get_greeting(name: str) -> str:
    """
    Get a greeting
    :param name:
    :return: str
    """
    return f"Hello {name}!"


