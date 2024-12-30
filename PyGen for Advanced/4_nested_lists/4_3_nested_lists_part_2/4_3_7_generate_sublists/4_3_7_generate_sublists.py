'''
TODO:
    A sublist is a part of another list.

    A sublist can contain one element, several elements, or even none.

    For example, [1], [2], [3], and [4] are sublists of the list [1, 2, 3, 4].

    The list [2, 3] is a sublist of the list [1, 2, 3, 4], but the list [2, 4]
    is not a sublist of the list [1, 2, 3, 4], because elements 2 and 4 in
    the second list are not adjacent (they are broken by element 3).

    The empty list is a sublist of any list.

    The list itself is a sublist of itself, that is, the list [1, 2, 3, 4]
    is a sublist of the list [1, 2, 3, 4].

    The program is given a string of text containing characters.

    A list is formed from this string.

    Write a program that outputs a list containing all possible sublists
    of the list, including the empty list.

NOTE:
    The order of lists of the same length must match the order in which they
    appear in the main list.
'''
from typing import List


def generate_sublists(lst: List[str]) -> List[List[str]]:
    """
    Generates all possible contiguous sublists of the given list,
    including the empty list.

    Args:
        lst (List[str]): The list to generate sublists from.

    Returns:
        List[List[str]]: A list containing all possible sublists
                         of the input list.
    """
    result: List[List[str]] = [[]]  # Start with the empty list as a sublist
    for i in range(len(lst)):
        # j should go from i+1 to len(lst) to include all sublists
        for j in range(i + 1, len(lst) + 1):
            result.append(lst[i:j])
    return result


# Input
lst: List[str] = input().split()

# Output the generated sublists
print(generate_sublists(lst))
