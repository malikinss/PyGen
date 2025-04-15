'''
TODO:
    Implement a PermaDict class that describes a dictionary that allows adding
    and removing (<key>, <value> pairs), but does not allow changing values
    based on existing keys.

    When instantiated, the class must accept one argument:
        data — a dictionary that defines the initial set of elements of
               the PermaDict instance.
               If not passed, the initial set of elements is considered empty

    The PermaDict class must have three instance methods:
        keys() — a method that returns an iterable whose elements are the keys
                 of the PermaDict instance
        values() — a method that returns an iterable whose elements are
                   the values of the keys of the PermaDict instance
        items() — a method that returns an iterable whose elements are
                  the elements of the PermaDict instance as (<key>, <value>)
                  tuples

    When passing a PermaDict instance to the len() function, the number
    of elements in it must be returned.

    Also, an instance of the PermaDict class must be an iterable object, i.e.
    it must allow iterating over its keys, for example, using a for loop.

    Finally, an instance of the PermaDict class must allow it to obtain
    the values of its elements by their keys, add new pairs (key, value),
    and delete existing ones using the del operator.

    However, changing the values by existing keys must be unavailable,
    and when attempting to perform such an operation, a KeyError exception
    must be raised with the text:
        Changing the value by key is impossible

NOTE:
    An instance of the PermaDict class must not depend on the dictionary on
    which it was created.

    In other words, if the original dictionary changes, the instance of
    the PermaDict class must not change.

    The implementation of the PermaDict class can be arbitrary, i.e. there are
    no requirements for the presence of certain attributes.

    Additional data validation in methods is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Any, Dict, Iterable, Iterator, Optional, Tuple


class PermaDict:
    """
    A dictionary that prevents changing values for existing keys.
    """

    def __init__(self, data: Optional[Dict[Any, Any]] = None) -> None:
        """
        Initialize with an optional dictionary.

        Args:
            data: Initial key-value pairs (default is None, creating an empty
                  dict).
        """
        self._dict = {} if data is None else dict(data)

    def keys(self) -> Iterable[Any]:
        """
        Return an iterable of keys.

        Returns:
            Iterable[Any]: The keys of the dictionary.
        """
        return self._dict.keys()

    def values(self) -> Iterable[Any]:
        """
        Return an iterable of values.

        Returns:
            Iterable[Any]: The values of the dictionary.
        """
        return self._dict.values()

    def items(self) -> Iterable[Tuple[Any, Any]]:
        """
        Return an iterable of key-value pairs.

        Returns:
            Iterable[Tuple[Any, Any]]: The key-value pairs of the dictionary.
        """
        return self._dict.items()

    def __len__(self) -> int:
        """
        Return the number of key-value pairs.

        Returns:
            int: The number of pairs.
        """
        return len(self._dict)

    def __iter__(self) -> Iterator[Any]:
        """
        Yield keys of the dictionary.

        Yields:
            Any: Keys of the dictionary.
        """
        yield from self._dict

    def __getitem__(self, key: Any) -> Any:
        """
        Get the value for a key.

        Args:
            key: The key to look up.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key does not exist.
        """
        return self._dict[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Add a key-value pair, preventing changes to existing keys.

        Args:
            key: The key to set.
            value: The value to associate.

        Raises:
            KeyError: If the key already exists.
        """
        if key in self._dict:
            raise KeyError("Changing the value by key is impossible")
        self._dict[key] = value

    def __delitem__(self, key: Any) -> None:
        """
        Remove a key-value pair.

        Args:
            key: The key to remove.

        Raises:
            KeyError: If the key does not exist.
        """
        del self._dict[key]
