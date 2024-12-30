'''
TODO:
    Complete the code below so that list1 looks like this:
        list1 = [
            [8, 7, 1],
            [102, 7, 9],
            [105, 106, 102],
            [103, 98, 99, 100],
            [3, 2, 1]
        ]
'''
from typing import List


def reverse_nested_lists(list1: List[List[int]]) -> List[List[int]]:
    """
    Reverses each nested list within a list of lists.

    Args:
        list1 (List[List[int]]): A list of nested lists containing integers.

    Returns:
        List[List[int]]: A list of nested lists with each list reversed.
    """
    for li in list1:
        li.reverse()

    return list1


# Example usage
list1 = [
    [1, 7, 8],
    [9, 7, 102],
    [102, 106, 105],
    [100, 99, 98, 103],
    [1, 2, 3]
]

print(reverse_nested_lists(list1))
