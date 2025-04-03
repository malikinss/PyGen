'''
TODO:
    Implement a User class that describes an Internet user.

    When instantiated, the class must accept two arguments in the following
    order:
        - name — the user's name.
        If name is not a non-empty string consisting only of letters,
        a ValueError exception must be raised with the text:
            Invalid name

        - age — the user's age.
        If age is not an integer in the range [0; 110], a ValueError exception
        must be raised with the text:
            Invalid age

    An instance of the User class must have two attributes:
        _name — the user's name
        _age — the user's age

    The User class must have four instance methods:
        - get_name() — a method that returns the user's name

        - set_name() — a method that takes new_name as an argument and changes
        the user's name to new_name.
        If new_name is not a non-empty string consisting only of letters,
        a ValueError exception should be raised with the text:
            Invalid name

        - get_age() is a method that returns the user's age

        - set_age() is a method that takes new_age as an argument and changes
        the user's age to new_age.
        If new_age is not an integer in the range [0; 110], a ValueError
        exception should be raised with the text:
            Invalid age

NOTE:
    If both the name and age are invalid when creating an instance of the User
    class, an exception related to the name should be raised.
'''
import re


class User:
    """
    A class representing an Internet user with name and age.

    This class encapsulates a user's name and age, enforcing validation rules
    during instantiation and updates. The name must be a non-empty string of
    Latin or Russian letters, and the age must be an integer between 0 and 110
    inclusive.

    Attributes:
        _name (str): The user's name.
        _age (int): The user's age.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a User instance with a name and age.

        Validates the provided name and age, raising exceptions if invalid.
        Name validation takes precedence over age validation if both fail.

        Args:
            name (str): The user's name, must be a non-empty string of Latin
                or Russian letters.
            age (int): The user's age, must be an integer in [0; 110].

        Raises:
            ValueError: If name is invalid, with message 'Invalid name'.
            ValueError: If age is invalid, with message 'Invalid age'.
        """
        self._validate_name(name)
        self._validate_age(age)
        self._name: str = name
        self._age: int = age

    def _validate_name(self, name: str) -> None:
        """
        Validate that the name is a non-empty string of Latin or Russian
        letters.

        Uses a regular expression to ensure the name contains only Latin
        (a-z, A-Z) or Russian (а-я, А-Я) letters and is not empty.

        Args:
            name (str): The name to validate.

        Raises:
            ValueError: If name is not a non-empty string of Latin or Russian
                letters, with message 'Invalid name'.
        """
        regex = r'[a-zA-Zа-яА-Я]+'
        if not isinstance(name, str) or not re.fullmatch(regex, name):
            raise ValueError('Invalid name')

    def _validate_age(self, age: int) -> None:
        """
        Validate that the age is an integer between 0 and 110 inclusive.

        Converts age to string and uses a regular expression to check if it
        matches an integer in the range [0; 110].

        Args:
            age (int): The age to validate.

        Raises:
            ValueError: If age is not an integer in [0; 110], with message
                'Invalid age'.
        """
        regex = r'[0-9]|[1-9][0-9]|10[0-9]|110'
        if not isinstance(age, int) or not re.fullmatch(regex, str(age)):
            raise ValueError('Invalid age')

    def get_name(self) -> str:
        """
        Return the user's name.

        Provides access to the user's current name.

        Returns:
            str: The user's name.
        """
        return self._name

    def set_name(self, new_name: str) -> None:
        """
        Change the user's name to the specified new name.

        Updates the user's name if the new name is valid.

        Args:
            new_name (str): The new name, must be a non-empty string of Latin
                or Russian letters.

        Raises:
            ValueError: If new_name is invalid, with message 'Invalid name'.
        """
        self._validate_name(new_name)
        self._name = new_name

    def get_age(self) -> int:
        """
        Return the user's age.

        Provides access to the user's current age.

        Returns:
            int: The user's age.
        """
        return self._age

    def set_age(self, new_age: int) -> None:
        """
        Change the user's age to the specified new age.

        Updates the user's age if the new age is valid.

        Args:
            new_age (int): The new age, must be an integer in [0; 110].

        Raises:
            ValueError: If new_age is not in [0; 110], with message
            'Invalid age'.
        """
        self._validate_age(new_age)
        self._age = new_age
