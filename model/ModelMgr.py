from smolagents import LiteLLMModel, HfApiModel

local_model = LiteLLMModel(model_id="ollama_chat/qwen2.5",  # The model ID from ollama
                           api_base="http://localhost:11434",  # The local ollama server.
                           )

hf_model = HfApiModel(model_id="Qwen/QwQ-32B")