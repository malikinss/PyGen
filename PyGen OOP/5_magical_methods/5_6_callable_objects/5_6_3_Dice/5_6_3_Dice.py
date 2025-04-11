'''
TODO:
    Implement a Dice class that describes a dice with a certain number of
    sides.

    When instantiated, the class must accept one argument:
        sides — the number of sides of the dice

    An instance of the Dice class must be a callable object and must not
    accept any arguments.

    When called, it must return the value of a random side of the dice.

    For example, if the dice has 6 sides, an instance of the Dice class must
    return a random number from the range [1; 6].

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Dice class,
    it can be arbitrary.
'''
import random


class Dice:
    """
    A class representing a dice with a fixed number of sides.
    """

    def __init__(self, sides: int) -> None:
        """
        Initialize Dice with a specified number of sides.

        Args:
            sides (int): The number of sides on the dice.
        """
        self.sides = sides

    def __call__(self) -> int:
        """
        Simulate rolling the dice and return a random side value.

        Returns:
            int: A random number from 1 to the number of sides (inclusive).
        """
        return random.randint(1, self.sides)
