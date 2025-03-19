from smolagents import CodeAgent, LogLevel
from currency_tool.currency import ServiceChargeCalculator, ServiceChargeRateProvider, ExchangeRate
from model.ModelMgr import local_model

service_charge_rate = ServiceChargeRateProvider()
calculate_service_charge = ServiceChargeCalculator()
exchange_rate = ExchangeRate()

agent = CodeAgent(model=local_model,
                  tools=[service_charge_rate,
                         calculate_service_charge,
                         exchange_rate,
                         ],
                  planning_interval=1, # The agent will do the planning every step.
                  max_steps=12,
                  verbosity_level=LogLevel.DEBUG,
                )

agent.run("Convert 100 USD to EUR.")
