'''
TODO:
    Edit the code below to:
        - Replace the second element of the list with 17;
        - Add the numbers 4, 5 and 6 to the end of the list;
        - Remove the first element of the list;
        - Double the list;
        - Insert the number 25 at index 3;
        - Print out a list using the print() function
'''
from typing import List

# original code
numbers = [8, 9, 10, 11]


# fixed code
def modify_list(numbers: List[int]) -> List[int]:
    """
    This function performs a series of operations on a given list:
        - Replaces the second element of the list with 17;
        - Adds the numbers 4, 5, and 6 to the end of the list;
        - Removes the first element of the list;
        - Doubles the list;
        - Inserts the number 25 at index 3.

    Args:
        numbers (List[int]): A list of integers to modify.

    Returns:
        List[int]: The modified list after all operations.
    """
    # Replace the second element with 17
    numbers[1] = 17

    # Add 4, 5, and 6 to the end of the list
    numbers.extend([4, 5, 6])

    # Remove the first element
    del numbers[0]

    # Double the list
    numbers *= 2

    # Insert 25 at index 3
    numbers.insert(3, 25)

    return numbers


# Original list
numbers = [8, 9, 10, 11]

# Apply the modifications
modified_numbers = modify_list(numbers)

# Print the result
print(modified_numbers)
