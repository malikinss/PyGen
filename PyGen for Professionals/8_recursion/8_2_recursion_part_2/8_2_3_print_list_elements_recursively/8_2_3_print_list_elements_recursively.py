'''
TODO:
    You have a list numbers that contains exactly 100 integers.

    Expand the code below using recursion so that it prints all the elements
    of this list from first to last, each on a separate line, in the following
    format:
        Element <element index>: <element value>
'''
from typing import List

numbers = [243, -279, 395, 130, 89, 269, 861,
           669, 939, 367, -46, 710, 841, -280,
           -244, 274, -132, 273, 418, 432, -341,
           437, 360, 960, 195, 792, 106, 461, -35,
           980, -80, 540, -358, 69, -26, -416, 597,
           96, 533, 232, 755, 894, 331, 323, -383,
           -386, 231, 436, 553, 967, 166, -151, 772,
           434, 325, 301, 275, 431, 556, 728, 558,
           702, 463, 127, 984, 212, 876, -287, -16,
           -177, 577, 604, 116, 500, 653, 669, 916,
           802, 817, 762, -210, -353, 144, -351, 777,
           805, 692, 22, -303, 249, 190, 411, 236,
           -274, 174, 380, 71, 124, -85, 430]


def print_list_elements_recursively(elements: List[int]) -> None:
    """
    Prints all elements of a list recursively.

    Args:
        elements (List[int]): A list of integers to be printed.

    Returns:
        None
    """
    def print_element_recursive(index: int) -> None:
        """
        Recursively prints each element in the list.

        Args:
            index (int): The current index of the element to be printed.

        Returns:
            None
        """
        # Base case: if the index is within the list bounds
        if index <= len(elements) - 1:
            print(f'Элемент {index}: {elements[index]}')
            print_element_recursive(index + 1)

    print_element_recursive(0)


print_list_elements_recursively(numbers)
