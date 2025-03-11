'''
TODO:
    Implement a generator function that takes two arguments in the following
    order:
        iterable — an iterable
        obj — an arbitrary object

    The function must return a generator that produces a sequence of elements
    of iterable until it reaches an element equal to obj.

    If iterable does not contain any elements equal to obj, the generator must
    produce all elements of iterable.

NOTE:
    The elements of iterable in the generator returned by the function must be
    in their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from typing import Iterable, Generator, Any


def stop_on(iterable: Iterable[Any], obj: Any) -> Generator[Any, None, None]:
    """
    Generate elements from an iterable until the specified object
    is encountered.

    This function produces elements from the iterable one by one, and stops
    when the specified stop_element is found.

    If the stop_element is not in the iterable, the generator will return all
    elements.

    Args:
        iterable (Iterable): The input iterable (e.g., list, string, etc.).
        stop_element (Any): The object that will stop the iteration.

    Yields:
        The elements of the iterable until stop_element is encountered.
    """
    for cur_obj in iterable:
        if cur_obj == obj:
            break
        yield cur_obj
