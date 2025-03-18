'''
TODO:
    You have the password_gen() function, which returns a generator that
    produces all three-character string passwords in ascending order, composed
    of the digits 0 through 9 inclusive.

    Rewrite this function using the product() function to perform the same
    task.
'''
from itertools import product
from typing import Iterator


def password_gen() -> Iterator[str]:
    """
    Generates all three-character string passwords in ascending order,
    composed of digits from 0 through 9 inclusive.
    Yields passwords as strings.
    """
    password_combs = product(map(str, range(10)), repeat=3)

    for comb in password_combs:
        yield ''.join(comb)
