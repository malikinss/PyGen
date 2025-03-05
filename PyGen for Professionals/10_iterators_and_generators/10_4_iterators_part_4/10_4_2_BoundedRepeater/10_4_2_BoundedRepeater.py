'''
TODO:
    Implement a BoundedRepeater class that produces iterators whose
    constructor takes two arguments in the following order:
        - obj is an arbitrary object
        - times is a natural number

    The iterator of the BoundedRepeater class must produce the value obj times
    and then throw a StopIteration exception.
'''
from typing import Any, Iterator


class BoundedRepeater:
    """
    An iterator that repeats a given object a specified number of times.

    Args:
        obj (Any): The object to be repeatedly returned.
        times (int): The number of times the object should be returned.

    Methods:
        __iter__() -> Iterator[Any]: Returns the iterator itself.
        __next__() -> Any: Returns the stored object until the specified count
        is reached, then raises StopIteration.

    Example:
        repeater = BoundedRepeater("Hello", 3)
        print(list(repeater))  # Output: ['Hello', 'Hello', 'Hello']
    """

    def __init__(self, obj: Any, times: int) -> None:
        self.obj: Any = obj
        self.times: int = times
        self.counter: int = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.counter >= self.times:
            raise StopIteration
        self.counter += 1
        return self.obj
