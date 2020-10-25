from abs_adapter import AbsAdapter

class VendorAdapter(AbsAdapter):

    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return f"{self._adaptee.street} {self._adaptee.number}"
