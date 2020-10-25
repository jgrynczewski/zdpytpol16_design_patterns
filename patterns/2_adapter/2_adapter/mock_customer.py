from customer import Customer
from customer_adapter import CustomerAdapter

MOCKCUSTOMER = (
    CustomerAdapter(Customer("Tom", "Liljowa 32")),
    CustomerAdapter(Customer("John", "Konwaliowa 12")),
    CustomerAdapter(Customer("James", "Truskawkowa 22"))
)