from smolagents import LiteLLMModel

model = LiteLLMModel(model_id="ollama_chat/qwen2.5", # The model ID from ollama
                     api_base="http://localhost:11434", # The local ollama server.
                     )