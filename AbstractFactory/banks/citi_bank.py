from interfaces.bank_union import BankUnion

class CitiSavingAcc():
    def __init__(self):
        print("Citi saving account")

class CitiLoanAcct():
    def __init__(self):
        print("Citi loan account")


class CitiBank(BankUnion):
    
    def saving_acct(self):
        return CitiSavingAcc()

    def loan_acct(self):
        return CitiLoanAcct()