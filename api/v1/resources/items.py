from api.main import mcp


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Get a greeting
    :param name:
    :return: str
    """
    return f"Hello {name}!"
