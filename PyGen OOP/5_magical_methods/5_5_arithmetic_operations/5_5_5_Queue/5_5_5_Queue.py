'''
TODO:
    Queue is an abstract data type with first-in-first-out access discipline.

    An element can only be added to the end of the queue, and a selection can
    only be made from the beginning of the queue, with the selected element
    being removed from the queue.

    Implement a Queue class that describes a queue.

    When instantiated, the class must accept an arbitrary number of positional
    arguments, each of which is an element of the queue.

    The order of the arguments forms the order of the elements in the queue,
    i.e. the first argument is the first element of the queue, the second
    argument is the second element of the queue, and so on.

    The Queue class must have two instance methods:
        - add() is a method that accepts an arbitrary number of positional
          arguments and adds them to the end of the queue in the order in
          which they were passed
        - pop() is a method that removes the first element from the queue and
          returns it.
          If the queue is empty, the method must return None

    An instance of the Queue class must have the following informal string
    representation:
        <first element of the queue> ->
        <second element of the queue> ->
        <third element of the queue> -> ...

    In addition, instances of the Queue class must support comparison
    operations between themselves using the == and != operators.

    Two queues are considered equal if they have equal length and contain
    equal elements in equal positions.

    Also, instances of the Queue class must support the operation of addition
    with the + and += operators:
        - the result of addition with the + operator must be a new instance of
          the Queue class, representing the queue with all the elements of
          the original queues: first all the elements of the left queue, then
          all the elements of the right queue
        - the result of addition with the += operator must be the left
          instance of the Queue class, representing the queue to which all
          the elements of the right queue are added

    Finally, an instance of the Queue class must support the operation of
    bitwise shifting to the right by an integer n using the >> operator,
    the result of which must be a new instance of the Queue class,
    representing the original queue without the first n elements.

    If n is greater than or equal to the length of the original queue,
    the result must be an instance of the Queue class, representing an empty
    queue.

NOTE:
    If the object with which the comparison or arithmetic operation is
    performed is invalid, the method implementing this operation must return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the Queue class,
    it can be arbitrary.
'''


from typing import Any, Union


class Queue:
    """
    A class representing a queue with first-in-first-out access.
    """

    def __init__(self, *args: Any) -> None:
        """
        Initialize Queue with an arbitrary number of elements.

        Args:
            *args: Elements to add to the queue in the order they are passed.
        """
        self.elements = list(args)

    def __str__(self) -> str:
        """
        Informal string representation of the Queue.

        Returns:
            str: Elements separated by ' -> ', e.g., '1 -> 2 -> 3'.
        """
        return " -> ".join(map(str, self.elements))

    def add(self, *args: Any) -> None:
        """
        Add elements to the end of the queue.

        Args:
            *args: Elements to append in the order they are passed.
        """
        self.elements.extend(args)

    def pop(self) -> Any:
        """
        Remove and return the first element from the queue.

        Returns:
            Any: The first element, or None if the queue is empty.
        """
        if self.elements:
            return self.elements.pop(0)
        return None

    def __eq__(self, other: 'Queue') -> 'Union[bool, NotImplemented]':
        """
        Compare two Queue instances for equality.

        Args:
            other (Queue): Another Queue instance to compare.

        Returns:
            bool: True if queues have equal length and elements,
                  False otherwise.
            NotImplemented: If other is not a Queue instance.
        """
        if isinstance(other, Queue):
            return self.elements == other.elements
        return NotImplemented

    def __add__(self, other: 'Queue') -> 'Union[Queue, NotImplemented]':
        """
        Add two Queue instances.

        Args:
            other (Queue): Another Queue instance to append.

        Returns:
            Queue: New instance with elements of both queues.
            NotImplemented: If other is not a Queue instance.
        """
        if isinstance(other, Queue):
            return Queue(*(self.elements + other.elements))
        return NotImplemented

    def __iadd__(self, other: 'Queue') -> 'Union[Queue, NotImplemented]':
        """
        In-place addition of another Queue instance.

        Args:
            other (Queue): Another Queue instance to append.

        Returns:
            Queue: Self with elements of other appended.
            NotImplemented: If other is not a Queue instance.
        """
        if isinstance(other, Queue):
            self.elements.extend(other.elements)
            return self
        return NotImplemented

    def __rshift__(self, n: int) -> 'Union[Queue, NotImplemented]':
        """
        Shift queue right by n, removing first n elements.

        Args:
            n (int): Number of elements to remove from the start.

        Returns:
            Queue: New instance without the first n elements, or empty
                   if n >= length.
            NotImplemented: If n is not an integer.
        """
        if isinstance(n, int):
            if n >= len(self.elements):
                return Queue()
            return Queue(*self.elements[n:])
        return NotImplemented
