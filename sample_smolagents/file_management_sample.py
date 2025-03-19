from smolagents import CodeAgent, LogLevel
from file_tool.filemgr import ReadFile, WriteFile
from model.ModelMgr import hf_model
from dotenv import load_dotenv

load_dotenv()

read_file = ReadFile()
write_file = WriteFile()

agent = CodeAgent(model=hf_model,
                  tools=[read_file,
                         write_file,
                         ],
                  max_steps=12,
                  verbosity_level=LogLevel.DEBUG,
                  )
agent.run("Write the text \"Hello, World!\" to \"C:/tmp/hello.txt\".")
agent.run("Read the content of the \"C:/tmp/hello.txt\".")