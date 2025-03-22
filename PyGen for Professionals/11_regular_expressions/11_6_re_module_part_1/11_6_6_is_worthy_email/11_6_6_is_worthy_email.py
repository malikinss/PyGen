'''
TODO:
    Timur often receives emails with offers of cooperation.

    Timur values mutual respect and considers a letter worthy of attention if
    it begins with one of the following expressions:
        - Hello
        - Good morning
        - Good afternoon
        - Good evening

    Write a program that determines whether a letter is worthy of Timur's
    attention.

    The program receives a single string as input.

    The program should output True if the input string begins with one of the
    expressions presented in the problem statement (in any case),
    or False otherwise.
'''
import re


def is_worthy_email() -> bool:
    """
    Checks if the email starts with one of the given greetings.

    The email is considered worthy of attention if it starts with one of the
    following phrases:
        - Hello
        - Good morning
        - Good afternoon
        - Good evening

    Returns:
        bool: True if the message starts with a valid greeting,
              otherwise False.
    """
    greeting_pattern = r'^(Hello|Good morning|Good afternoon|Good evening)'

    return bool(re.match(greeting_pattern, input(), re.IGNORECASE))


print(is_worthy_email())
