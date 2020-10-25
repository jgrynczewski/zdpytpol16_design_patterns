from abs_strategy import AbsStrategy


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 7
