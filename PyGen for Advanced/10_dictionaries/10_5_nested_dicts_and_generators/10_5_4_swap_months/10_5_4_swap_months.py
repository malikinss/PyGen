'''
TODO:
    Complete the above code using the generator to produce a dictionary result
    consisting of all elements of the dictionary months in which the key and
    value have been swapped.

NOTE:
    You do not need to print the contents of the dictionary result.
'''
from typing import Dict


def swap_months(months: Dict[int, str]) -> Dict[str, int]:
    """
    This function takes a dictionary where the keys are month numbers (1 to 12)
    and the values are month names, and returns a new dictionary with the keys
    and values swapped.

    In the resulting dictionary, the keys will be the month names, and the
    values will be the corresponding month numbers.

    Args:
        months (Dict[int, str]): A dictionary where the keys are integers
                                 (1 to 12) representing the month numbers,
                                 and the values are strings representing
                                 the month names.

    Returns:
        Dict[str, int]: A new dictionary with the keys and values swapped,
                        where the keys are month names and the values are the
                        corresponding month numbers.
    """
    # Using dictionary comprehension to swap the keys and values
    return {value: key for key, value in months.items()}


# Dictionary of months
months = {
    1: 'January', 2: 'February', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}

# Calling the function to swap the months dictionary
result = swap_months(months)
