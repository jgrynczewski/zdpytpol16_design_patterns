from abs_strategy import AbsStrategy


class UpcStrategy(AbsStrategy):
    def calculate(self, order):
        return 4