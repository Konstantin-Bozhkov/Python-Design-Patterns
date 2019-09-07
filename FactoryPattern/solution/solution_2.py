import abc

# Product
class Bank(abc.ABC):
    def __init__(self):
        self.balance = 0
    
    @abc.abstractmethod
    def get_balance(self):
        pass

# Concrete Product
class CityBank(Bank):
    def __init__(self):
        self.balance = 1000

    def get_balance(self):
        return self.balance


# Concrete Product
class NationalBank(Bank):
    def __init__(self):
        self.balance = 2000
        
    def get_balance(self):
        return self.balance


# Concrete Creator
class BankFactory:
    def get_bank(self, acct_num):
        if 'CITI' in acct_num:
            return CityBank()
        elif 'NATIONAL' in acct_num:
            return NationalBank()
        else:
            return ValueError(acct_num)


factory = BankFactory()
citi = factory.get_bank('CITI-321')
national = factory.get_bank('NATIONAL-987')

print(citi.get_balance())
print(national.get_balance())