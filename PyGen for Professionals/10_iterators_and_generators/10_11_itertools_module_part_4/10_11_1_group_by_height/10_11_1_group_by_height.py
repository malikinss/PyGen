'''
TODO:
    You have a named tuple Person that contains data about a person.

    The first element of the named tuple is the person's name, the second is
    their age, and the third is their height.

    You also have a list of persons that contains these tuples.

    Complete the code below so that it groups the people in this list by their
    height and prints the resulting groups.

    Each group must first list their height, followed by a comma-separated
    list of names of people with the corresponding height.

    The groups must be ordered by increasing height, each on a separate line,
    with names in alphabetical order, in the following format:
        <height>: <name>, <name>, ...

NOTE:
    The initial part of the response looks like this:
        158: Ariana, Eva
        172: Mark
        ...
'''
from collections import namedtuple
from itertools import groupby
from typing import Iterable, Callable

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [
    Person('Tim', 63, 193), Person('Eva', 47, 158),
    Person('Mark', 71, 172), Person('Alex', 45, 193),
    Person('Jeff', 63, 193), Person('Ryan', 41, 184),
    Person('Ariana', 28, 158), Person('Liam', 69, 193)
]


def group_by_height(iterable: Iterable[Person]) -> None:
    """
    Groups people by their height and prints the results in ascending order of
    height.

    Args:
        iterable (Iterable[Person]): List of Person tuples.

    Output Format:
        <height>: <name1>, <name2>, ...
    """
    key_func: Callable[[Person], int] = lambda x: x.height

    grouped = groupby(
        sorted(iterable, key=key_func),
        key=key_func
    )

    for height, group in grouped:
        names = sorted(map(lambda p: p.name, group))
        print(f'{height}: {", ".join(names)}')


group_by_height(persons)
