'''
TODO:
    Implement a limited_hash() function that takes three arguments in
    the following order:
        - left — an integer
        - right — an integer
        - hash_function — a hash function, by default equal to
                          the built-in hash()

    The function should return a new function that takes an arbitrary object
    as an argument, calculates its hash value using
    the hash_function() function, converts it to a number belonging to
    the range [left; right], and returns the result.

    If the calculated hash value already belongs to the range [left; right],
    the function should return it without conversion.

    If the calculated hash value is right + 1, the function should convert it
    before returning:
    — to left, if right + 2
    — to left + 1, if right + 3
    — to left + 2, and so on.

    Similar transformations, but in the other direction, must be performed for
    hash values that are less than left.

    The transformations must be performed cyclically upon each exit from
    the range.
'''
from typing import Any, Callable


def limited_hash(
    left: int, right: int, hash_function: Callable = hash
) -> Callable:
    """
    Returns a function that hashes an object and maps the result
    to [left; right].

    Args:
        left: Lower bound of the output range (inclusive).
        right: Upper bound of the output range (inclusive).
        hash_function: Function to compute the hash of an object, defaults
                       to built-in hash.

    Returns:
        Callable: A function that takes an object, computes its hash
                  using hash_function, and maps it to the range [left; right].
                  If the hash is outside the range, it is cyclically
                  transformed:
                    - right + 1 maps to left, right + 2 to left + 1, etc.
                    - left - 1 maps to right, left - 2 to right - 1, etc.
    """
    def func(obj: Any) -> int:
        hashed = hash_function(obj)
        if left <= hashed <= right:
            return hashed
        range_size = right - left + 1
        hashed = ((hashed - left) % range_size) + left
        return hashed
    return func
