'''
TODO:
    Often, when sorting objects, we use an additional function that describes
    the sorting rule.

    For example, if we need to sort a list of instances of a certain class
    based on the values of a certain attribute, we can implement a function
    that takes this instance as an argument and returns the value of
    the required attribute.

    The code below:
        class User:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
                return f'User({self.name}, {self.age})'

        users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]
        print(sorted(users, key=lambda user: user.age))

    outputs:
        [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]

    It would be convenient to have a SortKey class that allows sorting objects
    based on the values of various attributes, just listing the names of
    these attributes.

    So that the code below:
        class User:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
            return f'User({self.name}, {self.age})'

        users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]
        print(sorted(users, key=SortKey('age')))
        # sorting based on the age attribute
        print(sorted(users, key=SortKey('name', 'age')))
        # sorting based on the name attribute, and then age
    outputs:
        [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
        [User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]

    Implement the SortKey class, which describes a key for sorting objects
    based on the values of their specified attributes.

    When instantiating the class, it must accept an arbitrary number of
    positional arguments, each of which represents the name of an attribute
    involved in the sorting.

NOTE:
    When instantiating the SortKey class, the attribute names are passed in
    order of priority, that is, when sorting, the value of the first attribute
    must be taken into account first, then the second, and so on.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the SortKey
    class, it can be arbitrary.
'''
from typing import Any


class SortKey:
    """
    A class for creating a sorting key based on object attributes.
    """

    def __init__(self, *attributes: str) -> None:
        """
        Initialize SortKey with attribute names for sorting.

        Args:
            *attributes (str): Names of attributes to sort by, in order
                               of priority.
        """
        self.attributes = attributes

    def __call__(self, instance: Any) -> tuple:
        """
        Generate a sorting key from the instance's attribute values.

        Args:
            instance (Any): The object to extract attribute values from.

        Returns:
            tuple: A tuple of attribute values for sorting.
        """
        return tuple(instance.__dict__[attr] for attr in self.attributes)
