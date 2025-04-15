'''
TODO:
    Often we need to group objects by a certain feature.

    For example, strings can be grouped by their length or the first character.

    Implement the Grouper class, which describes an object that groups
    elements of some iterable object based on a key function.

    When instantiating, the class must accept two arguments in the following
    order:
        iterable — iterable object
        key — key function

    Elements are grouped if the key function returns the same result when
    passed to them.

    For example, elem1 and elem2 are grouped if key(elem1) == key(elem2).

    The value of key(elem1) is called the group key, and elem1 and elem2
    are group elements by this key.

    The Grouper class must have two instance methods:
        add() — a method that takes an arbitrary object as an argument and
                adds it to the desired group of the Grouper class instance
        group_for() — a method that takes an arbitrary object as an argument,
                      determines which group of the Grouper class instance
                      this object will fall into, and returns the key of this
                      group

    When passing an instance of the Grouper class to the len() function,
    the number of groups in it must be returned.

    In addition, the Grouper class instance must be an iterable object,
    that is, it must allow iterating over its groups, for example, using
    a for loop.

    In this case, a group is a tuple, the first element of which is the group
    key, and the second is a list of group elements.

    When iterating, groups can be arranged in any order.

    Also, the Grouper class instance must support the membership check
    operation using the in operator, which checks whether the Grouper class
    instance contains a group with the desired key.

    Finally, the Grouper class instance must allow getting group elements by
    key.

    In this case, the group elements must be represented as a list, and
    the elements in the list must be arranged in the order in which they were
    added.

NOTE:
    The instance of the Grouper class must not depend on the iterable object
    on which it was created.

    In other words, if the original iterable object changes, the instance
    of the Grouper class must not change.

    The implementation of the Grouper class can be arbitrary, that is,
    there are no requirements for the presence of certain attributes.

    Additional data validation in methods is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from collections import defaultdict
from typing import Any, Callable, Iterable, Iterator, Tuple, List


class Grouper:
    """
    A class that groups elements of an iterable based on a key function.
    """

    def __init__(self, iterable: Iterable, key: Callable[[Any], Any]) -> None:
        """
        Initialize with an iterable and a key function.

        Args:
            iterable: Iterable object whose elements are to be grouped.
            key: Function that determines the group key for each element.
        """
        self._groups = defaultdict(list)
        self._key = key
        for item in iterable:
            self.add(item)

    def add(self, obj: Any) -> None:
        """
        Add an object to the corresponding group.

        Args:
            obj: Object to be added to a group based on the key function.
        """
        self._groups[self._key(obj)].append(obj)

    def group_for(self, obj: Any) -> Any:
        """
        Return the group key for an object.

        Args:
            obj: Object to determine the group key for.

        Returns:
            Any: The key of the group the object belongs to.
        """
        return self._key(obj)

    def __len__(self) -> int:
        """
        Return the number of groups.

        Returns:
            int: The number of groups.
        """
        return len(self._groups)

    def __iter__(self) -> Iterator[Tuple[Any, List[Any]]]:
        """
        Yield groups as tuples of (key, elements).

        Yields:
            Tuple[Any, List[Any]]: A tuple containing the group key and a list
                                   of elements in the order they were added.
        """
        for key, elements in self._groups.items():
            yield (key, elements)

    def __contains__(self, key: Any) -> bool:
        """
        Check if a group with the given key exists.

        Args:
            key: Group key to check.

        Returns:
            bool: True if the group exists, False otherwise.
        """
        return key in self._groups

    def __getitem__(self, key: Any) -> List[Any]:
        """
        Get the list of elements for a group key.

        Args:
            key: Group key.

        Returns:
            List[Any]: List of elements in the group, in the order they were
                       added.

        Raises:
            KeyError: If the group key does not exist.
        """
        return self._groups[key]
