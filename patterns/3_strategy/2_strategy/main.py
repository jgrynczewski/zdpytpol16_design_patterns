from order import Order
from fedex_strategy import FedexStrategy
from upc_strategy import UpcStrategy
from shipping_cost import ShippingCost


# Teste FEDEX
order = Order()
strategy = FedexStrategy()
# strategy = UpcStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0
# assert cost == 4.0

print("OK")