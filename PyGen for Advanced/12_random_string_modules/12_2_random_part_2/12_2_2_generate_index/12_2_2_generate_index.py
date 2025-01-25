'''
TODO:
    The postal code in Latveria is:
        LetterLetterNumber_NumberLetterLetter
    where Letter is a capital letter of the English alphabet, Number is
    a number from 0 to 99 (inclusive).

    Write a function generate_index() that uses the random module to generate
    and return a random valid postal code for Latveria.

NOTE:
    An example of a valid (invalid) postal code for Latveria:
    AB23_56VG # valid
    V3F_231GT # invalid

    Note the _ symbol in the postal code.

    You don't need to call the generate_index() function, you just need
    to implement it.
'''
import random


def generate_index() -> str:
    """
    Generates and returns a random valid postal code for Latveria in
    the format:
        LetterLetterNumber_NumberLetterLetter where:
            - Letter is a capital letter from A-Z,
            - Number is a number from 0 to 99 (inclusive),
            - The postal code contains an underscore separating
              the number segments.

    Returns:
        str: A randomly generated valid postal code for Latveria.
    """
    postal_code = [
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),  # First letter
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),  # Second letter
        str(random.randint(0, 99)),  # First number
        '_',  # Underscore separator
        str(random.randint(0, 99)),  # Second number
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),  # Fifth letter
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   # Sixth letter
    ]
    return ''.join(postal_code)
