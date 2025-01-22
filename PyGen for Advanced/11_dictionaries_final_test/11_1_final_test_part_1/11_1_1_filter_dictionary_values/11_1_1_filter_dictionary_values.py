'''
TODO:
    Supplement the given code so that the lists of values of the elements
    of the dictionary my_dict do not contain numbers greater than 20.

    At the same time, the order of the remaining elements should not change.

NOTE:
    It is necessary to change the dictionary my_dict, there is no need
    to output anything.
'''


def filter_dictionary_values(my_dict: dict) -> None:
    """
    Modifies the given dictionary in-place such that the lists of values
    do not contain numbers greater than 20, while preserving the order
    of elements.

    Args:
        my_dict (dict): A dictionary where keys are strings and values are
                        lists of integers.
    """
    # Filter out numbers greater than 20 from each list in the dictionary
    for key, value in my_dict.items():
        my_dict[key] = [element for element in value if element <= 20]


# Original dictionary
my_dict = {
    'C1': [10, 20, 30, 7, 6, 23, 90],
    'C2': [20, 30, 40, 1, 2, 3, 90, 12],
    'C3': [12, 34, 20, 21],
    'C4': [22, 54, 209, 21, 7],
    'C5': [2, 4, 29, 21, 19],
    'C6': [4, 6, 7, 10, 55],
    'C7': [4, 8, 12, 23, 42],
    'C8': [3, 14, 15, 26, 48],
    'C9': [2, 7, 18, 28, 18, 28]
}

# Apply the filtering function
filter_dictionary_values(my_dict)
