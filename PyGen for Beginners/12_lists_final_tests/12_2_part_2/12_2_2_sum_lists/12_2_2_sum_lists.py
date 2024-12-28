'''
TODO:
    The input to the program is two lines of text containing integers.

    Lists of numbers L and M are formed from these strings.

    Write a program that creates a third list whose elements are the sums
    of the corresponding elements of the lists L and M.

    Then the program should display each element of the resulting list
    on one line, separated by 1 space.
'''
from typing import List


def sum_lists(lst1: List[int], lst2: List[int]) -> List[int]:
    """
    Takes two lists of integers and returns a list containing the sum
    of corresponding elements from both lists.

    Args:
        l (List[int]): The first list of integers.
        m (List[int]): The second list of integers.

    Returns:
        List[int]: A list containing the sums of corresponding elements.
    """
    return [lst1[i] + lst2[i] for i in range(len(lst1))]


# Input two lines of integers
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

# Get the resulting list by summing corresponding elements
result = sum_lists(line1, line2)

# Output each element of the resulting list on a new line, separated by spaces
print(*result)
