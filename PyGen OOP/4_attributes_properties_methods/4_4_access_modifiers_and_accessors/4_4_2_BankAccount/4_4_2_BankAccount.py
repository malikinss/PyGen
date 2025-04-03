'''
TODO:
    Implement the BankAccount class that describes a bank account.

    When instantiated, the class must accept one argument:
        balance — the account balance, 0 by default

    An instance of the BankAccount class must have one attribute:
        _balance — the account balance

    The BankAccount class must have four instance methods:
        get_balance() — a method that returns the current account balance
        deposit() — a method that takes an amount as an argument and increases
        the account balance by amount
        - withdraw() — a method that takes an amount as an argument and
        decreases the account balance by amount.
        If amount exceeds the amount of funds in the account balance,
        a ValueError exception must be raised with the message:
            There are not enough funds in the account
        - transfer() — a method that takes the bank account account and the
        amount number as arguments.
        The method must decrease the balance of the current account by amount
        and increase the balance of the account account by amount.
        If amount exceeds the balance of the current account, a ValueError
        exception should be raised with the message:
            There are not enough funds on the account

NOTE:
    Instances of the int and float classes will be considered as numbers.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Union


class BankAccount:
    """
    A class representing a bank account with balance management.

    This class encapsulates a bank account's balance and provides methods
    to retrieve the balance, deposit funds, withdraw funds, and transfer
    funds to another account. It enforces balance checks to prevent overdraft.

    Attributes:
        _balance (float | int): The current balance of the account.
    """

    def __init__(self, balance: Union[float, int] = 0) -> None:
        """
        Initialize a BankAccount instance with an optional balance.

        Sets the initial balance of the account. If no balance is provided,
        it defaults to 0.

        Args:
            balance (float | int): Initial account balance, defaults to 0.

        Returns:
            None
        """
        self._balance: Union[float, int] = balance

    def get_balance(self) -> Union[float, int]:
        """
        Return the current balance of the account.

        Provides access to the account's current balance.

        Returns:
            float | int: The current balance.
        """
        return self._balance

    def deposit(self, amount: Union[float, int]) -> None:
        """
        Increase the account balance by the specified amount.

        Adds the given amount to the current balance.

        Args:
            amount (float | int): The amount to deposit.

        Returns:
            None
        """
        self._balance += amount

    def _check_funds(self, amount: Union[float, int]) -> None:
        """
        Check if the account has enough funds for the operation.

        Raises a ValueError with the specified message if the amount exceeds
        the current balance.

        Args:
            amount (float | int): The amount to check against the balance.

        Raises:
            ValueError: If the amount exceeds the current balance, with the
                provided error message.
        """
        if self._balance < amount:
            raise ValueError('There are not enough funds in the account')

    def withdraw(self, amount: Union[float, int]) -> None:
        """
        Decrease the account balance by the specified amount.

        Subtracts the given amount from the current balance. If the amount
        exceeds the current balance, raises a ValueError.

        Args:
            amount (float | int): The amount to withdraw.

        Raises:
            ValueError: If the amount exceeds the current balance, with the
                message 'There are not enough funds in the account'.

        Returns:
            None
        """
        self._check_funds(amount)
        self._balance -= amount

    def transfer(
        self, account: 'BankAccount', amount: Union[float, int]
    ) -> None:
        """
        Transfer funds from this account to another account.

        Decreases the balance of this account by the specified amount and
        increases the balance of the target account by the same amount.
        If the amount exceeds the current balance, raises a ValueError.

        Args:
            account (BankAccount): The target account to transfer funds to.
            amount (float | int): The amount to transfer.

        Raises:
            ValueError: If the amount exceeds the current balance, with the
                message 'There are not enough funds on the account'.

        Returns:
            None
        """
        self._check_funds(amount)
        self._balance -= amount
        account.deposit(amount)
