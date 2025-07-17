"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number, get_amount, get_balance, make_deposit, get_task


#import sys
#sys.path.append('') # Replace with actual path

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

# default text string for testing
STRING_INPUT = str("abcdefg")
# default incorrect number input
WRONG_NUM_INPUT = int(1111111111)
# default valid input for testing
VALID_ACCOUNT_NUM = int(123456)

class chatbot(unittest.TestCase):

    # ValueError / WRONG NUMBER TESTING
    def test_get_account_number_ValueError(self)->int:

        # Arrange
        user_input = WRONG_NUM_INPUT
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_account_number()

            # Assert
            expected = ValueError("Account number entered does not exist.")
            self.assertEqual(str(expected), str(context.exception))

    # TypeError / NON NUMERIC TESTING    
    def test_get_account_number_TypeError(self)->int:

    # Arrange
        user_input = STRING_INPUT
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(TypeError) as context:
                get_account_number()

            # Assert
            expected = TypeError("Account number must be an int type.")
            self.assertEqual(str(expected), str(context.exception))

    # IS VALID ACCOUNT TESTING
    def test_get_account_number_valid_account(self)->int:

        # Arrange
        user_input = 123456
        with patch('builtins.input', return_value=user_input):
            
            # Act
            actual = get_account_number()

            # Assert
            expected = 123456
            self.assertEqual(expected, actual)


    # get_amount testing

    # NEGATIVE NUM VAL INPUT
    def test_get_amount_negative(self)->float:

    # Arrange
        user_input = -WRONG_NUM_INPUT
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            # Assert
            expected = ValueError("Amount must be a value greater than zero.")
            self.assertEqual(str(expected), str(context.exception))

    # NUM VAL ZERO INPUT
    def test_get_amount_zero(self)->float:

    # Arrange
        user_input = 0
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            # Assert
            expected = ValueError("Amount must be a value greater than zero.")
            self.assertEqual(str(expected), str(context.exception))
    

    # NON NUMERIC / STRING INPUT
    def test_get_amount_string(self)->float:

    # Arrange
        user_input = STRING_INPUT
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(TypeError) as context:
                get_amount()

            # Assert
            expected = TypeError("Amount must be a numeric type.")
            self.assertEqual(str(expected), str(context.exception))

    # get_balance testing

    # NON INT INPUT

    def test_get_balance_TypeError(self)->str:
        # Arrange

        account_num = STRING_INPUT

        with patch('builtins.input', return_value=account_num):
            
            # Act
            with self.assertRaises(TypeError) as context:
                get_balance(account_num)
            # Assert

            expected = TypeError("Account number must be an int type.")
            self.assertEqual(str(expected), str(context.exception))

    # INCORRECT VALUE INPUT
    def test_get_balance_ValueError(self)->str:
        # Arrange

        user_input = WRONG_NUM_INPUT

        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_balance(user_input)

            # Assert
            expected = ValueError("Account number entered does not exist.")
            self.assertEqual(str(expected), str(context.exception))

    # EXPECTED RESULTS TEST
    def test_get_balance_expected_result(self)->str:
        # Arrange

        user_input = VALID_ACCOUNT_NUM

        with patch('builtins.input', return_value=user_input):
            
            # Act
            actual = get_balance(user_input)
            # Assert
            expected = "Your current balance for account 123456 is $1,000.00."
            self.assertEqual(str(expected), str(actual))
    
    # make_deposit testing

    # testing for account_input TypeError ONLY

    def test_make_deposit_account_TypeError(self):
        # Arrange
        account_num = STRING_INPUT
        deposit_amount = None
        with patch('builtins.input', account_return_value=account_num, deposit_return_value = deposit_amount):
            
            # Act
            with self.assertRaises(TypeError) as context:
                make_deposit(account_num, deposit_amount)
            # Assert
            expected = TypeError("Account number must be an int type.")
            self.assertEqual(str(expected), str(context.exception))

    # Raises exception when account number not in dictionary

    def test_make_deposit_account_ValueError(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [WRONG_NUM_INPUT, None]
            
            # Act

            with self.assertRaises(ValueError) as context:
                make_deposit(WRONG_NUM_INPUT, None)
            # Assert
            expected = ValueError("Account number entered does not exist.")
            self.assertEqual(str(expected), str(context.exception))

    # Raise exception when amount entered is not numeric
    def test_make_deposit_amount_non_numeric(self):
        # Arrange

        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [VALID_ACCOUNT_NUM, STRING_INPUT]
            
            # Act

            with self.assertRaises(TypeError) as context:
                make_deposit(VALID_ACCOUNT_NUM, STRING_INPUT)

            # Assert
            expected = TypeError("Deposit amount must be a numeric type.")
            self.assertEqual(str(expected), str(context.exception))

    # Raise Exception when the amount entered is zero

    def test_make_deposit_amount_zero(self):
        # Arrange

        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [VALID_ACCOUNT_NUM, 0]
            
            # Act

            with self.assertRaises(ValueError) as context:
                make_deposit(VALID_ACCOUNT_NUM, 0)

            # Assert
            expected = ValueError("Deposit amount must be greater than zero.")
            self.assertEqual(str(expected), str(context.exception))

    # Raise Exception when the amount entered is negative

    def test_make_deposit_amount_negative(self):
        # Arrange

        with patch('builtins.input') as mock_input:
            mock_input.side_effect = [VALID_ACCOUNT_NUM, -1234]
            
            # Act

            with self.assertRaises(ValueError) as context:
                make_deposit(VALID_ACCOUNT_NUM, -1234)

            # Assert
            expected = ValueError("Deposit amount must be greater than zero.")
            self.assertEqual(str(expected), str(context.exception))

    # Function returns string as expected

    def test_make_deposit_valid(self):
        # Arrange

        with patch('builtins.input') as mock_input:
            account_num = VALID_ACCOUNT_NUM
            deposit_amount = 1234
            mock_input.side_effect = [account_num, deposit_amount]
            
            # Act

            actual = make_deposit(account_num, deposit_amount)
            # Assert
            expected = f"You have made a deposit of ${deposit_amount:,.2f} to account #{account_num}."
            self.assertEqual(expected, actual)

    # get_task testing

    # raise exception when task is invalid
    def test_get_task_invalid(self)->str:
        # arrange
        task_input = STRING_INPUT
        with patch('builtins.input', return_value = task_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_task()

            #assert
            expected = ValueError(f"{task_input} is an unknown task.")
            self.assertEqual(str(expected), str(context.exception))

    # Function returns valid task
    def test_get_task_valid_entry(self)->str:
        # arrange
        task_input = "deposit"
        with patch('builtins.input', return_value = task_input):
            
            # Act
            actual = get_task()

            #assert
            expected = "deposit"
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()