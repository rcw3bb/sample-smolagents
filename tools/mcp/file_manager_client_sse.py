import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from smolagents import Tool

from mcp import ClientSession
from mcp.client.sse import sse_client

# Class to manage the MCP client connection and tool interactions
class MCPClient:
    def __init__(self, url: str):
        self._url = url
        self._streams_context = None
        self._session_context = None
        self._tools = None
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    # Asynchronously get a session and initialize it
    async def _get_session(self):
        self._streams_context = sse_client(url=self._url)
        streams = await self._streams_context.__aenter__()

        self._session_context = ClientSession(*streams)
        self.session: ClientSession = await self._session_context.__aenter__()

        await self.session.initialize()

        return self.session

    # Cleanup the session and streams context
    async def cleanup(self):
        if self._session_context:
            await self._session_context.__aexit__(None, None, None)
        if self._streams_context:
            await self._streams_context.__aexit__(None, None, None)

    # List available tools from the session
    async def list_tools(self):
        session = (await self._get_session())
        response = (await session.list_tools())

        return response.tools

    # Call a specific tool with given arguments
    async def call_tool(self, tool_name, arguments):
        session = (await self._get_session())
        response = (await session.call_tool(tool_name, arguments))

        return response

# Base class for file manager tools
class FileManagerTool(Tool):
    def __init__(self, name: str, description: str, inputs: dict, output_type: str):
        super().__init__()
        self.name = name
        self.description = description
        self.inputs = inputs
        self.output_type = output_type

    # Forward the tool call to the MCP client
    async def forward_to_mcp(self, args : dict[str, str]) -> str | None:
        client = MCPClient("http://localhost:8000/sse")
        try:
            return (await client.call_tool(self.name, args)).content[0].text
        finally:
            await client.cleanup()

# Tool to read a file using the MCP client
class ReadFile(FileManagerTool):
    def forward(self, file_path: str) -> str:
        return asyncio.run(self.forward_to_mcp({"file_path" : file_path}))

# Tool to write to a file using the MCP client
class WriteFile(FileManagerTool):
    def forward(self, file_path: str, text: str) -> str:
        return asyncio.run(self.forward_to_mcp({"file_path": file_path, "text": text}))

# Asynchronously get the file manager tools from the MCP client
async def file_manager_tools() -> dict[str, Tool] | None:
    registered_tools = {}
    client = MCPClient("http://localhost:8000/sse")
    try:
        available_tools = (await client.list_tools())

        for tool in available_tools:
            name = tool.name
            description = tool.description
            output_type = 'string'
            properties = tool.inputSchema['properties']
            prop_names = properties.keys()
            inputs = {}
            for prop_name in prop_names:
                prop = properties[prop_name]
                prop_desc = prop['description']
                prop_type = prop['type']
                inputs[prop_name] = {
                    "type": prop_type,
                    "description": prop_desc
                }

            smol_tool = None

            if name == "read_file":
                smol_tool = ReadFile(name=name, description=description, inputs=inputs, output_type=output_type)

            elif name == "write_file":
                smol_tool = WriteFile(name=name, description=description, inputs=inputs, output_type=output_type)

            if smol_tool:
                registered_tools[name] = smol_tool
    finally:
        await client.cleanup()

    return registered_tools