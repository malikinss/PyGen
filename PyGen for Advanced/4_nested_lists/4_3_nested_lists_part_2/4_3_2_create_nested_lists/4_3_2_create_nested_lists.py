'''
TODO:
    The input to the program is a number n.

    Write a program that creates and outputs a line-by-line nested list
    consisting of n lists [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]]
'''
from typing import List


def create_nested_lists(n: int) -> List[List[int]]:
    """
    Creates a list of lists where each sublist contains integers from 1
    to the index of the sublist.

    Args:
        n (int): The number of sublists and the maximum integer in the final
                 sublist.

    Returns:
        List[List[int]]: A list of lists, where each sublist contains integers
                         from 1 up to the sublist's index.
    """
    lst2 = []
    for i in range(1, n + 1):
        lst2.append(list(range(1, i + 1)))

    return lst2


# Example usage
n = int(input())
result = create_nested_lists(n)
for sublist in result:
    print(sublist)
