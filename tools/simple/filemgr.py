from smolagents import Tool

# Tool to read a file
class ReadFile(Tool):
    # Name of the tool
    name = "read_file_tool"
    # Description of the tool
    description = "Reads a text file."
    # Input schema for the tool
    inputs = {
        "file_path": {
            "type": "string",
            "description": "The path to the file."
        }
    }
    # Output type of the tool
    output_type = "string"

    # Method to read the file content
    def forward(self, file_path: str) -> str:
        # Open the file in read mode and return its content
        with open(file_path, 'r') as file:
            return file.read()

# Tool to write to a file
class WriteFile(Tool):
    # Name of the tool
    name = "write_file_tool"
    # Description of the tool
    description = "Writes text to a file."
    # Input schema for the tool
    inputs = {
        "file_path": {
            "type": "string",
            "description": "The path to the file."
        },
        "text": {
            "type": "string",
            "description": "The text to write."
        }
    }
    # Output type of the tool
    output_type = "string"

    # Method to write text to the file
    def forward(self, file_path: str, text: str) -> str:
        # Open the file in write mode and write the text
        with open(file_path, 'w') as file:
            file.write(text)
            return "File written successfully."