from smolagents import CodeAgent, LogLevel
from currency_tool.currency import ServiceChargeCalculator, ServiceChargeRateProvider, ExchangeRate
from model.ModelMgr import model

service_charge_rate = ServiceChargeRateProvider()
calculate_service_charge = ServiceChargeCalculator()
exchange_rate = ExchangeRate()

service_charge_agent = CodeAgent(model=model,
                                 name="service_charge_agent",
                                 description="The agent that provides the latest service charge rate then "
                                             "calculates the service charge.",
                                 tools=[calculate_service_charge, service_charge_rate],
                                 )

exchange_rate_agent = CodeAgent(model=model,
                                name="exchange_rate_agent",
                                description="The agent that retrieves the current exchange rate",
                                tools=[exchange_rate],
                                )

agents_manager = CodeAgent(model=model,
                           tools=[],
                           managed_agents=[service_charge_agent, exchange_rate_agent],
                           verbosity_level=LogLevel.DEBUG,
                           )

agents_manager.run("Convert 100 USD to EUR.")