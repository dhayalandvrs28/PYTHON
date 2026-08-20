class MinimumBalanceError(Exception):
    def __init__(self):
        self.msg = "Minimum Balance Rs.500 could not be maintained with the withdrawal."

class InsufficientAmountError(Exception):
    def __init__(self):
        self.msg = "Insufficient Balance! Entered amount is more than that of the balance."

class NegativeError(Exception):
    def __init__(self):
        self.msg = "Negative value of amount is invalid!"

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance

    def deposit(self, da):
       if da<0:
          raise NegativeError()
       else:
          self.bal += da
          print("\nRs.", da, "is deposited to the account.\nYour current balance is:", self.bal, '\n')

    def withdraw(self, wa):
        if wa < 0:
            raise NegativeError()
        if self.bal < wa:
            raise InsufficientAmountError()
        else:
            if self.bal - wa < 500:
                raise MinimumBalanceError()
            else:
                self.bal -= wa
                print("Rs.", wa, "is withdrawn successfully.\nYour current balance is:", self.bal, '\n')

    def balance(self):
        print("Your Current Balance is", self.bal)

name = input("Enter account holder name: ")
balance = int(input("Enter the initial deposit for the account: "))

try:
    user = Bank(name, balance)
    print("\nBanking system Initialized!\n")
    print("\n1. Check balance\n2. Deposit amount into the account.\n3. Withdraw cash from the account.\n4. Exit\n")

    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            user.balance()
        elif ch == 2:
            user.deposit(int(input("Enter the amount for deposit: ")))
        elif ch == 3:
            wa = int(input("Enter the amount to be withdrawn: "))
            user.withdraw(wa)
        elif ch == 4:
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice. Please try again.")
except (InsufficientAmountError, MinimumBalanceError, NegativeError) as e:
    print(e.msg)
except ValueError:
    print("Invalid input! Please enter a valid number.")
