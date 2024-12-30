'''
TODO:
    Using the list comprehension's extend() method, extend the code below
    so that list1 looks like this:
        list1 = [
            'a', 'b',
            [
                'c',
                [
                    'd',
                    'e',
                    ['f', 'g', 'h', 'i', 'j'],
                    'k'
                ],
                'l'
            ],
            'm', 'n'
        ]
'''
from typing import List


list1: List = [
    'a',
    'b',
    ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'],
    'm',
    'n'
]
list1[2][1][2].extend(['h', 'i', 'j'])

print(list1)
