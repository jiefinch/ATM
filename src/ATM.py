class ATM():
    def __init__(self, Bank):
        self.Bank = Bank
    
    def insert_card(self, cardID):
        if cardID in self.Bank.activeCards:
            card = self.bank.activeCards[cardID]
            
            
            pin = input("Please type in your Pin to view account.")
            if pin == card.pin:
                return card.account.customer
            else:
                print("Error. Invalid pin.")
            
        else:
            print("Invalid Card. Try again.")



