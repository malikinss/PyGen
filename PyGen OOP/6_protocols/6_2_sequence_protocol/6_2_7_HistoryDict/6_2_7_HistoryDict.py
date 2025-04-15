'''
TODO:
    Implement a HistoryDict class that describes a dictionary that remembers
    previous values for each key.

    When instantiated, the class must accept one argument:
        data — a dictionary that defines the initial set of elements of
               the HistoryDict instance.
               If not passed, the initial set of elements is considered empty

    The HistoryDict class must have five instance methods:
        keys() — a method that returns an iterable whose elements are the keys
                 of the HistoryDict instance
        values() — a method that returns an iterable whose elements are
                   the values of the keys of the HistoryDict instance
        items() — a method that returns an iterable whose elements are
                  the elements of the HistoryDict instance as tuples:
                    (<key>, <value>)
        history() — a method that takes a key as an argument and returns
                    a list whose elements are all the values that have ever
                    been contained in the HistoryDict instance for
                    the specified key.
                    If the given key is not contained in the HistoryDict
                    instance (it was deleted or never added), the method must
                    return an empty list
        all_history() — a method that returns a dictionary whose keys are
                        the keys of the HistoryDict instance, and whose values
                        are lists containing all the values that have ever
                        been contained by these keys.
                        If any key has been deleted from the HistoryDict
                        instance, then its history is considered to have been
                        deleted as well.

    When passing an instance of the HistoryDict class to the len() function,
    the number of elements in it must be returned.

    Also, an instance of the HistoryDict class must be an iterable object,
    that is, it must allow iterating over its keys, for example, using a for
    loop.

    Finally, an instance of the HistoryDict class must allow getting and
    changing the values of its elements by their keys, adding new pairs
    (key, value) and deleting existing ones.

NOTE:
    An instance of the HistoryDict class must not depend on the dictionary on
    which it was created.

    In other words, if the original dictionary changes, the instance of
    the HistoryDict class should not change.

    The implementation of the HistoryDict class can be arbitrary, i.e. there
    are no requirements for the presence of certain attributes.

    Additional data validation in methods is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple


class HistoryDict:
    """
    A dictionary that remembers all previous values for each key.
    """

    def __init__(self, data: Optional[Dict[Any, Any]] = None) -> None:
        """
        Initialize with an optional dictionary.

        Args:
            data: Initial key-value pairs (default is None, creating
                  an empty dict).
        """
        self._dict = {} if data is None else dict(data)
        self._history = {key: [value] for key, value in self._dict.items()}

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

    def history(self, key: Any) -> List[Any]:
        """
        Return the list of all values ever associated with a key.

        Args:
            key: The key to query.

        Returns:
            List[Any]: List of values for the key, or empty list if key
                       never existed.
        """
        return self._history.get(key, [])

    def all_history(self) -> Dict[Any, List[Any]]:
        """
        Return a dictionary of histories for all current keys.

        Returns:
            Dict[Any, List[Any]]: Dictionary mapping current keys to their
                                  value histories.
        """
        return self._history

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
        Get the current value for a key.

        Args:
            key: The key to look up.

        Returns:
            Any: The current value associated with the key.

        Raises:
            KeyError: If the key does not exist.
        """
        return self._dict[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set a key-value pair, updating history.

        Args:
            key: The key to set.
            value: The value to associate.
        """
        self._dict[key] = value
        self._history.setdefault(key, []).append(value)

    def __delitem__(self, key: Any) -> None:
        """
        Remove a key-value pair and its history.

        Args:
            key: The key to remove.

        Raises:
            KeyError: If the key does not exist.
        """
        del self._dict[key]
        self._history.pop(key, None)
