import asyncio

from smolagents import CodeAgent, LogLevel
from tools.mcp.file_manager_client_sse import file_manager_tools
from model.ModelMgr import active_model
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Create an instance of CodeAgent with the specified model and tools
agent = CodeAgent(model=active_model,
                  tools=[value for value in asyncio.run(file_manager_tools()).values()],  # Retrieve and use all file manager tools
                  max_steps=12,  # Maximum number of steps the agent can take
                  verbosity_level=LogLevel.DEBUG,  # Set verbosity level to DEBUG for detailed logging
                  )

# Run the agent with a specific task to write text to a file and then read its content
agent.run("Write the text \"Hello, World!\" to \"C:/tmp/mcp-sse-hello.txt\" and show me its content.")