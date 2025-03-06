'''
TODO:
    As you know, when iterating over a dictionary, we get keys, not values
    or key-value pairs.

    The code below:
        info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
        print(*info)
    outputs:
        name age gender

    Implement a DictItemsIterator class that produces iterators whose
    constructor takes one argument:
        data — dictionary

    The iterator of the DictItemsIterator class must produce a sequence of
    tuples representing key-value pairs of the data dictionary, and then raise
    a StopIteration exception.

NOTE:
    When solving this problem, do not use the keys(), values(), and items()
    dictionary methods.

    The key-value pairs in the iterator returned by the function must be
    in their original order.
'''
from typing import Dict, Tuple


class DictItemsIterator:
    """
    Iterator that iterates over the key-value pairs of a dictionary.

    The iterator generates tuples representing key-value pairs from the given
    dictionary, without using the `items()`, `keys()`, or `values()` methods.

    Args:
        data (dict): The dictionary to iterate over.

    Raises:
        StopIteration: When the iteration over all key-value pairs is complete.
    """

    def __init__(self, data: Dict):
        """
        Initializes the iterator with the given dictionary.

        Args:
            data (dict): The dictionary to iterate over.
        """
        self.data = data

        # List of keys to maintain insertion order
        self.keys = list(data)

        # Start before the first key
        self.index = -1

    def __iter__(self) -> 'DictItemsIterator':
        """
        Returns the iterator object itself.

        Returns:
            DictItemsIterator: The iterator instance.
        """
        return self

    def __next__(self) -> Tuple:
        """
        Returns the next key-value pair from the dictionary as a tuple.

        If there are no more key-value pairs, raises StopIteration.

        Returns:
            Tuple: A tuple (key, value) for the next key-value pair.

        Raises:
            StopIteration: When all key-value pairs have been iterated over.
        """
        self.index += 1

        # If we've iterated over all the keys, stop the iteration
        if self.index >= len(self.data):
            raise StopIteration

        key = self.keys[self.index]
        value = self.data[key]

        return key, value
