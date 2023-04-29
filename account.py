class Account:
    def __init__(self, name: str) -> None:
        '''set default values for account object'''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float)-> bool:
        '''deposit  by the specified amount'''
        if amount <=0:
            return False
        else:
            self.__account_balance += amount
            return True
    def withdraw(self, amount: float)-> bool:
        '''withdraw by the specified amount'''

        if amount <=0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''return balance'''
        return self.__account_balance

    def get_name(self) -> str:
        '''return the account name'''
        return self.__account_name


