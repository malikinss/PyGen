'''
TODO:
    The input to the program is a number n.

    Write a program that creates and outputs line by line a list consisting of
    n lists [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
'''
from typing import List


def create_lists(n: int) -> List[List[int]]:
    """
    Creates a list of lists where each sublist contains integers from 1 to n.

    Args:
        n (int): The number of sublists and the range of integers in each
        sublist.

    Returns:
        List[List[int]]: A list of lists, each containing integers from 1 to n.
    """
    lst2 = []
    for _ in range(n):
        lst2.append(list(range(1, n+1)))

    return lst2


# Example usage
n = int(input())
result = create_lists(n)

for sublist in result:
    print(sublist)
