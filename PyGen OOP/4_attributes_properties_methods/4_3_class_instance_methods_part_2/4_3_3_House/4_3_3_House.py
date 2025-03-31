'''
TODO:
    You have access to the House class, which describes a house.

    When instantiating the class, it takes two arguments in the following
    order:
        - color — the color of the house
        - rooms — the number of rooms in the house

    An instance of this class has two attributes:
        - color — the color of the house
        - rooms — the number of rooms in the house

    Implement two instance methods for the House class:
        - paint() — a method that takes a new_color value as an argument and
        changes the current color of the house to new_color
        - add_rooms() — a method that takes an integer n as an argument and
        increases the number of rooms in the house by n

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class House:
    """
    A class representing a house.

    Attributes:
        color (str): The color of the house.
        rooms (int): The number of rooms in the house.
    """

    def __init__(self, color: str, rooms: int) -> None:
        """
        Initializes a new House instance.

        Args:
            color (str): The color of the house.
            rooms (int): The number of rooms in the house.
        """
        self.color = color
        self.rooms = rooms

    def paint(self, new_color: str) -> None:
        """
        Changes the color of the house.

        Args:
            new_color (str): The new color of the house.
        """
        self.color = new_color

    def add_rooms(self, n: int) -> None:
        """
        Increases the number of rooms in the house.

        Args:
            n (int): The number of rooms to add.
        """
        self.rooms += n
