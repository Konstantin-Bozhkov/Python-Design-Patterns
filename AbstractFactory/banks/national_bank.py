
from interfaces.bank_union import BankUnion


class NationalSavingAcc():
    def __init__(self):
        print("National saving account")

class NationalLoanAcct():
    def __init__(self):
        print("National loan account")


class NationalBank(BankUnion):

    def saving_acct(self):
        return NationalSavingAcc()

    def loan_acct(self):
        return NationalLoanAcct()