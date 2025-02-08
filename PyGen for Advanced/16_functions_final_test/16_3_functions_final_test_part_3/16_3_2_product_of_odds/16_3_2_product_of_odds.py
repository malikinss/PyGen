'''
TODO:
    Rewrite the product_of_odds() function in a functional style using the
    built-in filter() and reduce() functions.

    def product_of_odds(data): # data is a list of integers
        result = 1
        for i in data:
            if i % 2 == 1:
                result *= i
        return result

NOTE:
    The testing system will not "punish" you for not using the built-in
    filter() and reduce() functions, but it is better to do this task honestly.

    You do not need to call the product_of_odds() function, you only need
    to implement it in a functional style.
'''
from functools import reduce
from typing import List


def product_of_odds(data: List[int]) -> int:
    """
    Returns the product of all odd numbers in the given list of integers.

    Parameters:
    - data (List[int]): The list of integers to process.

    Returns:
    - int: The product of all odd numbers in the list. If no odd numbers
           are found, returns 1.
    """
    filtered_data = filter(lambda x: x % 2 == 1, data)
    result = reduce(lambda x, y: x * y, filtered_data, 1)
    return result
