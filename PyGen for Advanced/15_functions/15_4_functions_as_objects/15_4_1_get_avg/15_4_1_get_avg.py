'''
TODO:
    Given a list numbers, containing tuples of numbers, write a program that
    uses the built-in functions min() and max() to print those tuples (each on
    a separate line) that have the minimum and maximum arithmetic mean
    of their elements.

NOTE:
    Use the optional argument key.
'''


def get_avg(sequence: tuple[int, ...]) -> float:
    """
    Calculates the arithmetic mean of a tuple of numbers.

    Args:
        sequence (tuple[int, ...]): A tuple containing numeric values.

    Returns:
        float: The arithmetic mean of the numbers in the tuple.
    """
    return sum(sequence) / len(sequence)


numbers = [
    (10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100),
    (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65),
    (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)
]

# Printing the tuple with the minimum arithmetic mean
print(min(numbers, key=get_avg))

# Printing the tuple with the maximum arithmetic mean
print(max(numbers, key=get_avg))
