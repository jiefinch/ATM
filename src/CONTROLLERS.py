def world_controller(bank):
    action = input("Where would you like to go? (bank/atm/home) ")
    if action.lower() == "bank":
        bank_controller(bank)
    
    elif action.lower() == "atm":
        atm_controller(bank)
        
    elif action.lower() == "home":
        print("Good night.")
        
    else:
        print("I have no idea what you just said.\n")
        world_controller()
        

def bank_controller(bank):
    print("You're at the bank\n")
    bank.enact()

def atm_controller(bank):
    print("you're at the ATM\n")
    bank.ATM.enact()

