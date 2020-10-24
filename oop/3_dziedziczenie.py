# Dziedziczenie - mechanizm do wielokrotnego używania raz napisanego kodu

class UIControl:
    def enable(self):
        print("Enable")


class TextBox(UIControl):
    pass

t = TextBox()
t.enable()

