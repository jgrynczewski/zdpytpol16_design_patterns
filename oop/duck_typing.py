# If it looks like a duck, swims like a duck and quacks like a duck, then it probably is a duck.

import abc
class SwimDuckAnimal(abc.ABC):
    @abc.abstractmethod
    def swim_quack(self):
        pass

class Duck(SwimDuckAnimal):
    def swim_quack(self):
        print("Jestem kaczką")

class Dog(SwimDuckAnimal):
    def swim_quack(self):
        print("Jestem psem")

class Fish(SwimDuckAnimal):
    def swim(self):
        print("Jestem rybą")

def duck_testing(animal: SwimDuckAnimal):
    animal.swim_quack()

duck_testing(Duck())
duck_testing(Dog())
duck_testing(Fish())