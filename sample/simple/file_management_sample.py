from smolagents import CodeAgent, LogLevel
from tools.simple.filemgr import ReadFile, WriteFile
from model.ModelMgr import active_model
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Create instances of the ReadFile and WriteFile tools
read_file = ReadFile()
write_file = WriteFile()

# Create an instance of CodeAgent with the specified model and tools
agent = CodeAgent(model=active_model,
                  tools=[read_file,  # Tool to read a file
                         write_file,  # Tool to write to a file
                         ],
                  max_steps=12,  # Maximum number of steps the agent can take
                  verbosity_level=LogLevel.DEBUG,  # Set the verbosity level to DEBUG for detailed logging
                  )

# Run the agent with a specific task to write text to a file and then read its content
agent.run("Write the text \"Hello, World!\" to \"C:/tmp/simple-hello.txt\" and show me its content.")