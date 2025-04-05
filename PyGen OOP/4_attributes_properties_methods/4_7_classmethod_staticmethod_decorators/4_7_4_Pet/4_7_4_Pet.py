'''
TODO:
    Implement a Pet class that describes a pet.

    When instantiated, the class must accept one argument:
        - name — the name of the pet

    An instance of the Pet class must have one attribute:
        - name — the name of the pet

    The Pet class must have three class methods:
        - first_pet() — a method that returns the very first instantiated
                        Pet class.
                        If no instances have been instantiated yet, the method
                        must return None
        - last_pet() — a method that returns the very last instantiated
                       Pet class.
                       If no instances have been instantiated yet, the method
                       must return None
        - num_of_pets() — a method that returns the number of instantiated
                          Pet class instances

NOTE:
    There are no restrictions on the implementation of the Pet class,
    it can be arbitrary.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Optional


class Pet:
    """
    A class representing a pet.

    Attributes:
        name (str): The name of the pet.

    Class Attributes:
        _counter (int): The number of instantiated Pet objects.
        _first (Pet | None): The first instantiated Pet object.
        _last (Pet | None): The last instantiated Pet object.
    """
    _counter: int = 0
    _first: Optional['Pet'] = None
    _last: Optional['Pet'] = None

    def __init__(self, name: str) -> None:
        """
        Initialize a Pet instance with a name.

        Args:
            name (str): The name of the pet.
        """
        if Pet._counter == 0:
            Pet._first = self

        Pet._last = self
        Pet._counter += 1
        self.name: str = name

    @classmethod
    def first_pet(cls) -> Optional['Pet']:
        """
        Get the first instantiated Pet object.

        Returns:
            Pet | None: The first Pet instance, or None if no instances exist.
        """
        return cls._first

    @classmethod
    def last_pet(cls) -> Optional['Pet']:
        """
        Get the last instantiated Pet object.

        Returns:
            Pet | None: The last Pet instance, or None if no instances exist.
        """
        return cls._last

    @classmethod
    def num_of_pets(cls) -> int:
        """
        Get the number of instantiated Pet objects.

        Returns:
            int: The total number of Pet instances.
        """
        return cls._counter
