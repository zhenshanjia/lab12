from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1
    def test_init(self):
        assert self.a1.get_name() == "John"

    def test_deposit(self):
        assert self.a1.deposit(-5) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(2.5) is True
        assert self.a1.get_balance() == approx(2.5,abs = 0.001)


    def test_withdraw(self):
        assert self.a1.withdraw(5) is False
        assert self.a1.get_balance() == 0
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0
        self.a1.deposit(10)
        assert self.a1.withdraw(2.5) is True
        assert self.a1.get_balance() == approx(7.5,abs = 0.001)



