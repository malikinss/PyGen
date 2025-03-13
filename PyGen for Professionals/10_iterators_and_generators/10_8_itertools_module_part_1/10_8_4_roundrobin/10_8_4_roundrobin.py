'''
TODO:
    Implement a roundrobin() function that takes an arbitrary number of
    positional arguments, each of which is an iterable.

    The function must return an iterator that generates a sequence of the
    elements of all the iterables passed in:
        first the first element of the first iterable,
        then the first element of the second iterable,
        and so on;

        then the second element of the first iterable,
        then the second element of the second iterable,
        and so on.

NOTE:
    The elements of the iterables in the iterator returned by the function
    must be in their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''

from typing import Iterable, Iterator, Any


def roundrobin(*iterables: Iterable[Any]) -> Iterator[Any]:
    """
    Round-robin over multiple iterables.

    Args:
        *iterables (Iterable[Any]): Arbitrary number of iterables to be
        processed.

    Returns:
        Iterator[Any]: An iterator that yields elements from each iterable
        in a round-robin fashion, preserving their original order.

    Example:
        >>> list(roundrobin([1, 2], ['a', 'b'], [True, False]))
        [1, 'a', True, 2, 'b', False]
    """
    iterators = [iter(it) for it in iterables]

    while iterators:
        for current_iter in iterators[:]:
            try:
                yield next(current_iter)
            except StopIteration:
                iterators.remove(current_iter)
                if not iterators:
                    break
