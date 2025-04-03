# BankAccount Class Finance Manager

## Description 📝

The `BankAccount` class simulates a bank account with a balance that can be initialized optionally (defaulting to 0).
It provides methods to check the balance, deposit funds, withdraw funds with overdraft protection, and transfer funds to another account, ensuring sufficient funds before withdrawals or transfers.

## Purpose 🎯

This class is designed for financial simulations, educational examples of object-oriented programming, or as a component in systems requiring basic account management with balance constraints.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `_balance` to the provided value or 0 if none is given.
-   **get_balance() Method**: Returns the current `_balance`.
-   **deposit() Method**: Increases `_balance` by the specified amount.
-   **withdraw() Method**: Decreases `_balance` by the amount if sufficient funds exist, otherwise raises a `ValueError`.
-   **transfer() Method**: Transfers an amount to another `BankAccount` instance if funds are sufficient, otherwise raises a `ValueError`.
-   **Helper Method**: `_check_funds()` ensures balance sufficiency, raising an error with a custom message if funds are lacking.

## Usage 📦

1. Save the class in a Python file, e.g., `bank_account.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from bank_account import BankAccount
account1 = BankAccount(100)
account2 = BankAccount()
account1.deposit(50)
account1.transfer(account2, 30)
print(f"Account1 balance: {account1.get_balance()}")
print(f"Account2 balance: {account2.get_balance()}")
```

## Conclusion 🚀

The `BankAccount` class offers a robust and straightforward way to manage a bank account’s balance in Python.
Its built-in overdraft protection via exceptions ensures safe transactions, making it a reliable tool that can be extended with features like transaction history or interest calculations for more complex financial applications.
