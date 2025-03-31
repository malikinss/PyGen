'''
TODO:
    Implement a Scales class that describes a scale with two pans.

    The class must not take any arguments when instantiated.

    The Scales class must have three instance methods:
        - add_right() — a method that takes a weight in kilograms as an
        argument and adds this weight to the right pan of the scale
        - add_left() — a method that takes a weight in kilograms as an
        argument and adds this weight to the left pan of the scale
        - get_result() — a method that returns a string.

        The scale is balanced if the weights on the pans are the same.

        The right pan is heavier if the right pan is heavier.

        The left pan is heavier if the left pan is heavier

NOTE:
    Empty scales are always balanced.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class Scales:
    """
    A class representing a two-pan balance scale.

    This class simulates a scale with two pans (left and right), tracking the
    weight added to each.

    It determines the balance state based on the total
    weight on each pan.

    The class is instantiated without arguments.

    Attributes:
        right_pan (float): Total weight in kilograms on the right pan,
                           starting at 0.
        left_pan (float): Total weight in kilograms on the left pan,
                          starting at 0.

    Methods:
        add_right(weight): Adds weight to the right pan.
        add_left(weight): Adds weight to the left pan.
        get_result(): Returns the current balance state as a string.
    """
    BALANCED = 'The scale is balanced'
    LEFT_HEAVIER = 'The left pan is heavier'
    RIGHT_HEAVIER = 'The right pan is heavier'

    def __init__(self) -> None:
        """
        Initialize a Scales instance with empty pans.

        Sets up the scale with zero weight on both the left and right pans.

        Returns:
            None
        """
        self.right_pan: float = 0
        self.left_pan: float = 0

    def add_right(self, weight: float) -> None:
        """
        Add weight to the right pan of the scale.

        Increases the total weight on the right pan by the specified amount.

        Args:
            weight (float): The weight in kilograms to add to the right pan.

        Returns:
            None
        """
        self.right_pan += weight

    def add_left(self, weight: float) -> None:
        """
        Add weight to the left pan of the scale.

        Increases the total weight on the left pan by the specified amount.

        Args:
            weight (float): The weight in kilograms to add to the left pan.

        Returns:
            None
        """
        self.left_pan += weight

    def get_result(self) -> str:
        """
        Determine and return the current balance state of the scale.

        Compares the weights on the left and right pans and returns a string
        indicating whether the scale is balanced, the left pan is heavier, or
        the right pan is heavier.

        Returns:
            str: The balance state ('Весы в равновесии', 'Левая чаша тяжелее',
                 or 'Правая чаша тяжелее').
        """
        if self.left_pan > self.right_pan:
            return self.LEFT_HEAVIER
        elif self.left_pan < self.right_pan:
            return self.RIGHT_HEAVIER

        return self.BALANCED
