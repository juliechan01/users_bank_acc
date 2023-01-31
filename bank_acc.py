class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {'checking':BankAccount(int_rate = 0.04, bal = 0), 'savings':BankAccount(int_rate = 0.09, bal = 0)}

    # other methods
    def make_deposit(self):
        dep = input("What account would you like to deposit into?\nChecking\nSavings\n")
        self.account[dep].deposit()
        return self

    def make_withdrawal(self):
        draw = input("Which account would you like to withdraw from?\nChecking\nSavings\n")
        self.account[draw].withdraw()
        return self

    def display_user_bal(self):
        info = input("Which account's balance would you like to see?\nChecking\nSavings\n")
        self.account[info].display_account_info()
        return self

    def make_transfer(self, other_user):
        self.account['checking'].transfer_money(other_user)

class BankAccount:
    bank_name = "JP Morgan Chase"
    all_acc = [] # class attribute - list of all accounts; need to find out how to print this!
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, bal): 
        self.int_rate = int_rate
        self.bal = bal
        BankAccount.all_acc.append(self)

    def deposit(self):
        amount = input("How much would you like to deposit today?\n")
        amount = int(amount)
        self.bal = self.bal + amount
        print(f"You now have a balance of ${self.bal}")
        return self

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
        m = input(f"Welcome to {BankAccount.bank_name}. What would you like to do today?\n Deposit\n Withdraw\n Transfer\n")
        if m == "deposit":
            self.deposit()
        elif m == "withdraw":
            self.withdraw()
        elif m == "transfer":
            self.transfer_money(other_user)
        else:
            print("Thank you for banking with us. Have a nice day!")

    def yield_interest(self):
        self.bal = (self.bal * self.int_rate) + self.bal
        print(f"Current balance w/ interest accrued: ${self.bal}")

    def change_bank(cls, name):
        cls.bank_name = name

    def transfer_money(self, other_user):
        amount = input(f"How much money would you like to transfer to {other_user.name}?\n")
        amount = int(amount)
        confirm = input(f"You would like to transfer ${amount} to {other_user.name}. Do you confirm? Y or N\n")
        if confirm == "y":
            self.bal = self.bal - amount
            BankAccount.all_acc[1].bal = self.bal + amount #fix this
            print(f"{self.name} has sent you ${amount} and it's ready now.")
        else:
            ask = input("Would you like to do anything else?\n Deposit\n Withdraw\n Transfer\n")
            if ask == "deposit":
                self.deposit()
            elif ask == "withdraw":
                self.withdraw()
            elif ask == "transfer":
                self.transfer_money(other_user)
            else:
                print("Thank you for banking with us. Have a nice day!")

user1 = User("Julie Chan", "juliechan03@gmail.com")
user2 = User("Annie Tu", "annietu4@gmail.com")
user1.make_deposit()
user1.make_transfer(user2)