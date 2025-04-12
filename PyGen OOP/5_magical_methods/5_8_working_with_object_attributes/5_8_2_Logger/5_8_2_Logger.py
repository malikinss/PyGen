'''
TODO:
    It was required to implement the Logger class.

    The class was not supposed to accept any arguments when instantiating it.

    It was assumed that when setting or changing the value of an attribute of
    the Logger class instance, the following text would be displayed:
        Changing the value of the attribute <attribute name>
        to <new attribute value>

    It was also planned that when deleting an attribute, the following text
    would be displayed:
        Deleting the attribute <attribute name>

    The programmer was in a hurry and solved the problem incorrectly.

    Complete the code below and implement the correct Logger class.

NOTE:
    There are no restrictions regarding the implementation of the Logger class,
    it can be arbitrary.
'''
from typing import Any


class Logger:
    """
    A class that logs attribute changes and deletions.
    """

    def __init__(self) -> None:
        """
        Initialize an empty Logger instance.
        """
        pass

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Log and set an attribute value.

        Args:
            attr (str): The name of the attribute.
            value (Any): The new value of the attribute.
        """
        print(f'Изменение значения атрибута {attr} на {value}')
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr: str) -> None:
        """
        Log and delete an attribute.

        Args:
            attr (str): The name of the attribute.
        """
        print(f'Удаление атрибута {attr}')
        object.__delattr__(self, attr)
