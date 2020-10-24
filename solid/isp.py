# ISP - Intrface Segregation Principle (Zasada rozdzielenia interfejsów)

# Łamiemy ISP
class Machine:
    def print_doc(self, document):
        raise NotImplementedError

    def fax_doc(self, document):
        raise NotImplementedError

    def scan_doc(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print_doc(self, document):
        print("Drukuję")

    def fax_doc(self, document):
        print("Faksuję")

    def scan_doc(self, document):
        print("Skanuję")


class OldFashionedPrinter(Machine):
    def print_doc(self, document):
        print("Drukuję")

    def fax_doc(self, document):
        raise NotImplementedError("Drukarka nie wysyła faksu")

    def scan_doc(self, document):
        raise NotImplementedError("Drukarka nie skanuje")

ofp = OldFashionedPrinter()
ofp.fax_doc("asd")

class Printer:
    def print_doc(self, document):
        pass

class Scanner:
    def scan_doc(self, document):
        pass

class Fax:
    def fax_doc(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def print_doc(self, document):
        print("Drukuję")
    def scan_doc(self, document):
        print("Skanuję")

class MultiFunctionDevice(Printer, Scanner, Fax):
    def print_doc(self, document):
        print("Drukuję")
    def scan_doc(self, document):
        print("Skanuję")
    def fax_doc(self, document):
        print("Wysyłam faks")


class OldFashionPrinter(Printer):
    def print_doc(self, document):
        print("Drukuję")
