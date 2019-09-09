import abc

class BankUnion(abc.ABC):
    @abc.abstractmethod
    def saving_acct():
        pass

    @abc.abstractmethod
    def loan_acct():
        pass    