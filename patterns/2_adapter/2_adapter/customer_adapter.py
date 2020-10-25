from abs_adapter import AbsAdapter

class CustomerAdapter(AbsAdapter):

    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return self._adaptee.address
