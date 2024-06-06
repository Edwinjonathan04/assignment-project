
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print("Insufficient funds!")
            return False

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <= 700000:
            super().deposit(amount)
            self._balance *= 1.005  # 0.5% interest
        else:
            print("Deposit limit exceeded for Savings Account!")


class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)


class childrensAccount(Account):
   def--init--(self, balance=0):
  super()._ _init_ _(balance)

def deposit(self,):
    super().deposit(amount)
    self._balance*=1.007  # 0.7% interest

    def withdrawalnot allowed for chlidren's account!")



class student(Account):
    def_ _inti_ _(self, balance=0):
    super()._ _init_ _(balance)

