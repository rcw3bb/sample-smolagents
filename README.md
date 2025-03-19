# Sample Usage Smolagents

## Overview

This project demonstrates the use of [smolagents](https://huggingface.co/docs/smolagents/en/index) from Hugging Face to create AI agents.

## Requirements

- Python >= 3.13
- [Ollama](https://github.com/ollama/ollama)
- [Hugging Face Token](https://huggingface.co/settings/tokens)

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

## Running the Ollama Server

To start the Ollama server, execute the following command:

```sh
ollama serve
```

> The server will listen on port 11434 by default.

## Downloading the Qwen2.5 Model

While the Ollama server is running, download the model using the following command:

```sh
ollama run qwen2.5
```

> This only needs to be done once.

> This is a small agent and can get confused easily. For a more robust implementation, use a model with more parameters.

## Sample Currency Exchange

To run the currency conversion agent, execute the following command:

> Ensure the Ollama server is running.

```sh
poetry run python -m sample_smolagents.currency_exchange_sample
```

Observe if it uses the provided tools.

## Sample Currency Exchange with Planning

To run the currency conversion agent with planning, execute the following command:

> Ensure the Ollama server is running.

```sh
poetry run python -m sample_smolagents.currency_exchange_planning_sample
```

Observe the planning process for each step.

## Sample Currency Exchange with Agent Manager

To run the currency conversion agent with a manager, execute the following command:

> Ensure the Ollama server is running.

```sh
poetry run python -m sample_smolagents.currency_exchange_managed_sample
```

Observe how the manager delegates tasks to other agents, if necessary.

## Sample File Management

1. Create a `.env` file with the following content:

   ```properties
   HF_TOKEN=<HUGGING_FACE_TOKEN>
   ```

   Replace `<HUGGING_FACE_TOKEN>` with your actual Hugging Face token. This is required because this sample uses the Inference API with the following model:

   ```
   Qwen/QwQ-32B
   ```

2. Execute the following command:

   ```sh
   poetry run python -m sample_smolagents.file_management_sample
   ```

​	Observe if it uses the provided tools.

## Author

Ronaldo Webb
