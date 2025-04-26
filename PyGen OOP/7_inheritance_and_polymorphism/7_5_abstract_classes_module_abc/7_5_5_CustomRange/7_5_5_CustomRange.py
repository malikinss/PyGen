'''
TODO:
    Let's call a range a notation of two non-negative integers separated by
    a hyphen a-b, where a is the left end of the range, b is the right end of
    the range, and a <= b.

    A range contains all numbers from a to b inclusive.

    For example, the range 1-4 contains the numbers 1, 2, 3, and 4.

    Implement a CustomRange class that describes a sequence whose elements are
    single integers and numbers from certain ranges.

    When creating an instance, the class must accept an arbitrary number
    of positional arguments, each of which is a single integer or a range.

    When passing an instance of the CustomRange class to the len() function,
    the number of elements in it must be returned.

    When passing an instance of the CustomRange class to the reversed()
    function, an iterator must be returned whose elements are the elements of
    the passed instance of the CustomRange class, arranged in reverse order.

    An instance of the CustomRange class must be an iterable object, i.e. it
    must allow iterating over its elements, for example, using a for loop.

    In addition, an instance of the CustomRange class must support
    the membership check operation using the in operator.

    Finally, an instance of the CustomRange class must allow iterating over
    its elements using indexes, both positive and negative

NOTE:
    Before making a decision, think about which abstract class from
    the collections.abc module would be convenient as a parent.

    The implementation of the CustomRange class can be arbitrary,
    i.e. there are no requirements for the presence of certain attributes.

    Additional data validation in methods is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from collections.abc import Sequence
from typing import Any, Union


class CustomRange(Sequence):
    """
    Sequence of integers from single numbers and ranges (e.g., 'a-b').

    Supports iteration, indexing, length, membership testing, and reversal.
    """

    def __init__(self, *args: Any) -> None:
        """
        Initialize with integers or range strings (e.g., 'a-b').

        Args:
            *args: Integers or strings representing ranges (e.g., '1-4').
        """
        self.data = []
        for arg in args:
            if isinstance(arg, str):
                start, end = map(int, arg.split('-'))
                self.data.extend(range(start, end + 1))
            else:  # Assumes int (per specification)
                self.data.append(arg)

    def __len__(self) -> int:
        """
        Return the number of elements in the sequence.

        Returns:
            int: Total number of integers.
        """
        return len(self.data)

    def __getitem__(self, key: Union[int, slice]) -> Any:
        """
        Get element or slice by index.

        Args:
            key: Integer index or slice.

        Returns:
            Element or subsequence.
        """
        return self.data[key]
