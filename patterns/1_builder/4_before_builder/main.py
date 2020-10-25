from computer import Computer
from my_computer_builder import MyComputerBuilder
from cheap_computer_builder import CheapComputerBuilder

builder = MyComputerBuilder()
builder.build_computer()
computer = builder.get_computer()
computer.display()

builder = CheapComputerBuilder()
builder.build_computer()
computer = builder.get_computer()
computer.display()
