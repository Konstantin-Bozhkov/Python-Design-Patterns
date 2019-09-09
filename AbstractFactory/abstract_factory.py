# from interfaces import bank_union
from banks.citi_bank import CitiBank
from banks.national_bank import NationalBank

class BankUnionFactory:    
    def __init__(self, bank):
        self.bank = bank

    def show_bank_details(self):
        saving_acct = self.bank.saving_acct()
        loan_acct = self.bank.loan_acct()


citi = CitiBank()
national = NationalBank()

factory_1 = BankUnionFactory(citi)
factory_2 = BankUnionFactory(national)

factory_1.show_bank_details()
factory_2.show_bank_details()