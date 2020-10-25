from computer import Computer
from my_computer_builder import MyComputerBuilder
from cheap_computer_builder import CheapComputerBuilder
from director import Director


builder_1 = MyComputerBuilder()
d = Director(builder_1)
d.build_computer()
computer = d.get_computer()
computer.display()

builder_2 = CheapComputerBuilder()
d = Director(builder_2)
d.build_computer()
computer = d.get_computer()
computer.display()
