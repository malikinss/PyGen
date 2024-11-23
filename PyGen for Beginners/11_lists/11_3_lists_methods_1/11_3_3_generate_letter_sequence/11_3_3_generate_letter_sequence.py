'''
TODO:
    Write a program that displays the following list:
        ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
'''
from typing import List


def generate_letter_sequence() -> List[str]:
    """
    This function generates a list of strings where each string consists
    of a repeated letter starting from 'a' to 'z', with the number of
    repetitions increasing by 1 for each subsequent letter.

    Returns:
    List[str]: A list of strings with increasing repetitions of letters.
    """
    result = []

    for i in range(26):
        cur = ""

        for j in range(i + 1):
            cur += chr(ord("a") + i)

        result.append(cur)

    return result


# Generate the list and print it
result = generate_letter_sequence()
print(result)
