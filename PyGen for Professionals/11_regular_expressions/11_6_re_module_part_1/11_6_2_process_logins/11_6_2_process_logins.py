'''
TODO:
    In the BEEGEEK online school, the account login is determined as follows:
        - the first character is the underscore _
        - then one or more digits
        - then zero or more Latin letters in any case
        - the login may have an optional underscore _ at the end

    Write a program that accepts an arbitrary number of lines and determines
    which of them represent a valid login for the BEEGEEK online school.

    The program is given an arbitrary number of lines, each containing a set
    of arbitrary characters.

    The program should output True for each line entered if it represents
    a valid login for the BEEGEEK online school, or False otherwise.
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


def process_logins(logins: List[str]) -> None:
    """
    Processes each login and determines whether it is valid according to the
    BEEGEEK login rules.

    A valid login must:
        - Start with an underscore (_),
        - Followed by one or more digits,
        - Optionally contain zero or more Latin letters
          (uppercase or lowercase),
        - Optionally end with an underscore (_).

    Args:
        logins (List[str]): A list of login strings to validate.

    Returns:
        None: Prints True for valid logins and False for invalid ones.
    """
    regex = r'_\d+[a-zA-Z]*_?'  # Regular expression to match valid logins
    for login in logins:
        if re.fullmatch(regex, login):
            print(True)
        else:
            print(False)


process_logins(read_code_from_input())
