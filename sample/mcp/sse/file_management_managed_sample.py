import asyncio

from smolagents import CodeAgent, LogLevel
from tools.mcp.file_manager_client_sse import file_manager_tools
from model.ModelMgr import active_model
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Asynchronously retrieve the file manager tools from the MCP client
tools = asyncio.run(file_manager_tools())

# Create an instance of CodeAgent for reading files
read_file_agent = CodeAgent(model=active_model,
                            name="read_file_agent",  # Name of the agent
                            description="An agent that reads a file",  # Description of the agent
                            tools=[tools['read_file']],  # Tools available to the agent
                            )

# Create an instance of CodeAgent for writing files
write_file_agent = CodeAgent(model=active_model,
                             name="write_file_agent",  # Name of the agent
                             description="An agent that writes a file",  # Description of the agent
                             tools=[tools['write_file']],  # Tools available to the agent
                             )

# Create a manager agent to manage the read and write file agents
agents_manager = CodeAgent(model=active_model,
                           tools=[],  # No direct tools, only managed agents
                           managed_agents=[read_file_agent, write_file_agent],  # Agents managed by this manager
                           verbosity_level=LogLevel.DEBUG,  # Set verbosity level to DEBUG for detailed logging
                           )

# Run the manager agent with a task to write text to a file and then read its content
agents_manager.run("Write the text \"Hello, World!\" to \"C:/tmp/mcp-sse-managed-hello.txt\" and show me its content.")