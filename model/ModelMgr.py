from smolagents import LiteLLMModel, HfApiModel

# Initialize a local model using LiteLLMModel with the specified model ID and API base URL
local_model = LiteLLMModel(model_id="ollama_chat/qwen2.5",  # The model ID from ollama
                           api_base="http://localhost:11434",  # The local ollama server.
                           )

# Initialize a Hugging Face model using HfApiModel with the specified model ID
hf_model = HfApiModel(model_id="Qwen/QwQ-32B")

# Set the active model
active_model = hf_model