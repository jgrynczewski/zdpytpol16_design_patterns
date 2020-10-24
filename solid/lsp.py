# LSP - Liscov Substitution Principle (Zasada podstawień Liskova)
# Podklasy powinny być w stanie zastąpić swoich rodziców w kodzie klienta.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = 10 * w
    print(f"Oczekiwana wartość: {expected_area}, rzeczywistość wartość {rc.area}")

rc = Rectangle(5, 3)
use_it(rc)

# Łamiemy zasadę lsp
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

sq = Square(5)
use_it(sq)
