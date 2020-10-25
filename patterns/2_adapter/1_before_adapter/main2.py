from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR
TYPE = 'vendors'


def main():
    if TYPE == "vendors":
        for ven in MOCKVENDOR:
            print(f"Imię: {ven.name}, adres: {ven.street} {ven.number}")
    elif TYPE == "customers":
        for cust in MOCKCUSTOMER:
            print(f"Imię: {cust.name}, adres: {cust.address}")

if __name__ == "__main__":
    main()
