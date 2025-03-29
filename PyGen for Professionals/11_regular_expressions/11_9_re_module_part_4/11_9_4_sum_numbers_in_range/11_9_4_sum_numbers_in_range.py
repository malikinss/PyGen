'''
TODO:
    Write a program that adds up all the natural numbers in a string that are
    in the specified index range.

    The program first receives two integers a and b, greater than or equal to
    0, separated by a space, and then a string.

    The program should output the sum of all the natural numbers in the input
    string that are in the index range from a (inclusive) to b (exclusive).

    If there are no numbers in the specified range,
    the program should output 0.
'''
import re


def sum_numbers_in_range(string: str, start: int, end: int) -> int:
    """
    Extracts natural numbers from the specified substring (from start to end)
    and returns their sum.

    Args:
        string (str): The input string containing natural numbers.
        start (int): The starting index of the range (inclusive).
        end (int): The ending index of the range (exclusive).

    Returns:
        int: The sum of natural numbers found in the specified range.
    """
    numbers = re.findall(r'\d+', string[start:end])
    return sum(map(int, numbers))


start, end = map(int, input().split())
string = input()
print(sum_numbers_in_range(string, start, end))
