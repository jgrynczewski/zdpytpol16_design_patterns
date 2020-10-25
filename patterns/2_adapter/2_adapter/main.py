from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR

def main():
    for cust in MOCKVENDOR:
        print(f"Imię: {cust.name}, adres: {cust.address}")

if __name__ == "__main__":
    main()
