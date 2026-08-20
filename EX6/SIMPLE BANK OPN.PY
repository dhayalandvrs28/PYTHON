class BankCustomer:
   def __init__(self,name,acc_number,initial_balance):
      self.name=name
      self.account=self.BankAccount(acc_number,initial_balance)
   def show_details(self):
      print("Customer: ",self.name)
      print("Account Number: ",self.account.acc_number)
      print("Balance: ",self.account.get_balance())
   class BankAccount:
      def __init__(self,acc_number,balance):
         self.acc_number=acc_number
         self.balance=balance
      def deposit(self,amount):
         if amount > 0:
            self.balance+=amount
            print("Deposited: ",amount)
         else:
            print("Invalid deposit amount")
      def withdraw(self,amount):
         if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdraw: ",amount)
         else:
            print("Insufficient balance or invalid amount")
      def get_balance(self):
         return self.balance
customer1=BankCustomer("Allan","ACC123",10000)
customer1.account.deposit(2000)
customer1.account.withdraw(1500)
