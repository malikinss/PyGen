'''
TODO:
    During an interview, you were asked to solve a username validation problem.

    The user is trying to create a nickname for their account
    on social network Y.

    The rules for a correct nickname on social network Y are as follows:
        - The nickname must start with the @ symbol
        - The nickname must contain from 5 to 15 (inclusive) characters
            (including the first @ symbol)
        - The nickname must contain only lowercase letters and numbers
            (except for the first @ symbol)

    Write a program that outputs "Correct" (without quotes) if the nickname
    meets all the above rules, or "Incorrect" (without quotes) otherwise.

NOTE:
    Please note that the nickname does not have to contain lowercase letters
    and numbers at the same time, the nickname can contain only lowercase
    letters or only numbers (except for the first @ symbol).
    For example, the following nicknames are considered correct:
        @duncan
        @1111
'''
from string import ascii_lowercase, digits


def is_correct_nickname(nickname: str) -> None:
    """
    Validates the nickname based on the rules of the social network.

    Args:
    nickname (str): The input nickname to validate.

    Outputs:
    str: "Correct" if the nickname is valid, "Incorrect" otherwise.
    """
    if not nickname.startswith("@"):
        print("Incorrect")
        return

    if len(nickname) < 5 or len(nickname) > 15:
        print("Incorrect")
        return

    # Check if all characters after "@" are in the allowed set
    allowed_chars = ascii_lowercase + digits
    for char in nickname[1:]:
        if char not in allowed_chars:
            print("Incorrect")
            return

    print("Correct")


# Reading input
given_nickname = input()
is_correct_nickname(given_nickname)
