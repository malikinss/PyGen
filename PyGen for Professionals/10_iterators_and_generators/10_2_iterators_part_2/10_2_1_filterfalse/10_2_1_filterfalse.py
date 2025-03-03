'''
TODO:
    Implement the filterfalse() function using the filter() function, which
    takes two arguments:
        predicate — the predicate function; if None, it works like bool()
        iterable — the iterable

    The function should work in the opposite way to filter(), that is, it
    should return an iterator whose elements are the elements of the iterable
    for which the predicate returned False.

NOTE:
    A predicate is a function that returns True or False depending on the
    value passed as an argument.

    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from typing import Callable, Iterable, Iterator, Optional, Any


def filterfalse(predicate: Optional[Callable[[Any], bool]],
                iterable: Iterable[Any]) -> Iterator[Any]:
    """
    Filters elements from the iterable for which the predicate returns False.

    Args:
        predicate (Optional[Callable[[Any], bool]]): A function that returns a
        boolean value.
        iterable (Iterable[Any]): An iterable object containing elements to
        be filtered.

    Returns:
        Iterator[Any]: An iterator with elements for which the
        predicate returned False.
    """
    if predicate is None:
        predicate = bool

    return filter(lambda x: not predicate(x), iterable)


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))
