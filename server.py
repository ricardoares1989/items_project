from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    :param a:
    :param b:
    :return:
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


