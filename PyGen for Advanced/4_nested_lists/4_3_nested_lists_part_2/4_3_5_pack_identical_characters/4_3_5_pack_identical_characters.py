'''
TODO:
    The program is given a text string containing characters as input.

    Write a program that packs sequences of identical characters of a given
    string into sublists.
'''
from typing import List


def pack_identical_characters(s: str):
    """
    Packs sequences of identical characters of a given string into sublists.

    Args:
        s (str): The input string containing characters.

    Returns:
        List[List[str]]: A list of lists where each sublist contains identical
                         characters.
    """
    lst: List = []
    if not s:  # If the string is empty, return an empty list
        return lst

    # Initialize the first sublist with the first character
    lst.append([s[0]])

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # If the current character is the same
        # as the last one in the current sublist
        if s[i] == s[i-1]:
            lst[-1].append(s[i])
        else:
            lst.append([s[i]])  # Otherwise, start a new sublist

    return lst


# Input and output
s = input()  # Read the input string
result = pack_identical_characters(s)  # Get the result
print(result)
