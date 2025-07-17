"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

import time
import os

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
    try:
        account_number = int(input("Enter account number: "))

        if account_number in ACCOUNTS:
            return account_number
        else:
            raise ValueError("Account number entered does not exist.")


    except ValueError:
        return "Account number must be an int type."

def get_amount()->float:
    """Returns deposit amount as float when value above zero.
   
    args:
    input(int or float): user input that must be above zero.

    returns:
        float: deposit amount as float.
    """
    # Accepts any data type as input, verifies type in next step
    try:
        deposit_amount = int(input("Enter an amount:"))
    
    # raises TypeError ONLY if type is str

            
        
        # raises ValueError if less than or equal to zero.
        if deposit_amount <= 0:
            raise ValueError("Amount must be a value greater than zero.")
        
        else:
            return deposit_amount
    
    except TypeError:
     print("Amount must be a numeric type.")
    
def get_balance(account_number: int) -> str:
    """
    Returns a balance statement as a string containing
    account number and balance in a currency format.

    Args:
        integer: account number / key to access ACCOUNTS dictionary

    returns:
        string: a string containing the balance of the input account
    """
   
    try:
        type(account_number) == int
    
        
        if account_number not in ACCOUNTS:
            raise ValueError("Account number entered does not exist.")
        
        else:
            balance = ACCOUNTS[account_number]["balance"]
            balance_formatted = f"${balance:,.2f}"
            return f"Your current balance for account {account_number} is {balance_formatted}."

    except TypeError:
        print("Account number must be an int type.")

def make_deposit(account_num: int, deposit_amount: int) -> str:
    """Returns a string containing an account number and amount deposited.

    args:
        account_num (int): the number of the account.
        deposit_amount (int or float): the number being deposited.

    returns:
        A string containing an account number and amount deposited.
    
    """

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
    task_input = input("What would you like to do (balance/deposit/exit)?: ")
    task = task_input.lower()
    if task not in VALID_TASKS:
        raise ValueError(f"{task} is an unknown task.")
    
    return task


def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")
    
        # select menu option
    task = get_task()
    
        # Print thank you message
    if task == "exit":
        print(f"Thank you for banking with {COMPANY_NAME}.")

        # thank you msg lingers then clear
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    
    else:
        # verify acc num in dictionary
        account_number = get_account_number()
        if account_number in ACCOUNTS:
            if task == "deposit":
                # make deposit
                # deposit amount
                amount = get_amount()
                # deposit msg and wait
                print(make_deposit(account_number, amount))
                time.sleep(3)

                # calc new balance
                ACCOUNTS[account_number]["balance"] += amount
                print(get_balance(account_number))

                # balance msg lingers then returns to start
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')

                # return to start
                chatbot()
            elif task == "balance":

                # get balance
                print(get_balance(account_number))

                
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                # return to start
                chatbot()
                


if __name__ == "__main__":
    chatbot()

