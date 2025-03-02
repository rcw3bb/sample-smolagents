from smolagents import CodeAgent, LogLevel
from currency_tool.currency import ServiceChargeCalculator, ServiceChargeRateProvider, ExchangeRate
from model.ModelMgr import model

service_charge_rate = ServiceChargeRateProvider()
calculate_service_charge = ServiceChargeCalculator()
exchange_rate = ExchangeRate()

agent = CodeAgent(model=model,
                  tools=[service_charge_rate,
                         calculate_service_charge,
                         exchange_rate,
                         ],
                  max_steps=12,
                  verbosity_level=LogLevel.DEBUG,
                  )

agent.run("Convert 100 USD to EUR.")