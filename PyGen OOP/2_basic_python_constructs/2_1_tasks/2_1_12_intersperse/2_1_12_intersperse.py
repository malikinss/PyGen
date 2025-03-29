'''
TODO:
    Implement a generator function intersperse() that takes two arguments in
    the following order:
        - iterable — the iterable
        - delimiter — the delimiter value

    The function should return a generator that produces a sequence of
    elements of the iterable, with the delimiter value between them.

NOTE:
    Consider the first test, in which the iterable is a list of numbers from 1
    to 3, and the delimiter value is 0.

    The sequence produced by the generator consists of the numbers 1, 2, and 3,
    with the number 0 between them:
        1 0 2 0 3
'''


def intersperse(iterable, delimiter):
    """
    A generator function that yields elements from the iterable,
    interspersed with a delimiter value.

    Args:
        iterable (iterable): The iterable to process.
        delimiter: The delimiter to place between the elements.

    Yields:
        elements: The elements of the iterable with the delimiter between them.
    """
    it = iter(iterable)
    try:
        yield next(it)

        for element in it:
            yield delimiter
            yield element
    except StopIteration:
        pass
