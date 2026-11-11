class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.current_bike = None

    def can_pay(self, amount):
        return self.balance >= amount

    def pay(self, amount):
        if not self.can_pay(amount):
            return False
        self.balance -= amount
        return True
