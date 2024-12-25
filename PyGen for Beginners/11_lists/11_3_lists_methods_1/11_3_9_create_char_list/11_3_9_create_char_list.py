'''
TODO:
    The input to the program is a natural number n,
    and then n strings.

    Write a program that creates a list of characters from all
    strings and then prints it out.
'''
from typing import List


def create_char_list(n: int, strings: List[str]) -> List[str]:
    """
    This function creates a list of characters by combining all the characters
    from the given strings and returns the list.

    Args:
    n (int): The number of strings.
    strings (List[str]): A list of strings.

    Returns:
    List[str]: A list containing all characters from all the strings.
    """
    char_list: List[str] = []
    for string in strings:
        char_list.extend(string)  # Adding each character from the string
    return char_list


# Input
n = int(input())
strings = [input() for _ in range(n)]  # Reading n lines of input

# Call the function and print the result
result = create_char_list(n, strings)
print(result)
