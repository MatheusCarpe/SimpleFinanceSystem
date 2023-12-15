# Simple Finance System

## Overview
This Python project implements a straightforward finance system with features such as
deposit, withdrawal, statement viewing, and balance checking. The system is
organized into modular files for clarity and modularity. It incorporates error handling,
daily withdrawal limits, and timestamps for transactions.


## Files

1. bank_system.py: Main file containing the Bank class representing the finance
system. Handles deposit, withdrawal, statement viewing, and balance checking.
Execute this file to interact with the system.


2. balance.py: Contains the do_balance function to display the current account balance.


3. statement.py: Includes the do_statement function allowing users to view
different types of statements: general, withdrawal, and deposit.


5. deposit.py: Implements the do_deposit function for handling deposit
operations.

7. withdraw.py: Contains the do_withdraw function for managing withdrawal operations.

   

## How to Run
Execute bank_system.py to run the finance system. The system displays a text-based menu
for deposit, withdrawal, statement viewing, balance checking, and quitting. Follow the prompts
for each operation.


## Additional Notes

. The system employs a simple text-based menu for user interaction.

. Robust error handling is implemented for valid input during deposit and withdrawal operations.

. Statements are categorized into general, withdrawal, and deposit statements for effective tracking.

. The system enforces a daily withdrawal limit of three withdrawals.

. Transaction timestamps are based on the current date and time.

. Feel free to customize or extend the system based on your requirements.
Contributions and feedback are welcome!


Note: Ensure that you have Python installed to run this application.
