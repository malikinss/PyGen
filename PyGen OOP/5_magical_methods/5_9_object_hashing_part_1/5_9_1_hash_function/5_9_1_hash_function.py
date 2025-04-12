'''
TODO:
    Implement a hash_function() that takes one argument:
        - obj — an arbitrary object

    The function should calculate the hash value of the object obj according
    to the following algorithm:
        1. calculate the value of the expression:
            ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) +\
                ord(obj[2]) * ord(obj[-3]) + ...
        where obj is an object converted to a string using the str() function.

        Note that the sum must be the products of the first and last elements,
        the second and the penultimate, and so on up to the middle.

        If obj has an odd number of characters, then the middle element should
        be added without multiplication

        2. calculating the expression value:
            ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ...
        where obj is an object converted to a string using the str() function

        3. calculating the expression value:
            (temp1 * temp2) % 123456791
        where temp1 is the value obtained in the first step, temp2 is
        the value obtained in the second step

    and return the value obtained in the third step.

NOTE:
    Submit to the testing system a program containing only the required
    hash_function() function, but not the code that calls it.
'''
from typing import Any


def hash_function(obj: Any) -> int:
    """
    Calculate a custom hash value for an object based on its string
    representation.

    Args:
        obj: Any object to be hashed.

    Returns:
        int: Hash value computed as (temp1 * temp2) % 123456791, where:
            - temp1 is the sum of products ord(s[i]) * ord(s[-(i+1)])
              for i from 0 to len(s)//2, plus ord(s[len(s)//2]) if len(s)
              is odd.
            - temp2 is the alternating sum
              ord(s[0])*1 - ord(s[1])*2 + ord(s[2])*3 - ...,
            - s is str(obj).
    """
    s = str(obj)
    n = len(s)

    # Expression 1: Symmetric product sum
    symmetric_sum = 0
    for i in range(n // 2):
        symmetric_sum += ord(s[i]) * ord(s[-(i + 1)])
    if n % 2:
        symmetric_sum += ord(s[n // 2])

    # Expression 2: Weighted alternating sum
    weighted_sum = sum(
        (ord(c) * (i + 1) * (-1 if i % 2 else 1)) for i, c in enumerate(s)
    )

    return (symmetric_sum * weighted_sum) % 123456791
