'''
TODO:
    Implement a Calculator class whose instances can perform various
    arithmetic operations on two numbers.

    When instantiating the class, it should not accept any arguments.

    An instance of the Calculator class should be a callable object and accept
    three arguments:
        a is a number
        b is a number
        operation is one of the symbols +, -, *, and /

    If operation is +, the Calculator instance should return the sum of a
    and b, if -, the difference of a and b, if *, the product of a and b,
    and if /, the quotient of a and b.

    An attempt to divide by zero should raise a ValueError exception with
    the text:
        Division by zero is impossible

NOTE:
    Instances of the int and float classes will be considered as numbers.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the Calculator class, it can be arbitrary.
'''
from typing import Union
from operator import add, sub, mul, truediv


class Calculator:
    """
    A class representing a calculator for basic arithmetic operations.
    """

    _operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    def __call__(
        self, a: Union[int, float], b: Union[int, float], operation: str
    ) -> Union[int, float]:
        """Perform an arithmetic operation on two numbers.

        Args:
            a (int | float): First number.
            b (int | float): Second number.
            operation (str): One of '+', '-', '*', '/' to specify
                             the operation.

        Returns:
            int | float: Result of the operation (sum, difference, product,
                         or quotient).

        Raises:
            ValueError: If operation is '/' and b is 0, with message:
                            'Division by zero is impossible'.
        """
        if operation == '/' and b == 0:
            raise ValueError("Division by zero is impossible")
        return self._operations[operation](a, b)
