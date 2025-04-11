'''
TODO:
    Implement a Filter class that describes an object for filtering elements
    of iterable objects.

    When instantiated, the class must accept one argument:
        predicate — a predicate function; if None, it works like
                    the bool() function

    An instance of the Filter class must be a callable object and accept
    one argument:
        iterable — an iterable object

    An instance of the Filter class must return a list whose elements are
    the elements of the iterable object iterable for which the predicate
    function returned True.

NOTE:
    A predicate is a function that returns True or False depending on
    the value passed as an argument.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Filter class,
    it can be arbitrary.
'''
from typing import Optional, Callable, Any, Iterable


class Filter:
    """
    A class for filtering elements of iterable objects based on a predicate.
    """

    def __init__(self, predicate: Optional[Callable[[Any], bool]]) -> None:
        """
        Initialize Filter with a predicate function.

        Args:
            predicate (Callable[[Any], bool] | None): A function that returns
                                                      True or False for
                                                      a given argument.
                                                      If None, uses the bool()
                                                      function.
        """
        self.predicate = bool if predicate is None else predicate

    def __call__(self, iterable: Iterable) -> list:
        """
        Filter elements of an iterable based on the predicate.

        Args:
            iterable (Iterable): An iterable object to filter.

        Returns:
            list: A list of elements for which the predicate returns True.
        """
        return [element for element in iterable if self.predicate(element)]
