# Enkapsulacja - powiązanie danych z metodami (kapsułka)

class Account:
    def __init__(self, balance):
        self.balance = balance

a = Account(100)
a.balance = 250
a.balance = -350
a.balance = "asd"

print(a.balance)

class Account:
    def __init__(self, balance):
        self.balance = balance

    # setter atrybutu balance
    def set_balance(self, value):
        if type(value) != int or value < 0:
            print("Podano niepoprawną wartość!")
        else:
            self.balance = value

    # getter atrybutu balance
    def get_balance(self):
        return self.balance

print("""Version 2""")
a = Account(100)
print(a.get_balance())
a.set_balance(350)
print(a.get_balance())
a.set_balance(-350)

a.balance = "asd"
print(a.get_balance())

# Information/data hiding
# Modyfikatory dostępu (access modifier)
# - atrybuty/pola publiczne
# - atrybuty/pola chronione - prefix nazwy: _
# - atrybuty/pola prywatne - prefi nazwy: __

class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter atrybutu balance
    def set_balance(self, value):
        if type(value) != int or value < 0:
            print("Podano niepoprawną wartość!")
        else:
            self.__balance = value

    # getter atrybutu balance
    def get_balance(self):
        return self.__balance

print("""=== Version 3 ===""")
a3 = Account(100)
print(a3.get_balance())
a3.set_balance(350)
print(a.get_balance())
a3.set_balance(-350)

a3.set_balance(a3.get_balance()+ 2*a3.get_balance()+2)

# property
class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter
    def set_balance(self, value):
        if type(value) != int or value < 0:
            print("Podano niepoprawną wartość!")
        else:
            self.__balance = value

    # getter
    def get_balance(self):
        return self.__balance

    balance = property(get_balance, set_balance)


print("""=== Version 4 ===""")
a4 = Account(100)
print(a4.balance)
a4.balance = 350
print(a4.balance)
a4.balance = -350

class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if type(value) != int or value < 0:
            print("Podano niepoprawną wartość!")
        else:
            self.__balance = value

print("""=== Version 5 ===""")
a4 = Account(100)
print(a4.balance)
a4.balance = 350
print(a4.balance)
a4.balance = -350
