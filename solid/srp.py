# Single Responsible Principle (Zasada jednej odpowiedzialności)
# S w SOLID
# Klasa powinna mieć swoją własną odpowiedzialności i nie powinna brać
# odpowiedzialności innych klas.
# Klasa powinna mieć jeden i tylko jeden powód do zmiany.

# SoC - Separation of Concern

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

j = Journal()
j.add_entry("Wstałem")
j.add_entry("Połyżem się")

# Łamiemy SRP
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    def load(self):
        pass

    def load_from_web(self, uri):
        pass

# Antywzorzec - God Object

# Refaktoryzacja
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

class PeristanceManager:
    @staticmethod
    def save_to_file(jurnal, filename):
        with open(filename, 'w') as f:
            f.write(str(jurnal))

j = Journal()
j.add_entry("Dzień dobry")
j.add_entry("Witam")
print(j)

file = r"journal.txt"

PeristanceManager.save_to_file(j, file)

