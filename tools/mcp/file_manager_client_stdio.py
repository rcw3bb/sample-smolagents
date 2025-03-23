import asyncio

from smolagents import Tool
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

# Function to get the server parameters for the stdio client
def get_server_params() -> StdioServerParameters:
    return StdioServerParameters(command="poetry",
                                 args=["run", "python", "mcp_servers\\file_manager_server_stdio.py"])

# Base class for file manager tools
class FileManagerTool(Tool):
    def __init__(self, name: str, description: str, inputs: dict, output_type: str):
        super().__init__()
        self.name = name
        self.description = description
        self.inputs = inputs
        self.output_type = output_type

    # Forward the tool call to the MCP client
    async def forward_to_mcp(self, args : dict[str, str]) -> str:
        async with stdio_client(get_server_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return (await session.call_tool(self.name, args)).content[0].text

# Tool to read a file using the MCP client
class ReadFile(FileManagerTool):
    def forward(self, file_path: str) -> str:
        return asyncio.run(self.forward_to_mcp({"file_path" : file_path}))

# Tool to write to a file using the MCP client
class WriteFile(FileManagerTool):
    def forward(self, file_path: str, text: str) -> str:
        return asyncio.run(self.forward_to_mcp({"file_path": file_path, "text": text}))

# Asynchronously get the file manager tools from the MCP client
async def file_manager_tools() -> dict[str, Tool]:
    async with stdio_client(get_server_params()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            available_tools = await session.list_tools()

            registered_tools = {}
            for tool in available_tools.tools:
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

    return registered_tools