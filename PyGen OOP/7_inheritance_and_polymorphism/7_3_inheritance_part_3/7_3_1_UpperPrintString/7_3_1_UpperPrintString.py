'''
TODO:
    Implement the UpperPrintString class, a subclass of str that describes
    a string.

    The process of creating an instance of the UpperPrintString class must be
    the same as the process of creating an instance of the str class.

    An instance of the UpperPrintString class must have the following informal
    string representation:
        <uppercase string value>

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with valid data.

    There are no restrictions regarding the implementation of
    the UpperPrintString class, it can be arbitrary.
'''


class UpperPrintString(str):
    """
    Class representing a string with uppercase informal string representation.

    Inherits from str and returns the string in uppercase for its informal
    representation.
    """

    def __str__(self) -> str:
        """
        Return the string in uppercase.

        Returns:
            str: The string value in uppercase.
        """
        return super().__str__().upper()
