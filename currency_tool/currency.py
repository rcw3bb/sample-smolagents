import requests
from smolagents import Tool


class ExchangeRate(Tool):
    name = "exchange_rate_tool"
    description = "Provides the latest exchange rate."
    inputs = {
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

    def forward(self, from_currency: str, to_currency: str) -> float:
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency.lower()}.json'
        response = requests.get(url)
        currency = from_currency.lower()
        rates = response.json()[currency]

        return rates[currency]

class ServiceChargeRateProvider(Tool):
    name = "service_charge_rate_tool"
    description = "Provides the latest service charge rate to use in calculating the service charge."
    inputs = {}
    output_type = "number"

    def forward(self) -> float:
        return 0.05

class ServiceChargeCalculator(Tool):
    name = 'calculate_service_charge_tool'
    description = 'Calculate the service charge for the currency exchange.'
    inputs = {
        "amount": {
            "type": "number",
            "description": "The amount to exchange."
        },
        "rate": {
            "type": "number",
            "description": "The service charge rate."
        }
    }

    output_type = "number"

    def forward(self, amount: float, rate: float) -> float:
        return round(amount * rate, 2)
