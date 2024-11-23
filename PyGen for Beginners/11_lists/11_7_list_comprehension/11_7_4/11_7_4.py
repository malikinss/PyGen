'''
TODO:
    Complete the above code using a list expression so that you get a list
    of all palindrome numbers from 100 to 1000.

NOTE:
    The resulting list must consist of integers.
'''
from typing import List


def find_palindromes() -> List[int]:
    """
    Generates a list of all palindrome numbers from 100 to 1000.

    A palindrome is a number that reads the same backward as forward.

    Returns:
        List[int]: A list of palindrome numbers between 100 and 1000.
    """
    return [i for i in range(100, 1001) if str(i) == str(i)[::-1]]


# Calling the function to find and print the palindromes
palindromes = find_palindromes()

print(palindromes)
