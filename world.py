# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
from src.BANK import *
from src.ATM import *
from src.CONTROLLERS import *

WooriBank = Bank()
WooriATM = ATM(WooriBank)

world_controller()