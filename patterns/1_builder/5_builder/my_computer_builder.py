from abs_computer_builder import AbsComputerBuilder
from computer import Computer

class MyComputerBuilder(AbsComputerBuilder):

    def get_case(self):
        self._computer.case = "Collmaster"

    def get_mainboard(self):
        self._computer.mainboard = "MSI 970"
        self._computer.cpu = "Intel"
        self._computer.memory = "16GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_disk = 'Seagate 2GB'
