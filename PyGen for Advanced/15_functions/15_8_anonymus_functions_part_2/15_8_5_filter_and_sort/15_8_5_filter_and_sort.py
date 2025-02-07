'''
TODO:
    Write a program that uses the built-in functions filter() and sorted()
    to output words from the list words that are exactly 6 characters long.

    The words should be output in alphabetical order on one line, separated
    by a space.

NOTE:
    Use an anonymous function as the filtering criterion.
'''
from typing import Callable


words = [
    'beverage', 'monday', 'abroad', 'bias',
    'abuse', 'abolish', 'abuse', 'abuse',
    'bid', 'wednesday', 'able', 'betray',
    'accident', 'abduct', 'bigot', 'bet',
    'abandon', 'besides', 'access', 'friday',
    'bestow', 'abound', 'absent', 'beware',
    'abundant', 'abnormal', 'aboard', 'about',
    'accelerate', 'abort', 'thursday', 'tuesday',
    'sunday', 'berth', 'beyond', 'benevolent',
    'abate', 'abide', 'bicycle', 'beside',
    'accept', 'berry', 'bewilder', 'abrupt',
    'saturday', 'accessory', 'absorb'
]

# Using lambda function to filter and sort words
filter_and_sort: Callable = lambda words: (
    sorted(filter(lambda word: len(word) == 6, words))
)

# Print the result on a single line separated by spaces
print(*filter_and_sort(words))
