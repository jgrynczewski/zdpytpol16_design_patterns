import abc


class TaxCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate_tax(self):
        pass


class TaxCalculator2020(TaxCalculator):

    def calculate_tax(self):
        return 1


class TaxCalculator2021(TaxCalculator):

    def calculate_tax(self):
        return 2


class Main:
    @staticmethod
    def main(calc: TaxCalculator):
        calculator = calc
        tax = calculator.calculate_tax()
        return tax


print(Main.main(TaxCalculator2021()))
