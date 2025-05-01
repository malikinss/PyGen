'''
TODO:
    Implement a Queue class that describes a queue whose elements
    are key:value pairs.

    When instantiated, the class must accept one argument:
        pairs — a list or dictionary that specifies the initial set
                of elements in the queue.
                The order of the elements in the queue must match their order
                in the passed iterable.
                If not passed, the queue is considered empty

    The Queue class must have two instance methods:
        add() — a method that takes an element as an argument and adds it to
                the end of the queue.
                The element in this case is a two-element tuple containing
                the key and value.
                If the queue already contains an element with the specified
                key, it must be moved to the end of the queue and its value
                must be updated
        pop() — a method that removes the first element from the queue and
                returns it.
                The element in this case is a two-element tuple containing
                the key and value.
                If the queue is empty, a KeyError exception should be raised
                with the text:
                    The queue is empty

    An instance of the Queue class should have the following formal string
    representation:
        Queue(
            [
                (<key of the 1st element>, <value of the 1st element>),
                (<key of the 2nd element>, <value of the 2nd element>),
                ...
            ]
        )

    When passing an instance of the Queue class to the len() function,
    the number of elements in it should be returned.

NOTE:
    It will probably be convenient to use one of the classes from
    the collections module when solving this problem.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Queue class,
    it can be arbitrary.
'''
from collections import deque
from collections.abc import Iterable
from typing import Any, Tuple


class Queue:
    """
    Queue of key:value pairs.
    """

    def __init__(
        self,
        pairs: Iterable[Tuple[Any, Any]] | dict | None = None
    ) -> None:
        """
        Init queue.

        Args:
            pairs: Initial key:value pairs or dict, defaults to empty.
        """
        self._queue = deque()
        if pairs:
            if isinstance(pairs, dict):
                pairs = pairs.items()
            self._queue.extend(pairs)

    def add(self, item: Tuple[Any, Any]) -> None:
        """
        Add or update key:value pair.

        Args:
            item: Tuple of (key, value).
        """
        key = item[0]
        for i, (k, _) in enumerate(self._queue):
            if k == key:
                self._queue.rotate(-i)
                self._queue.popleft()
                self._queue.rotate(i)
                break
        self._queue.append(item)

    def pop(self) -> Tuple[Any, Any]:
        """
        Remove and return first pair.

        Returns:
            Tuple: First (key, value).

        Raises:
            KeyError: If queue is empty.
        """
        if not self._queue:
            raise KeyError("The queue is empty")
        return self._queue.popleft()

    def __repr__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format Queue([(key1, value1), ...]).
        """
        return f"Queue({list(self._queue)!r})"

    def __len__(self) -> int:
        """
        Get queue length.

        Returns:
            int: Number of pairs.
        """
        return len(self._queue)
