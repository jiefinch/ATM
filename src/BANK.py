import random
# acc can be in integers

class Bank:
    def __init__(self):
        self.customers = {}
        self.activeCards = {} # cardID: card
        
    def new_customer(self):
        name = input("What is your name?")
        print(f"Registering {name} with our bank.")
        customer = Customer(self, name)
        self.customers[name] = customer
        
    
class Customer:
    def __init__(self, Bank, name):
        self.Bank = Bank
        self.name = name
        self.accounts = {}
        
        print("Would you like to open an account")
    
    def open_account(self, name, balance = 0):
        # name: name of account
        # balance: starting balance
                
        self.accounts[name] = Account(name, balance)
    
    def close_account(self, name):
        if name not in self.accounts.keys():
            print(f"Failed to close accounts. Account {name} does not exist")
            print(f"Here are your accounts: {self.accounts.keys()}")
        else:
            response = input(f"Are you sure you want to close account {name}? (Y/N)")
            if response.capitalize() == 'Y':
                account = self.accounts.pop(name)
                self.bank.activeCards.pop(account.card.ID) # deactivate card in bank registry
                money = account.balance
                
                print(f"You have succesfully closed account. Returning ${money}")
                return money

class Account:
    def __init__(self, customer, name, balance = 0):
        self.customer = customer
        self.name = name
        self.balance = balance
        self.card = self.create_card()
        
    def create_card(self):
        NoPin = True
        while NoPin:
            pin = input("Please set your pin.")
            confirm = input("Please re-confirm your pin.")
            
            if pin == confirm:
                NoPin = False
            else:
                print("Failed to set pin. Inputs were not the same.")
        return Card(pin)
        
    def see_balance(self):
        # no security problem, int type is unmutable / readonly 
        return self.balance 
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Overdrafting error. You only have {self.balance}")
            # for added realism. lol.
            self.balance -= 1
            print(f"Applying overdraft fee of $1. You now have {self.balance}")
            # for added realism, doesnt check if this will put you into debt ^_
        
        else:
            self.balance -= amount
            
            print(f"Succesfully withdrew ${amount}")
            return amount
        
class Card:
    def __init__(self, account, pin):
        self.account = account
        ID = None
        while ID in self.account.customer.bank.activeCards:
            ID = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        self.ID = ID
        self.pin = pin
        
        print(f"Card {ID} for account {self.account.name} has been sent to your address. Please do not lose your card...")
        print(f"CARD: {ID}")
        self.account.customer.bank.activeCards[ID] = self