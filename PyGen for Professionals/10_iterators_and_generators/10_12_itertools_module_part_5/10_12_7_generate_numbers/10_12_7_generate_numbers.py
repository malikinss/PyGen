'''
TODO:
    Write a program that generates all numbers of length m in the number
    system n.

    The first line of the program is the natural number 2≤n≤16 — the base of
    the number system, and then the natural number m — the length of the
    numbers being generated.

    The program must generate all numbers of length m in the number system n
    and output them in ascending order separated by a space.

NOTE:
    In number systems with base 11 and higher, capital Latin letters must be
    used as digits:
        A, B, C, D,...
'''
from itertools import product


def generate_numbers(n: int, m: int) -> None:
    """
    Generates all numbers of length `m` in the number system of base `n`
    and outputs them in ascending order separated by spaces.

    Args:
    n (int): The base of the number system (2 ≤ n ≤ 16).
    m (int): The length of the numbers to generate.
    """
    digits = '0123456789ABCDEF'

    result = product(digits[:n], repeat=m)

    for comb in result:
        print(''.join(comb), end=' ')


generate_numbers(int(input()), int(input()))
