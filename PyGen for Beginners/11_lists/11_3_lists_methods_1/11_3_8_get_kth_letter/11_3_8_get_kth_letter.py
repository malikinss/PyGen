'''
TODO:
    The input to the program is a natural number n and n lines,
    and then the number k.

    Write a program that prints the kth letter from the input strings
    on one line without spaces.
'''
from typing import List


def get_kth_letter(n: int, strings: List[str], k: int) -> str:
    """
    This function returns the concatenated kth letter from each string
    in the list.

    Args:
    n (int): The number of strings.
    strings (List[str]): A list of n strings.
    k (int): The index (1-based) of the letter to extract from each string.

    Returns:
    str: A string of concatenated kth letters from each string.
    """
    result = ''
    for current_string in strings:
        if len(current_string) >= k:
            result += current_string[k - 1]
    return result


# Input
n = int(input())
given_list = [input() for _ in range(n)]  # Reading n lines of input
k = int(input())  # Reading the index of the letter to extract

# Call the function and print the result
print(get_kth_letter(n, given_list, k))
