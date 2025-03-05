'''
TODO:
    Implement a Repeater class that generates iterators, the constructor of
    which takes one argument:
        obj — an arbitrary object

    The iterator of the Repeater class must infinitely generate a single
    value — obj.

NOTE:
    Submit a program containing only the required Repeater class to
    the testing system.
'''


class Repeater:
    """
    An iterator that infinitely generates a single value.

    Args:
        obj (Any): The object to be repeatedly returned.

    Methods:
        __iter__(): Returns the iterator itself.
        __next__(): Returns the stored object indefinitely.

    Example:
        repeater = Repeater(42)
        print(next(repeater))  # Output: 42
        print(next(repeater))  # Output: 42
    """

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj
