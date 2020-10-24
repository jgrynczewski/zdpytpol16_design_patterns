# OCP - Open Close Principle (Zasada otwarte-zamknięte)
# Otwarte na rozbudowę, zamknięte na modyfikację.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# Łamiemy zasadę OCP
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print("Green products:")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f" - {p.name}")

print("Large products:")
for p in pf.filter_by_size(products, Size.LARGE):
    print(f" - {p.name}")

print("Large and green products:")
for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.GREEN):
    print(f" - {p.name}")

# Refaktoryzacja (wzorzec Specyfikacja z Enterprise design patterns)
class Specification():
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


print("Green products (new way):")
green_spec = ColorSpecification(Color.GREEN)
bf = BetterFilter()
for p in bf.filter(products, green_spec):
    print(f"- {p.name}")


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

print("Large products (new way):")
large_spec = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large_spec):
    print(f"- {p.name}")
