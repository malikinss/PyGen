'''
TODO:
    Enhance the following code using the concatenation (+) and
    list multiplication (*) operators so that it outputs a list:
        [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].
'''
from typing import List

# original code
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

# fixed code


def create_custom_list(numbers1: List[int],
                       numbers2: List[int],
                       numbers3: List[int]) -> List[int]:
    """
    Returns a list created by concatenating and multiplying the input lists
    in the following order:
    - The first list is repeated twice.
    - The second list is repeated nine times.
    - The third list is added as is.
    """
    return (numbers1 * 2) + (numbers2 * 9) + numbers3


# original code
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

# Call the function and print the result
result = create_custom_list(numbers1, numbers2, numbers3)
print(result)
