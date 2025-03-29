'''
TODO:
    Implement a quantify() function that takes two arguments in the following
    order:
        - iterable — the iterable
        - predicate — the predicate function, i.e. a function that returns
                      True or False.

    If it has a value of None, then it works similarly to the bool() function

    The quantify() function should count for how many elements of the iterable
    the predicate function predicate returned True, and return the result.

NOTE:
    Consider the first test, in which a list of numbers from 1 to 10 is passed
    as the iterable, and a function that returns True if the argument is
    greater than one, or False otherwise, is passed as the predicate function.

    The passed list of numbers contains exactly 9 numbers greater than one.
'''


def quantify(iterable, predicate=None):
    """
    Counts how many elements in the iterable satisfy the condition of the
    predicate.

    Args:
        iterable (iterable): The iterable to check.
        predicate (function, optional): A function that returns a boolean.
        Defaults to None.

    Returns:
        int: The number of elements that satisfy the condition.
    """
    if predicate is None:
        predicate = bool

    return sum(1 for item in iterable if predicate(item))
