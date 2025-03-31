'''
TODO:
    You have access to the User class, which describes an Internet user.

    When creating an instance, the class takes one argument:
        - name — user name

    An instance of the User class has two attributes:
        - name — user name
        - friends — number of friends of the user, the initial value is 0

    The User class has one instance method:
        - add_friends() — a method that takes an integer n as an argument and
        increases the number of friends of the user by n

    Find and correct errors made in the implementation of the add_friends()
    method.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''


class User:
    """
    A class representing an Internet user.

    Attributes:
        name (str): The name of the user.
        friends (int): The number of friends, initially set to 0.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new User instance.

        Args:
            name (str): The name of the user.
        """
        self.name = name
        self.friends = 0

    def add_friends(self, n: int) -> None:
        """
        Increases the number of friends of the user by n.

        Args:
            n (int): The number of friends to add.
        """
        self.friends += n
