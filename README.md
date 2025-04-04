# Sample Usage Smolagents

[TOC]

## Overview

This project demonstrates the use of [smolagents](https://huggingface.co/docs/smolagents/en/index) from **Hugging Face** to create **AI agents**. The samples were created on **Windows** and will create files on `C:\\tmp` directory.

## Requirements

- Python >= 3.13
- [Ollama](https://github.com/ollama/ollama)
- [Hugging Face Token](https://huggingface.co/settings/tokens)

## Running the Ollama Server

To start the Ollama server, execute the following command:

```sh
ollama serve
```

> The server will listen on port 11434 by default.

## Running the Qwen2.5 Model with Ollama

While the Ollama server is running, download the model using the following command:

```sh
ollama run qwen2.5
```

> This only needs to be done once.

> This is a small agent and can get confused easily. For a more robust implementation, use a model with more parameters.

## The .env File

Create a `.env` file with the following content:

```properties
HF_TOKEN=<HUGGING_FACE_TOKEN>
```

Replace `<HUGGING_FACE_TOKEN>` with your actual Hugging Face token. This is required because all the samples use the Inference API with the following model by default:

```
Qwen/QwQ-32B
```

> Switch to **Ollama** model if needed by changing the `active_model` to `local_model` in the **model.ModelMgr** module.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/rcw3bb/sample-smolagents.git
   cd sample-smolagents
   ```

2. Install the dependencies:

   > If Poetry is not yet installed, use the following command to install it:
   >
   > ```sh
   > python -m pip install poetry
   > ```

   ```sh
   poetry install
   ```

## Non-MCP Samples

### Simple File Management with AI Agent

```sh
poetry run python -m sample.simple.file_management_sample
```

Observe if it uses the provided tools.

### Simple File Management with AI Manager Agent

```sh
poetry run python -m sample.simple.file_management_managed_sample
```

Observe if it uses the provided tools.

## MCP Stdio Server Samples

### Simple File Management with AI Agent

```sh
poetry run python -m sample.mcp.stdio.file_management_sample
```

Observe if it uses the provided tools.

### Simple File Management with AI Manager Agent

```sh
poetry run python -m sample.mcp.stdio.file_management_managed_sample
```

Observe if it uses the provided tools.

## MCP SSE Server Samples

### Starting the MCP SSE Server

The server must be running before running any sample from this section.

```sh
poetry run python -m mcp_servers.file_manager_server_sse
```

### Simple File Management with AI Agent

```sh
poetry run python -m sample.mcp.sse.file_management_sample
```

Observe if it uses the provided tools.

### Simple File Management with AI Manager Agent

```sh
poetry run python -m sample.mcp.sse.file_management_managed_sample
```

Observe if it uses the provided tools.

## Author

Ronaldo Webb