from abs_computer_builder import AbsComputerBuilder

class Director:
    def __init__(self, builder: AbsComputerBuilder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.get_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()

    def get_computer(self):
        return self._builder.get_computer()
