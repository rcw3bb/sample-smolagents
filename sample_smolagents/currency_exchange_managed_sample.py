from smolagents import CodeAgent, LogLevel
from currency_tool.currency import ServiceChargeCalculator, ServiceChargeRateProvider, ExchangeRate
from model.ModelMgr import local_model

service_charge_rate = ServiceChargeRateProvider()
calculate_service_charge = ServiceChargeCalculator()
exchange_rate = ExchangeRate()

service_charge_agent = CodeAgent(model=local_model,
                                 name="service_charge_agent",
                                 description="Calculate the latest fixed service change rate.",
                                 tools=[calculate_service_charge, service_charge_rate],
                                 )

exchange_rate_agent = CodeAgent(model=local_model,
                                name="exchange_rate_agent",
                                description="The realtime exchange rate",
                                tools=[exchange_rate],
                                )

agents_manager = CodeAgent(model=local_model,
                           tools=[],
                           managed_agents=[service_charge_agent, exchange_rate_agent],
                           verbosity_level=LogLevel.DEBUG,
                           )

agents_manager.run("Convert 100 USD to EUR.")