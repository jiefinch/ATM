import random
from src.CONTROLLERS import *
# from src.ATM import ATM
# acc can be in integers
# for simplicity, there will only be 1 ATM for the bank in this world
# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw


# helper class
def enact_template(hello_str, actions, bank):
    print(f"{hello_str}: {list(actions.keys())}")
    action = input("\nWhat would you like to do? ")
    
    if action in actions:
        func = actions[action]
        if action == 'return':
            func(bank) # moves back to world controller
        else:
            func()
    else:
        enact_template(hello_str, actions, bank)

class Bank:
    def __init__(self):
        self.customers = {}
        self.ATM = ATM(self)
        self.activeCards = {} # cardID: card
        self.actions = {'new customer': self.new_customer,
                'returning customer': self.returning_customer,
                'return': world_controller}

    def new_customer(self):
        name = input("\nWhat is your name? ")
        if name in self.customers:
            print("You already exist...")
            self.enact()
        else:
            print(f"Registering {name} with our bank.")
            customer = Customer(self, name)
            self.customers[name] = customer
            customer.enact()
        
    def returning_customer(self):
        name = input("\nWhat is your name? ")
        if name in self.customers:
            print(f"Welcome {name}.")
            customer = self.customers[name]
            customer.enact()
        else:
            print("Cannot find ya. Consider registering.")
            bank_controller(self)
            
    def get_card(self, cardID):
        if cardID in self.activeCards:
            return self.activeCards[cardID]
        else:
            print("Card does not exist.")
            return None
            
    def check_pin(self, card, pin):
        return card.pin == pin
    
    def enact(self):
        hello_str = "Here's what you can do at the bank"
        enact_template(hello_str, self.actions, self)
        
    
class Customer:
    def __init__(self, bank, name):
        self.bank = bank
        self.name = name
        self.accounts = {}
        self.actions = {'open account': self.open_account,
                'close account': self.close_account,
                'go back': self.bank.enact}
    
    def open_account(self):
        name = input("\nWhat is the name of this account? ")
        balance = input("\nHow much would you like to deposit into this account? (Min deposit is $10) ")
        balance = int(balance)
        
        if balance < 10:
            print("Not enough money. Come back when you're richer.")
        elif name in self.accounts:
            print("You already have an account with this name.")
        else:
            self.accounts[name] = Account(self, name, balance)
            print(f"Succesfully opened bank account {name} with ${balance}")
            
        self.enact()
        
    
    def close_account(self):
        print(f"Your accounts: {list(self.accounts.keys())}")
        name = input("\nWhat is the name of the account you would like to close? ")
        
        if name not in self.accounts.keys():
            print(f"Failed to close accounts. Account {name} does not exist")
        else:
            response = input(f"Are you sure you want to close account {name}? (Y/N) ")
            if response.upper() == 'Y':
                account = self.accounts.pop(name)
                self.bank.activeCards.pop(account.card.ID) # deactivate card in bank registry
                money = account.balance
                print(f"You have succesfully closed account. Returning ${money}.")

        self.enact()
        
    def enact(self):
        hello_str = "Here's what you can do as a customer"
        enact_template(hello_str, self.actions, self)
        
class Account:
    def __init__(self, customer, name, balance = 0):
        self.customer = customer
        self.name = name
        self.balance = balance
        self.card = self.new_card()
        
    def new_card(self):
        NoPin = True
        while NoPin:
            pin = input("\nPlease set your pin: ")
            confirm = input("\nPlease re-confirm your pin: ")
            
            if pin == confirm:
                NoPin = False
            else:
                print("Failed to set pin. Inputs were not the same.")
        return Card(self, pin)
        
      
        
class Card:
    def __init__(self, account, pin):
        self.account = account
        
        ID = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        while ID in self.account.customer.bank.activeCards:
            ID = ''.join([str(random.randint(0, 9)) for _ in range(10)])
 
        self.ID = ID
        self.pin = pin
        
        print(f"Card {self.ID} for account {self.account.name} has been sent to your address. Please do not lose your card...")
        print(f"CARD: {self.ID}")
        self.account.customer.bank.activeCards[self.ID] = self
        
        
        
# -----------------------------------------

class ATM():
    def __init__(self, bank):
        self.bank = bank
        self.actions = {'insert card': self.insert_card,
                'return': world_controller}

    def insert_card(self):
        cardID = input("\nPlease insert your card: ") 
        
        card = self.bank.get_card(cardID)
        if card:
            pin = input("\nPlease type in your Pin to view account: ")
            if self.bank.check_pin(card, pin):
                customer = card.account.customer
                print(f"Welcome back, {customer.name}.")
                valid_session = InternalATM(self, customer)
                valid_session.select_account()
            else:
                print("Error. Invalid pin.")
                self.enact()
        else:
            self.enact()

    def enact(self):
        hello_str = "Here's what you can do at the ATM"
        enact_template(hello_str, self.actions, self.bank)


class InternalATM():
    def __init__(self, ATM, customer):
        self.ATM = ATM
        self.customer = customer
        self.account = None
        self.actions = {'see balance': self.see_balance,
                    'deposit': self.deposit,
                    'withdraw': self.withdraw,
                    'return': atm_controller}
        
    def select_account(self):
        print(f"Accounts: {list(self.customer.accounts.keys())}")
        account = input("\nWhich account would you like to select? ")
        self.account = self.customer.accounts[account]
        self.enact()
    
    def see_balance(self):
        print(f"You have ${self.account.balance} in account {self.account.name}.")
        self.enact()
    
    def deposit(self):
        amount = input("\nHow much would you like to deposit?: ")
        amount = int(amount)
        
        self.account.balance += amount
        print(f"Succesfully deposited ${amount}.")
        print(f"You now have ${self.account.balance} in account {self.account.name}.")
        self.enact()
    
    def withdraw(self):   
        amount = input("\nHow much would you like to withdraw?: ")
        amount = int(amount)
        
        if self.account.balance < amount:
            print(f"Failed transaction. You only have ${self.account.balance}.")
            # for added realism. lol.
            self.account.balance -= 1
            print(f"Applying overdraft fee of $1. You now have ${self.account.balance}.")
            # for added realism, doesnt check if this will put you into debt ^_^
        
        else:
            self.account.balance -= amount
            
            print(f"Succesfully withdrew ${amount}.")
            
        print(f"You now have ${self.account.balance} in account {self.account.name}.")
        self.enact()
        
    def enact(self):
        hello_str = "Here's what you can do with your account"
        enact_template(hello_str, self.actions, self.ATM.bank)
        