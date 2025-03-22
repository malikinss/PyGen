'''
TODO:
    You have access to a set of phone numbers in the following formats:
        <country code>-<city code>-<number>
        <country code> <city code> <number>
    where the country code and city code are represented by sequences of one
    to three digits inclusive, and the number is a sequence of four to ten
    digits inclusive.

    A separator is used between the country code, city code and number, which
    is either a hyphen or a space, and both types of separators cannot be
    present in one number at the same time.

    Write a program that accepts an arbitrary number of phone numbers and
    outputs the country code, city code and number separately for each.

    The program is fed an arbitrary number of phone numbers that satisfy the
    above patterns, each on a separate line.

    The program should output the country code, city code and number
    separately for each entered phone number in the following format:
        Country code: <country code>, City code: <city code>, Number: <number>
'''
import re
import sys
from typing import List


def read_code_from_input() -> List[str]:
    """
    Reads the phone number lines from the input.

    This function reads all input lines and strips any trailing
    whitespace characters from each line. It returns the input as a list of
    strings.

    Returns:
        List[str]: A list of phone number strings, each representing a phone
        number line.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def process_numbers(numbers: List[str]) -> None:
    """
    Processes a list of phone numbers and prints the parsed components.

    This function uses a regular expression to extract the country code,
    city code, and number from each phone number.

    It prints these components in the specified format.

    Args:
        numbers (List[str]): A list of phone numbers to be processed.

    Returns:
        None: This function prints the results directly.
    """
    regex = r'(?P<country>\d{1,3})([- ]?)(?P<city>\d{1,3})\2(?P<num>\d{4,10})'

    for num in numbers:
        match = re.match(regex, num)
        if match:
            data = match.groupdict()
            print(
                f"Country code: {data['country']},"
                f" City code: {data['city']},"
                f" Number: {data['num']}"
            )
        else:
            print(f"Invalid phone number format: {num}")


process_numbers(read_code_from_input())
