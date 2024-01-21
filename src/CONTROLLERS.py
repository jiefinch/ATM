def world_controller(string = None):
    action = input("where would you like to go? (bank/atm/home) ")
    if action.lower() == "bank":
        bank_controller()
    
    elif action.lower() == "atm":
        atm_controller()
        
    elif action.lower() == "home":
        print("Good night.")
        
    else:
        print("I have no idea what you just said.\n")
        world_controller()
        

def bank_controller():
    print("you're at the bank")

def atm_controller():
    print("you're at the ATM")


