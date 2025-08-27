from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            await session.initialize()
            resources = await session.list_resource_templates()
            print("LISTING RESOURCES")
            for resource in resources:
                print(resource)
            tools = await session.list_tools()
            print("LISTING TOOLS")
            for tool in tools:
                print(tool)

            print("READING RESOURCE")
            content, mime_type = await session.read_resource(
                "greeting://hello"
            )
            print(f"El contenido es {content}, su mime type es {mime_type}")
            print("CALL TOOL")
            result = await session.call_tool("add", arguments={
                "a": 1, "b": 23
            })
            print(result.content)


if __name__ == '__main__':
    import asyncio

    asyncio.run(run())