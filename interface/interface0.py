import abc

class MyABC(abc.ABC):

    @abc.abstractmethod
    def do_something(self, value):
        pass

    @property
    @abc.abstractmethod
    def some_property(self):
        """Required property"""

class MyClass(MyABC):
    def __init__(self, value=None):
        self._my_propoperty = value

    def do_something(self, value):
        self._my_propoperty + value

    @property
    def some_property(self):
        return self._my_propoperty


class BadClass(MyABC):
    pass

my_class = MyClass()
bad_class = BadClass()