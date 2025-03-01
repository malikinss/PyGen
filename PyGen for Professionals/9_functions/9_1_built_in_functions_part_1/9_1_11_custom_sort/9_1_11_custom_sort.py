'''
TODO:
        Given a string containing Latin letters and numbers.

        Write a program that sorts the characters in the string according to
        the following rules:
        - all sorted lowercase letters come before capital letters
        - all sorted capital letters come before numbers
        - all sorted odd numbers come before sorted even numbers
'''


def custom_sort(given_string: str) -> str:
    """
    Sorts the characters in the given string according to specific rules.

    The sorting rules are as follows:
    - All sorted lowercase letters come before capital letters.
    - All sorted capital letters come before numbers.
    - All sorted odd numbers come before sorted even numbers.

    Args:
        given_string (str): The input string containing Latin letters and
        numbers.

    Returns:
        str: The sorted string.
    """
    def character_sort_key(c: str) -> tuple:
        """
        Determines the sorting key for a character.

        Args:
            c (str): The character to sort.

        Returns:
            tuple: A tuple that represents the sorting priority of
            the character.
        """
        if c.isalpha():
            return (0, c) if c.islower() else (1, c)
        elif c.isdigit():
            return (2, c) if int(c) % 2 != 0 else (3, c)

    sorted_characters = sorted(given_string, key=character_sort_key)

    return ''.join(sorted_characters)


# Example usage
print(custom_sort(input()))
