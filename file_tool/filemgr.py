from smolagents import Tool

class ReadFile(Tool):
    name = "read_file_tool"
    description = "Reads a text file."
    inputs = {
        "file_path": {
            "type": "string",
            "description": "The path to the file."
        }
    }
    output_type = "string"

    def forward(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()

class WriteFile(Tool):
    name = "write_file_tool"
    description = "Writes text to a file."
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
    output_type = "string"

    def forward(self, file_path: str, text: str) -> str:
        with open(file_path, 'w') as file:
            file.write(text)
            return "File written successfully."