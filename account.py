class Account:
    def __init__(self, name, balance):
        '''set default values for account object'''
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount: float)-> float:
        if amount <=0:
            return False
        else:
            self.__account_balance += amount
            return True
    def withdraw(self, amount: float)-> float:

        if amount <=0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name


