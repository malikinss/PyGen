'''
TODO:
    Implement a Money class that describes a monetary amount in rubles.

    When creating an instance, the class must accept one argument:
        amount — the amount of money

    An instance of the Money class must have the following informal string
    representation:
        <amount of money> rubles.

    Also, an instance of the Money class must support the unary
    operators + and -:
        - the result of the unary + must be a new instance of the Money class
          with a non-negative amount of money
        - the result of the unary - must be a new instance of the Money class
          with a negative amount of money

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Money class,
    it can be arbitrary.
'''


class Money:
    """
    A class representing a monetary amount in rubles.
    """

    def __init__(self, amount: float) -> None:
        """
        Initialize a Money instance.

        Args:
            amount (float): The amount of money in rubles.
        """
        self.amount = amount

    def __str__(self) -> str:
        """
        Return an informal string representation of the amount.

        Returns:
            str: The amount in format '<amount> rubles'.
        """
        return f"{self.amount} rubles"

    def __pos__(self) -> 'Money':
        """
        Return a new Money instance with a non-negative amount.

        Returns:
            Money: A new instance with abs(amount).
        """
        return Money(abs(self.amount))

    def __neg__(self) -> 'Money':
        """
        Return a new Money instance with a negative amount.

        Returns:
            Money: A new instance with -abs(amount).
        """
        return Money(-abs(self.amount))
