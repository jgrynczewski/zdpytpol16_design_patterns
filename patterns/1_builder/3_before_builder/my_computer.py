from computer import Computer

class MyComputer:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = "Collmaster"
        computer.mainboard = "MSI 970"
        computer.cpu = "Intel"
        computer.memory = "16GB"
        computer.hard_disk = 'Seagate 2GB'
