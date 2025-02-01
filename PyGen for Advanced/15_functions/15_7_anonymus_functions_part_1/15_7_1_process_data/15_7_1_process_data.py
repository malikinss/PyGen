'''
TODO:
    It was required to write a program that:

        - converts the list floats into a list of numbers squared and rounded
          to one decimal place;
        - filters the list words and leaves only palindromes longer than
          4 characters;
        - finds the product of numbers from the list numbers.

    The programmer was in a hurry and wrote the program incorrectly.
    Improve his program.
'''
from functools import reduce
from typing import List


def is_palindrome(word: str) -> bool:
    """
    Checks if a word is a palindrome and has more than 4 characters.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome and its length is greater
              than 4, otherwise False.
    """
    return word.lower() == word.lower()[::-1] and len(word) > 4


def process_data(
  floats: List[float], words: List[str], numbers: List[int]
) -> tuple[List[float], List[str], int]:
    """
    Processes the given lists of floats, words, and numbers.

    Args:
        floats (List[float]): A list of floating-point numbers.
        words (List[str]): A list of words.
        numbers (List[int]): A list of integers.

    Returns:
        tuple: A tuple containing:
            - A list of squared and rounded floats.
            - A list of palindromes longer than 4 characters.
            - The product of the numbers in the list.
    """
    # Mapping: Squaring and rounding to one decimal place
    map_result = list(map(lambda num: round(num ** 2, 1), floats))

    # Filtering: Only palindromes with more than 4 characters
    filter_result = list(
      filter(
        lambda name: is_palindrome(name), words
      )
    )

    # Reducing: Product of all numbers
    reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

    return map_result, filter_result, reduce_result


# Lists of input values
floats: List[float] = [
  4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32
]
words: List[str] = [
  'racecar', 'akinremi', 'deed',
  'temidayo', 'omoseun', 'civic',
  'TATTARRATTAT', 'malayalam', 'nun'
]
numbers: List[int] = [4, 6, 9, 23, 5]

# Call the function and unpack the results
map_result, filter_result, reduce_result = process_data(floats, words, numbers)

# Output results
print(map_result)
print(filter_result)
print(reduce_result)
