from mock_customer import MOCKCUSTOMER

def main():
    for cust in MOCKCUSTOMER:
        print(f"Imię: {cust.name}, adres: {cust.address}")

if __name__ == "__main__":
    main()
