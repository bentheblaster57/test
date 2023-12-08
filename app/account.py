class InsufficientAmount(Exception):
    pass


class Account:
    def __innit__(self, innitial_amount):
        self.balance = innitial_amount

    
    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount("not enough para yo")
        
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount