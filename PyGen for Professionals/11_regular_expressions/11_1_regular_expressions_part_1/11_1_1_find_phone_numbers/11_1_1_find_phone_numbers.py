'''
TODO:
    Write a program that finds all phone numbers in the given text that match
    the following formats:
        7-ddd-ddd-dd-dd
        8-ddd-dddd-dddd
        where d is a digit from 0 to 9.

    The program receives a string of arbitrary content as input.

    The program must find all phone numbers in the input text that match the
    formats specified in the problem statement and output them in the order in
    which they were found, each on a separate line.

NOTE:
    The problem can be solved both with and without regular expressions.

    At this stage, the module for solving with regular expressions has not yet
    been studied, so the recommended method is to solve without them.

    If desired, you can return to the problem after studying the corresponding
    module.
'''
import re


def find_phone_numbers(text: str) -> None:
    """Finds phone numbers in the given text that match the formats:
    - 7-ddd-ddd-dd-dd
    - 8-ddd-dddd-dddd
    - +7-ddd-ddd-dd-dd (converted to 7-ddd-ddd-dd-dd)

    Args:
        text (str): Input text containing phone numbers.

    Prints:
        Matching phone numbers, one per line.
    """
    pattern = re.compile(r'\+?7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}')
    matches = pattern.findall(text)

    for phone in matches:
        print(phone.lstrip('+'))


find_phone_numbers(input())
