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
    """Returns account numbers found in the ACCOUNTS dict.

    args:
    input (int): a user input to be compared to ACCOUNTS.

    returns:
        int: returns valid account numbers as an integer.
    """

    account_number = input("Enter account number: ")
    if type(account_number) != int:
        raise TypeError("Account number must be an int type.")
            
    if account_number in ACCOUNTS:
        return account_number 
    else:
        raise ValueError("Account number entered does not exist.")

def get_amount()->float:
    """Returns deposit amount as float when value above zero.
   
    args:
    input(int or float): user inout that must be above zero.

    returns:
        float: deposit amount as float.
    """
    # Accepts any data type as input, verifies type in next step
    deposit_amount = input("Enter an amount:")
    
    # raises TypeError ONLY if type is str
    if type(deposit_amount) == str:
        raise TypeError("Amount must be a numeric type.")
    
    # raises ValueError if less than or equal to zero.
    elif deposit_amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    else:
        return deposit_amount
    
def get_balance(account_num: int) -> str:
    """
    Returns a balance statement as a string containing
    account number and balance in a currency format.

    Args:
        integer: account number / key to access ACCOUNTS dictionary

    returns:
        string: a string containing the balance of the input account
    """
    account_num = input("Please input an account number: ")

    if type(account_num) != int:
        raise TypeError("Account number must be an int type.")
    
    elif account_num not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    else:
        balance = ACCOUNTS[account_num]["balance"]
        balance_formatted = f"${balance:,.2f}"
        return f"Your current balance for account {account_num} is {balance_formatted}."

def make_deposit(account_num: int, deposit_amount: int) -> str:
    """Returns a string containing an account number and amount deposited.

    args:
        account_num (int): the number of the account.
        deposit_amount (int or float): the number being deposited.

    returns:
        A string containing an account number and amount deposited.
    
    """
    account_num = input("Please input an account number: ")
    deposit_amount = input("Please input an deposit amount: ")
    

    if type(account_num) != int:
        raise TypeError("Account number must be an int type.")
    
    elif account_num not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    elif type(deposit_amount) == str:
        raise TypeError("Deposit amount must be a numeric type.")
    
    elif deposit_amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")
    else:
        deposit_formatted = f"${deposit_amount:,.2f}"
    
    return f"You have made a deposit of {deposit_formatted} to account #{account_num}."

def get_task():
    """Returns a string containing the desired task .


    Args:
        user input (str), 1 of 3 valid tasks , balance, deposit, and exit,

    exceptions:
        ValueError, When task input is not in VALID_TASKS dictionary.

    returns:
        a string containing the desired task 

    """
    task = input("What would you like to do (balance/deposit/exit)?: ")

    if task not in VALID_TASKS:
        raise ValueError(f"{task} is an unknown task.")


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

