'''
TODO:
    It was required to implement a function get_max_index() that takes a list
    of distinct integers as an argument and returns the index of the largest
    number from this list (starting with 0).

    The programmer was in a hurry and implemented the function incorrectly.

    Find and fix all the errors made in the implementation of this function
    (there are exactly 4 of them).
NOTE:
    It is known that each error affects only one string and can be corrected
    without changing other strings.
'''


# original code
def get_max_inex(numbers):
    max_index = 0
    max_value = numbers[-1]

    for index, value in enumerate(numbers, 1):
        if index > max_index:
            max_index = index
            max_value = value

    return max_value


def get_max_index(numbers: list[int]) -> int:
    """
    Returns the index of the largest number in the given list.

    Args:
        numbers (list[int]): A list of distinct integers.

    Returns:
        int: The index of the largest number in the list.
    """
    return numbers.index(max(numbers))
