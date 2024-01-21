# Due to difficulties with handling user input, here is the manual testing test cases.
# Sorry, i usally like to do automated unit testing ):
# to achieve this i would need to think of a way to stop the flow of inputs so i can chunk the methods individually

"""
Things to test (BASIC FUNCTIONALITY)
go to bank
new customer: boo
open account: check, 9 -> error
open account: check, 150
set pin: 123
return back to world
go to atm
insert card into atm
wrong pin
right pin
deposit 10 -> 160
check balance -> 160
withdraw 15 -> 145
check balance -> 145
overdraft (fee): 200 -> 144
go back to bank
return customer: boo
close account: check
new customer: fred
open account: check, 20
open account: save, 30
go to atm
insert card (boo, check) into atm -> error
insert card (fred, save) into atm
check balance: 30
insert card (fred, check) into atm
check balance: 20
go home
"""
