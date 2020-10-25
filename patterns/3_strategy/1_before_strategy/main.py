from order import Order
from shipper import Shipper
from shipping_cost import ShippingCost


# Teste FEDEX
order = Order(Shipper.FEDEX)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

print("OK")