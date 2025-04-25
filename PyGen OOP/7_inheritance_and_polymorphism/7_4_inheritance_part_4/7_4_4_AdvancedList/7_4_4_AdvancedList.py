'''
TODO:
    Implement the AdvancedList class, a subclass of the list class,
    that describes a list with additional functionality.

    The process of creating an instance of the AdvancedList class must be
    the same as the process of creating an instance of the list class.

    The AdvancedList class must have three instance methods:
        join() — a method that concatenates all elements of the AdvancedList
                 class instance into a string and returns the resulting result.
                 The method must take one string argument, by default equal to
                 a space, which is the separator between list elements in
                 the resulting string
        map() — a method that takes a function func as an argument and applies
                it to each element of the AdvancedList class instance.
                The method must modify the original AdvancedList class
                instance, not return a new one
        filter() — a method that takes a function func as an argument and
                   removes from the AdvancedList class instance those elements
                   for which the func function returned False.
                   The method must modify the original AdvancedList class
                   instance, not return a new one

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the AdvancedList
    class; it can be arbitrary.
'''
from typing import Any, Callable


class AdvancedList(list):
    """
    Class representing a list with additional functionality.

    Inherits from list, providing methods to join elements into a string,
    map a function over elements, and filter elements in-place.
    """

    def join(self, separator: str = " ") -> str:
        """
        Concatenate all elements into a string with a separator.

        Args:
            separator: The string to separate elements, defaults to a space.

        Returns:
            str: The concatenated string of all elements.
        """
        return separator.join(map(str, self))

    def map(self, func: Callable[[Any], Any]) -> None:
        """
        Apply a function to each element, modifying the list in-place.

        Args:
            func: The function to apply to each element.
        """
        for i in range(len(self)):
            self[i] = func(self[i])

    def filter(self, func: Callable[[Any], bool]) -> None:
        """
        Remove elements where func returns False, modifying the list in-place.

        Args:
            func: The function to test each element, returning True to keep
            the element.
        """
        self[:] = [el for el in self if func(el)]
