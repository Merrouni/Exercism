STATUS_CLOSED = 'closed'
STATUS_OPEN = 'open'

class BankAccount(object):
    def __init__(self):
        self.status = STATUS_CLOSED
        self.transactions = []
        pass

    def get_balance(self):
        if self.status == STATUS_CLOSED:
            raise ValueError("The account is closed !!!")
        return sum(self.transactions)

    def open(self):
        if self.status == STATUS_OPEN:
            raise ValueError("Account already open !!!")
        self.status = STATUS_OPEN
        self.transactions.append(0)

    def deposit(self, amount):
        if self.status == STATUS_CLOSED:
            raise ValueError("The account is closed !!!")
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative !!!")
        self.transactions.append(amount)

    def withdraw(self, amount):
        if self.status == STATUS_CLOSED:
            raise ValueError("The account is closed !!!")
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negative !!!")
        if sum(self.transactions) - amount < 0:
            raise ValueError("You can't withdraw more than diposited !!!")
        self.transactions.append(-amount)

    def close(self):
        if self.status == STATUS_CLOSED:
            raise ValueError("Account already closed !!!")
        self.status = STATUS_CLOSED
        self.transactions = []
