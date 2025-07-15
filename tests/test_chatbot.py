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
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number, get_amount, get_balance


#import sys
#sys.path.append('') # Replace with actual path

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

# default text string for testing
STRING_INPUT = "abcdefg"
# default incorrect number input
WRONG_NUM_INPUT = 1111111111

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

        user_input = 123456

        with patch('builtins.input', return_value=user_input):
            
            # Act
            actual = get_balance(user_input)
            # Assert
            expected = "Your current balance for account 123456 is $1,000.00."
            self.assertEqual(str(expected), str(actual))
    