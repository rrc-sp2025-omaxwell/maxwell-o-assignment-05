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
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number


#import sys
#sys.path.append('') # Replace with actual path

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class chatbot(unittest.TestCase):
    def test_get_account_number_ValueError(self)->int:

        # Arrange
        user_input = 1111111111
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(ValueError) as context:
                get_account_number()

            # Assert
            expected = ValueError("Account number entered does not exist.")
            self.assertEqual(str(expected), str(context.exception))
        
    def test_get_account_number_TypeError(self)->int:

    # Arrange
        user_input = "abcdefg"
        with patch('builtins.input', return_value=user_input):
            
            # Act
            with self.assertRaises(TypeError) as context:
                get_account_number()

            # Assert
            expected = TypeError("Account number must be an int type.")
            self.assertEqual(str(expected), str(context.exception))

    def test_get_account_number_valid_account(self)->int:

        # Arrange
        user_input = 123456
        with patch('builtins.input', return_value=user_input):
            
            # Act
            actual = get_account_number()

            # Assert
            expected = 123456
            self.assertEqual(expected, actual)