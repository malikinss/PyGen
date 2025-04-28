'''
TODO:
    Implement the MROHelper class that describes a set of functions for
    working with MROs of arbitrary classes.

    The class must not take any arguments when instantiated.

    The MROHelper class must have three static methods:
        len() — a method that takes a class as an argument and returns
                the number of elements in its MRO
        class_by_index() — a method that takes a class cls and an integer n,
                           zero by default, as arguments and returns the class
                           with index n in the MRO of class cls
        index_by_class() — a method that takes two classes child and parent
                           as arguments and returns an integer — the index of
                           the parent class in the MRO of class child

NOTE:
    The numbering of classes in the MRO starts with zero.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions on the implementation of the MROHelper class, it
    can be arbitrary.
'''


class MROHelper:
    """
    Helper class with static methods for working with Method Resolution Order
    (MRO).
    """

    @staticmethod
    def len(cls: type) -> int:
        """
        Return the number of classes in the MRO of the given class.

        Args:
            cls: The class to inspect.

        Returns:
            int: Number of classes in the MRO.
        """
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(cls: type, n: int = 0) -> type:
        """
        Return the class at index n in the MRO of the given class.

        Args:
            cls: The class to inspect.
            n: Index in the MRO, defaults to 0.

        Returns:
            type: Class at the specified index.
        """
        return cls.__mro__[n]

    @staticmethod
    def index_by_class(child: type, parent: type) -> int:
        """
        Return the index of the parent class in the MRO of the child class.

        Args:
            child: The class whose MRO is inspected.
            parent: The class to find in the MRO.

        Returns:
            int: Index of the parent class in the MRO.
        """
        return child.__mro__.index(parent)
