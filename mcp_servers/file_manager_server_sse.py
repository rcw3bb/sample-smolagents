import uvicorn
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.types import TextContent, ImageContent, EmbeddedResource, Tool
from starlette.applications import Starlette
from starlette.routing import Route, Mount

# Asynchronously reads a file and returns its content wrapped in a TextContent object
async def read_file(file_path: str) -> list[TextContent | ImageContent | EmbeddedResource]:
    with open(file_path, 'r') as file:
        return [TextContent(type="text", text=file.read())]

# Asynchronously writes text to a file and returns a success message wrapped in a TextContent object
async def write_file(file_path: str, text: str) -> list[TextContent | ImageContent | EmbeddedResource]:
    with open(file_path, 'w') as file:
        file.write(text)
    return [TextContent(type="text", text="File written successfully.")]

# Create an instance of the Server class with the name "MCP File Manager Server"
app = Server("MCP File Manager Server")
# Create an instance of the SseServerTransport class with the endpoint "/messages/"
sse = SseServerTransport("/messages/")
# Define the port number for the server
port = 8000

# Define a tool that can be called by the server to read or write files
@app.call_tool()
async def fetch_tool(name: str, arguments: dict) -> list[TextContent | ImageContent | EmbeddedResource]:
    if name == "read_file":
        if "file_path" not in arguments:
            raise ValueError("Missing required argument 'file_path'")
        return await read_file(arguments["file_path"])
    elif name == "write_file":
        if "file_path" not in arguments:
            raise ValueError("Missing required argument 'file_path'")
        if "text" not in arguments:
            raise ValueError("Missing required argument 'text'")
        return await write_file(arguments["file_path"], arguments["text"])

    return []

# Define a tool that lists all available tools
@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="read_file",
            description="Reads a text file.",
            inputSchema={
                "type": "object",
                "required": ["file_path"],
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file.",
                    }
                },
            },
        ),
        Tool(
            name="write_file",
            description="Writes text to a file.",
            inputSchema={
                "type": "object",
                "required": ["file_path", "text"],
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file.",
                    },
                    "text": {
                        "type": "string",
                        "description": "The text to write.",
                    }
                },
            },
        )
    ]

# Handle Server-Sent Events (SSE) connections
async def handle_sse(request):
    async with sse.connect_sse(
            request.scope, request.receive, request._send
    ) as (read_stream, write_stream):
        await app.run(
            read_stream, write_stream, app.create_initialization_options()
        )

# Main function to start the server
def main():
    # Create a Starlette application with routes for SSE and message handling
    starlette_app = Starlette(
        debug=True,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )

    # Run the Starlette application using Uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=port)

# Entry point of the script
if __name__ == "__main__":
    main()