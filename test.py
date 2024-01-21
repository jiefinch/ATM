import unittest
from unittest.mock import patch
from src.BANK import *
from src.CONTROLLERS import *
WooriBank = Bank()

"""
Things to test (FUNCTIONALITY)
1. go to bank
2. new customer
3. open account
4. set pin
5. return back to world
6. go to atm
7. insert card into atm
8. view balance
9. deposit 10
10. withdraw 10
11. go home
"""

class Tests(unittest.TestCase):

    @patch('builtins.input', return_value='hello')
    def test_process_input(self, mock_input):
        result = process_input()
        self.assertEqual(result, 'HELLO')

if __name__ == '__main__':
    unittest.main()
result, 'HELLO')
