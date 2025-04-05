'''
TODO:
    For security purposes, user account passwords are not stored in explicit
    form in databases, but as hash values ​​— numbers calculated using
    a special algorithm based on passwords.

    You have access to the hash_function() function, which takes a password as
    an argument and returns its hash value.

    Implement the Account class, which describes an Internet user account on
    some service.

    When creating an instance, the class must accept two arguments in the
    following order:
        - login — user login
        - password — user password

    The Account class must have two properties:
        - login — a read-only property that returns the user login.
        When attempting to change the property, an AttributeError exception
        must be raised with the text:
            Changing the login is impossible

        - password — a read-write property that returns the hash value of the
        user account password.
        When changing, the property should calculate the hash value of
        the new password and store it, not the password itself

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Account
    class, it can be arbitrary.
'''


def hash_function(password):
    """
    Calculate a hash value from a password.
    """
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    """
    A class representing an Internet user account.

    Attributes:
        _login (str): The user's login, stored internally.
        _password (int): The hash value of the user's password, stored
                         internally.

    Properties:
        login (str): A read-only property returning the user's login.
        password (int): A read-write property returning the hash value of
                        the password.
    """

    def __init__(self, login: str, password: str) -> None:
        """
        Initialize an Account instance with a login and password.

        Args:
            login (str): The user's login.
            password (str): The user's password, stored as a hash.
        """
        self._login: str = login
        self._password: int = hash_function(password)

    @property
    def login(self) -> str:
        """
        Get the user's login.

        Returns:
            str: The user's login.
        """
        return self._login

    @login.setter
    def login(self, login: str) -> None:
        """
        Prevent changes to the login.

        Args:
            login (str): The new login value (ignored).

        Raises:
            AttributeError: Always raised with message:
                'Changing the login is impossible'.
        """
        raise AttributeError("Changing the login is impossible")

    @property
    def password(self) -> int:
        """
        Get the hash value of the user's password.

        Returns:
            int: The hash value of the password.
        """
        return self._password

    @password.setter
    def password(self, new_password: str) -> None:
        """
        Set a new password by storing its hash value.

        Args:
            new_password (str): The new password to hash and store.
        """
        self._password = hash_function(new_password)
