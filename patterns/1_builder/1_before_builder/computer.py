class Computer:

    def __init__(self, case, mainboard, cpu, memory, hard_disk):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_disk = hard_disk

    def display(self):
        print("Moj komputer:")
        print(f"Case: {self.case}")
        print(f"Mainboard: {self.mainboard}")
        print("...")
    