'''
TODO:
    The program is given one number n as input.
    Write a program that outputs a list consisting of n letters of the
    English alphabet ['a', 'b', 'c', ...] in lowercase.
'''
import string


def generate_alphabet_list(n: int) -> list:
    """
    Generates a list of the first 'n' lowercase letters
    of the English alphabet.

    Args:
        n (int): The number of letters to include from the alphabet.

    Returns:
        list: A list containing the first 'n' letters of the alphabet.
    """
    return list(string.ascii_lowercase[:n])


# Read input, generate the list, and print it
n = int(input())
print(generate_alphabet_list(n))
