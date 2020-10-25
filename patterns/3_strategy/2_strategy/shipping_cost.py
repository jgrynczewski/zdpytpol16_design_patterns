from abs_strategy import AbsStrategy


class ShippingCost:
    def __init__(self, strategy: AbsStrategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)
