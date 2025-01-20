'''
TODO:
    The variable s stores a string of number:word pairs.

    Complete the code above using the generator to obtain a dictionary result
    in which numbers are keys and words are values.

NOTE:
    The dictionary keys must be integers (of type int), and the values must
    be strings (of type str).

    You do not need to print the contents of the dictionary result.
'''
from typing import Dict


def parse_string_to_dict(s: str) -> Dict[int, str]:
    """
    This function parses a string of number:word pairs into a dictionary,
    where the numbers are the keys (integers) and the words are the values
    (strings).

    Args:
        s (str): A string containing space-separated number:word pairs.

    Returns:
        Dict[int, str]: A dictionary where the keys are integers
                        (from the numbers in the string), and the
                        values are the corresponding words as strings.
    """
    # Split the input string into number:word pairs
    split_records = [record.split(':') for record in s.split()]

    # Create a dictionary using the split records
    return {int(key): value for key, value in split_records}


# Input string
s = ('1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car '
     '3:island 88:power 7:box 17:star 101:ice')

# Calling the function to parse the string into a dictionary
result = parse_string_to_dict(s)
