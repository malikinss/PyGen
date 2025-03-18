'''
TODO:
    Write a program that prints all permutations of characters in a string
    without duplicates.

    The program is given an arbitrary string of lowercase Latin letters,
    the length of which does not exceed 10 characters.

    The program must output all permutations of characters of this string
    without duplicates in alphabetical order, each on a separate line
'''
from itertools import permutations


def print_unique_permutations(s: str) -> None:
    """
    Prints all unique permutations of characters in a string in
    lexicographical order.

    Args:
        s (str): The input string consisting of lowercase Latin letters.
    """
    for perm in sorted(set(''.join(p) for p in permutations(s))):
        print(perm)


print_unique_permutations(input().strip())
