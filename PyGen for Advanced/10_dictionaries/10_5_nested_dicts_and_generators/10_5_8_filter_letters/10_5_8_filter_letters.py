'''
TODO:
    Complete the above code using the generator to get a result dictionary
    consisting of all elements of the letters dictionary except those whose
    keys are in the remove_keys list.

NOTE:
    You do not need to output the contents of the result dictionary.
'''
from typing import Dict, List


def filter_letters(
    letters: Dict[int, str], remove_keys: List[int]
) -> Dict[int, str]:
    """
    This function filters out key-value pairs from the `letters` dictionary
    where the key is in the `remove_keys` list and returns a new dictionary.

    Args:
        letters (Dict[int, str]): A dictionary where keys are integers
                                  and values are letters.
        remove_keys (List[int]): A list of keys to be excluded from the result.

    Returns:
        Dict[int, str]: A new dictionary containing only the key-value pairs
                        where the key is not in the `remove_keys` list.
    """
    # Using a dictionary comprehension with a generator to filter out
    # unwanted keys
    result = {
        key: value for key, value in letters.items() if key not in remove_keys
    }
    return result


# Dictionary of letters
letters = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'
}

# List of keys to be removed from the dictionary
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

# Calling the function and storing the result
result = filter_letters(letters, remove_keys)
