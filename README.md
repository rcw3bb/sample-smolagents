# Sample Usage Smolagents

## Overview

This project demonstrates the use of [smolagents](https://huggingface.co/docs/smolagents/en/index) from Hugging Face to create AI agents.

## Requirements

- Python >= 3.13
- [Ollama](https://github.com/ollama/ollama)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rcw3bb/sample-smolagents.git
    cd sample-smolagents
    ```

2. Install the dependencies:
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

> This must be done only once.

> This is a small agent that can get confused easily. For the actual implementation, use a model with more parameters.

## Sample Currency Exchange

To run the currency conversion agent, execute the following command:

> Ensure that the Ollama server is running.

```sh
poetry run currency_exchange_sample.py
```

Observe it uses the tools provided.

## Sample Currency Exchange with Planning

To run the currency conversion agent with planning, execute the following command:

> Ensure that the Ollama server is running.

```sh
poetry run currency_exchange_planning_sample.py
```

Observe the planning that happens for each step.

## Sample Currency Exchange with Agent Manager

To run the currency conversion agent with a manager, execute the following command:

> Ensure that the Ollama server is running.

```sh
poetry run currency_exchange_managed_sample.py
```

Observe how the manager delegates tasks to other agents if necessary.

## Author

Ronaldo Webb