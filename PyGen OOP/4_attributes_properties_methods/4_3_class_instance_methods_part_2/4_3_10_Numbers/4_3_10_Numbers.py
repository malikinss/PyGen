'''
TODO:
    Implement a Numbers class that describes an initially empty, extensible
    set of integers.

    The class must not take any arguments when instantiated.

    The Numbers class must have three instance methods:
        - add_number() — a method that takes an integer as an argument and
        adds it to the set
        - get_even() — a method that returns a list of all even numbers
        in the set
        - get_odd() — a method that returns a list of all odd numbers
        in the set

NOTE:
    The numbers in the lists returned by get_even() and get_odd() must be in
    the order in which they were added to the set.

    No additional validation of the data is required.

    It is guaranteed that the implemented class is used only with valid data.
'''
from typing import List


class Numbers:
    """
    A class representing an extensible collection of integers.

    This class maintains a list of integers and provides methods to add
    numbers and retrieve even or odd numbers in the order they were added.

    Attributes:
        numbers (list[int]): A list storing the integers added to the
        collection.

    Methods:
        add_number(num): Adds an integer to the collection.
        get_even(): Returns a list of all even numbers in the collection.
        get_odd(): Returns a list of all odd numbers in the collection.
    """

    def __init__(self) -> None:
        """
        Initialize a Numbers instance with an empty list.

        Sets up the collection with an empty list to store integers.

        Returns:
            None
        """
        self.numbers: List[int] = []

    def add_number(self, num: int) -> None:
        """
        Add an integer to the collection.

        Appends the provided integer to the internal list.

        Args:
            num (int): The integer to add to the collection.

        Returns:
            None
        """
        self.numbers.append(num)

    def get_even(self) -> List[int]:
        """
        Return a list of all even numbers in the collection.

        Retrieves all even integers from the collection in their original
        order.

        Returns:
            list[int]: A list of even numbers.
        """
        return [num for num in self.numbers if num % 2 == 0]

    def get_odd(self) -> List[int]:
        """Return a list of all odd numbers in the collection.

        Retrieves all odd integers from the collection in their original order.

        Returns:
            list[int]: A list of odd numbers.
        """
        return [num for num in self.numbers if num % 2 != 0]
