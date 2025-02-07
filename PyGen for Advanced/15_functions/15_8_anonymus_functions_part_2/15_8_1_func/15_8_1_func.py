'''
TODO:
    Write a function func using anonymous function syntax that takes
    an integer argument and returns True if it is divisible by 19 or 13,
    or False otherwise.
'''
from typing import Callable

# Anonymous function that returns True if x is divisible by 19 or 13,
# False otherwise.
func: Callable[[int], bool] = lambda x: (x % 19 == 0) or (x % 13 == 0)
