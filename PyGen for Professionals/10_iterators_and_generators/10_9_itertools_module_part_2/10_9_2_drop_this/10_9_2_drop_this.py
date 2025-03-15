'''
TODO:
    Implement a drop_this() function that takes two arguments in the following
    order:
        iterable — an iterable
        obj — an arbitrary object

    The function must return an iterator that generates a sequence of elements
    of the iterable, starting with an element that is not equal to obj.

NOTE:
    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import dropwhile
from typing import Iterable, Iterator, Any


def drop_this(iterable: Iterable[Any], obj: Any) -> Iterator[Any]:
    """
    Skip all leading occurrences of obj and return an iterator
    starting from the first non-matching element.

    Args:
        iterable (Iterable[Any]): An iterable containing elements.
        obj (Any): The object to skip at the beginning of the iterable.

    Returns:
        Iterator[Any]: An iterator that yields elements from the first
        non-matching element onward.

    Example:
        >>> list(drop_this([0, 0, 1, 2, 3], 0))
        [1, 2, 3]
        >>> list(drop_this(['a', 'a', 'b', 'c'], 'a'))
        ['b', 'c']
        >>> list(drop_this([None, None, 42], None))
        [42]
    """
    yield from dropwhile(lambda x: x is obj, iterable)
