class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        BankAccount.all_acc.append(User)

    # other methods
    def make_deposit(self, amount):
        BankAccount.deposit()

    def make_withdrawal(self, amount):
        BankAccount.withdraw()

    def display_user_bal():
        print(f"Your current balance is ${BankAccount.bal}.")

class BankAccount:
    bank_name = "JP Morgan Chase"
    all_acc = [] # class attribute - list of all accounts; need to find out how to print this!
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, bal): 
        self.int_rate = int_rate
        self.bal = bal

    def deposit(self):
        amount = input("How much would you like to deposit today?\n")
        amount = int(amount)
        self.bal = self.bal + amount
        print(f"You now have a balance of ${self.bal}")

    def withdraw(self):
        amount = input("How much would you like to withdraw today?\n")
        amount = int(amount)
        if amount <= self.bal:
            self.bal = self.bal - amount
            print(f"You now have a balance of ${self.bal}")
        else:
            c = input("You have insufficient funds. To continue withdrawing, we will charge you a fee of $5. Please confirm if you would like to continue. Y or N\n")
            if c == "y":
                self.bal = self.bal - amount - 5
                print(f"You now have a balance of ${self.bal}")
            else:
                c = input("Please enter an amount you would like to withdraw:\n")
                c = int(c)
                self.bal = self.bal - c
                print(f"You now have a balance of ${self.bal}")

    def display_account_info(self):
        print(f"Balance: ${self.bal}")
        m = input(f"Welcome to {BankAccount.bank_name}. What would you like to do today?\n Deposit\n Withdraw\nTransfer\n")
        if m == "deposit":
            self.deposit()
        elif m == "withdraw":
            self.withdraw()
        elif m == "transfer":
            self.transfer_money()
        else:
            print("Thank you for banking with us. Have a nice day!")

    def yield_interest(self):
        self.bal = (self.bal * self.int_rate) + self.bal
        print(f"Current balance w/ interest accrued: ${self.bal}")

    def change_bank(cls, name):
        cls.bank_name = name

    def transfer_money(self, amount, other_user):
        other_user = input("Who would you like to transfer?\n")
        amount = input("How much money would you like to transfer to them?\n")
        confirm = input(f"You would like to transfer ${amount} to {other_user}. Do you confirm? Y or N\n")
        if confirm == "y":
            self.bal = self.bal - amount
            BankAccount.all_acc[1].bal = self.bal + amount #fix this
            print(f"{User} has sent you ${amount} and it's ready now.")
        else:
            ask = input("Would you like to do anything else? Deposit\n Withdraw\n Transfer\n")
            if ask == "deposit":
                self.deposit()
            elif ask == "withdraw":
                self.withdraw()
            elif ask == "transfer":
                self.transfer_money()
            else:
                print("Thank you for banking with us. Have a nice day!")

User("Julie Chan", "juliechan03@gmail.com") = (0.04, 10000)
User("Andrew Fowler", "drewtotha@gmail.com") = (0.04, 10000)
BankAccount.all_acc()