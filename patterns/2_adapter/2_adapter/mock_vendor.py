from vendor import Vendor
from vendor_adapter import VendorAdapter

MOCKVENDOR = (
    VendorAdapter(Vendor("Alice", 22, "Liljowa")),
    VendorAdapter(Vendor("Eva", 30, "Konwaliowa")),
    VendorAdapter(Vendor("Anna", 4, "Truskawkowa"))
)