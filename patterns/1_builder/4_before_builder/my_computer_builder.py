from computer import Computer

class MyComputerBuilder:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        self._computer = Computer()
        self.get_case()
        self.get_mainboard()
        self.install_mainboard()
        self.install_hard_drive()

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
