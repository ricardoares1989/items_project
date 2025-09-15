from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import json
from openai.types.responses import ResponseFunctionToolCall

from app.src.shared.settings import Settings
from openai import OpenAI

settings = Settings()

server_params = StdioServerParameters(
    command="uv", args=["run", "uvicorn", "app.api.main:app"], env=None
)


def convert_to_llm_tool(tool: types.Tool):
    tool_schema = {
        "name": tool.name,
        "description": tool.description,
        "type": "function",
        "parameters": {"type": "object", "properties": tool.inputSchema["properties"]},
    }
    return tool_schema


def call_llm_to_retrieve_arguments(prompt: str, functions):
    tool_calls = []
    with OpenAI(api_key=settings.openai_api_key) as client:
        chat_completion = client.responses.create(
            model="gpt-4o", tools=functions, input=prompt
        )
    for response in chat_completion.output:
        if isinstance(response, ResponseFunctionToolCall):
            tool_calls.append(
                {"name": response.name, "args": json.loads(response.arguments)}
            )
    return tool_calls


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            resources = await session.list_resource_templates()
            print("LISTING RESOURCES")
            for resource in resources:
                print(resource)
            tools: types.ListToolsResult = await session.list_tools()
            print("LISTING TOOLS")
            functions = []
            for tool in tools.tools:
                functions.append(convert_to_llm_tool(tool))
            prompt = "agrega 2 a 50, si no obtienes respuesta, retorna una disculpa"
            arguments_retrieved = call_llm_to_retrieve_arguments(prompt, functions)
            for f in arguments_retrieved:
                result = await session.call_tool(f["name"], f["args"])
                print("Respuesta", result.content[0].text)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
