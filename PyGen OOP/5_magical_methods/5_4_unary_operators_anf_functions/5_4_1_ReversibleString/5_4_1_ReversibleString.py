'''
TODO:
    Implement a ReversibleString class that describes a string.

    When instantiated, the class must accept one argument:
        string — the string value

    An instance of the ReversibleString class must have the following informal
    string representation:
        <string value>

    Also, an instance of the ReversibleString class must support the unary
    operator -, which must result in a new instance of the ReversibleString
    class with the string value in reverse order.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the ReversibleString class, it can be arbitrary.
'''


class ReversibleString:
    """
    A class representing a string that can be reversed with the unary minus
    operator.
    """

    def __init__(self, string: str) -> None:
        """
        Initialize a ReversibleString instance.

        Args:
            string (str): The string value.
        """
        self.string = string

    def __str__(self) -> str:
        """
        Return an informal string representation of the string.

        Returns:
            str: The string value.
        """
        return self.string

    def __neg__(self) -> 'ReversibleString':
        """
        Return a new ReversibleString instance with the string reversed.

        Returns:
            ReversibleString: A new instance with the reversed string.
        """
        return ReversibleString(self.string[::-1])
