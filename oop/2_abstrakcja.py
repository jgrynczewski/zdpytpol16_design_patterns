# Abstrakcja - redukowanie złożoności poprzez chowanie szczegółw w implementacji

class MailServer:
    def send_mail(self):
        self.__connect()
        self.__authenticate()
        self.__disconnect()

    def __connect(self):
        print("Connect")

    def __disconnect(self):
        print("Disconnect")

    def __authenticate(self):
        print("Authenitcate")

m = MailServer()
m.send_mail()