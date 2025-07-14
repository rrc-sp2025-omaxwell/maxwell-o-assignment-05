"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"


ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number()->int:
    # Account num input validation
    """
    Returns account numbers found in the ACCOUNTS dict.

    args:
    input (int): a user input to be compared to ACCOUNTS
    """

    account_number = input("Enter account number: ")
    if type(account_number) != int:
        raise TypeError("Account number must be an int type.")
            
    if account_number in ACCOUNTS:
        return account_number 
    else:
        raise ValueError("Account number entered does not exist.")

def get_amount()->float:
    deposit_amount = input("Enter an amount:")
    if type(deposit_amount) != int or float:
        raise TypeError("Amount must be a numeric type.")
    
    elif deposit_amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    else:
        return deposit_amount

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()

