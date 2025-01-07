'''
TODO:
    The program is given a string of text containing numbers as input.

    For each number, output the word YES (on a separate line) if the number
    has appeared in the sequence before, or NO otherwise.

NOTE:
    Leading zeros in numbers should be ignored.
'''
from typing import List


def check_number_repeats(sequence: List[str]) -> None:
    """
    Determines if each number in the sequence has appeared before, ignoring
    leading zeros.

    Args:
        sequence (List[str]): List of numbers in string format.

    Returns:
        None: Prints "YES" if the number has appeared before, "NO" otherwise.
    """
    seen_numbers = set()

    for num in sequence:
        parsed_num = int(num)

        if parsed_num in seen_numbers:
            print("YES")
        else:
            print("NO")

        seen_numbers.add(parsed_num)


numbers = input().split()
check_number_repeats(numbers)
