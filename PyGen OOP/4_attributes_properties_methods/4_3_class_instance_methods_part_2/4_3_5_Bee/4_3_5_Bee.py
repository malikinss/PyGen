'''
TODO:
    Implement a Bee class that describes a bee that moves along the coordinate
    plane in four directions:
        up, down, left, and right.

    When instantiated, the class must take two arguments in the following
    order:
        - x — the x-coordinate of the bee, defaults to 0
        - y — the y-coordinate of the bee, defaults to 0

    A Bee instance must have two attributes:
        - x — the x-coordinate of the bee
        - y — the y-coordinate of the bee

    The Bee class must have four instance methods:
        - move_up()     — a method that takes an integer n as an argument and
                          increases the y-coordinate of the bee by n
        - move_down()   — a method that takes an integer n as an argument and
                          decreases the y-coordinate of the bee by n
        - move_right()  — a method that takes an integer n as an argument and
                          increases the x-coordinate of the bee by n
        - move_left()   — a method that takes an integer n as an argument and
                          decreases the x-coordinate of the bee by n

NOTE:
    No additional data validation is required. It is guaranteed that the
    implemented class is used only with correct data.
'''


class Bee:
    """
    A class representing a bee moving in a 2D coordinate plane.

    Attributes:
        x (int): The x-coordinate of the bee. Default is 0.
        y (int): The y-coordinate of the bee. Default is 0.

    Methods:
        __init__(x: int, y: int) -> None:
            Initializes a new Bee instance with the given coordinates.

        move_up(n: int) -> None:
            Moves the bee up by increasing its y-coordinate by n.

        move_down(n: int) -> None:
            Moves the bee down by decreasing its y-coordinate by n.

        move_right(n: int) -> None:
            Moves the bee right by increasing its x-coordinate by n.

        move_left(n: int) -> None:
            Moves the bee left by decreasing its x-coordinate by n.
    """

    def __init__(self, x: int = 0, y: int = 0):
        """
        Initializes a new Bee instance.

        Args:
            x (int): The initial x-coordinate of the bee (default is 0).
            y (int): The initial y-coordinate of the bee (default is 0).
        """
        self.x = x
        self.y = y

    def move_up(self, n: int) -> None:
        """
        Moves the bee up by increasing its y-coordinate by n.

        Args:
            n (int): The number to increase the y-coordinate by.
        """
        self.y += n

    def move_down(self, n: int) -> None:
        """
        Moves the bee down by decreasing its y-coordinate by n.

        Args:
            n (int): The number to decrease the y-coordinate by.
        """
        self.y -= n

    def move_right(self, n: int) -> None:
        """
        Moves the bee right by increasing its x-coordinate by n.

        Args:
            n (int): The number to increase the x-coordinate by.
        """
        self.x += n

    def move_left(self, n: int) -> None:
        """
        Moves the bee left by decreasing its x-coordinate by n.

        Args:
            n (int): The number to decrease the x-coordinate by.
        """
        self.x -= n
