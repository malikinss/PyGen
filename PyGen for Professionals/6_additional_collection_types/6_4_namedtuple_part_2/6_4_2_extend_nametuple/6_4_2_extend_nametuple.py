'''
TODO:
    You have a namedtuple called Game available.
    Extend the code below so that it creates a namedtuple of type
    ExtendedGame that has the same fields as Game, plus two additional
    fields:
        release_date and price.

NOTE:
    The program should not output anything.
'''
from collections import namedtuple

# Define the original named tuple 'Game'
Game = namedtuple('Game', 'name developer publisher')

# Extend 'Game' to create 'ExtendedGame' with additional fields:
# 'release_date' and 'price'
ExtendedGame = namedtuple(  # type: ignore
    'ExtendedGame', (*Game._fields, 'release_date', 'price')
)
