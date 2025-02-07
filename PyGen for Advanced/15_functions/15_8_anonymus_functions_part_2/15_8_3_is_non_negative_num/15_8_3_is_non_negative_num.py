'''
TODO:
    Write a function, is_non_negative_num, using anonymous function syntax
    that takes a string argument and returns True if the argument passed is
    a non-negative number (integer or float), or False otherwise.
'''
from typing import Callable


# Anonymous function that returns True if the input string represents
# a non-negative number
is_non_negative_num: Callable = lambda number: number.count('.') < 2 and \
    number.replace('.', '', 1).isdigit() and not number.startswith('-')
