'''
TODO:
    The program is given one number n as input.
    Write a program that outputs the list [1, 2, 3, ..., n].
'''


def create_number_list(n: int) -> list:
    """
    Creates a list of integers from 1 to n (inclusive).

    Args:
        n (int): The upper limit of the list.

    Returns:
        list: A list containing integers from 1 to n.
    """
    return list(range(1, n + 1))


# Read input, generate the list, and print it
n = int(input())
print(create_number_list(n))
