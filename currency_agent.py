"""
This script demonstrates how to create a simple currency conversion agent using the smolagents library.
"""

import requests

from smolagents import CodeAgent, LiteLLMModel, Tool

class ConvertCurrency(Tool):
    name = "convert_currency"
    description = "Converts an amount from one currency to another."
    inputs = {
        "amount": {
            "type": "number",
            "description": "The amount to convert."
        },
        "from_currency": {
            "type": "string",
            "description": "The currency to convert from."
        },
        "to_currency": {
            "type": "string",
            "description": "The currency to convert to."
        }
    }
    output_type = "number"

    def forward(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Converts an amount from one currency to another.

        Args:
        amount (float): The amount to convert.
        from_currency (str): The currency to convert from.
        to_currency (str): The currency to convert to.

        Returns:
        float: The converted amount.
        """

        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency.lower()}.json'
        response = requests.get(url)
        rates = response.json()[from_currency.lower()]
        converted = amount * rates[to_currency.lower()]

        return round(converted, 2)

def sample_currency_agent():
    model_id = "ollama_chat/qwen2.5" # The model ID from ollama

    model = LiteLLMModel(model_id=model_id,
                         api_base="http://localhost:11434" # The local ollama server.
                         )

    currency_converter = ConvertCurrency()

    currency_agent = CodeAgent(model=model,
                      tools=[currency_converter],
                      add_base_tools=True,
                      verbosity_level=2,
                    )

    return currency_agent

if __name__ == "__main__":
    agent = sample_currency_agent()
    agent.run("What is 100 USD in EUR?")
