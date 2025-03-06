'''
TODO:
    Implement a PowerOf class that produces iterators whose constructor takes
    one argument:
        number is a nonzero number

    The iterator of class PowerOf must generate an infinite sequence
    of nonnegative integer powers of number in ascending order, starting with
    the zeroth power.
'''


class PowerOf:
    """
    Iterator that generates powers of a given number.

    The sequence starts from the 0th power of the number (i.e., num^0 = 1),
    and then continues with increasing powers (num^1, num^2, ...).

    Args:
        number (int): The number for which powers will be generated.
                      Must be a non-zero integer.

    Raises:
        ValueError: If the provided number is 0, as powers of zero are
        not defined.
    """

    def __init__(self, number: int):
        if number == 0:
            raise ValueError('Number should have nonzero value')

        # Start exponent from 0 (to return num ** 0 = 1 initially)
        self.exp: int = 0
        self.num: int = number

    def __iter__(self) -> 'PowerOf':
        """
        Returns the iterator object (itself).

        Returns:
            PowerOf: The iterator instance.
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next power of the given number.

        The sequence starts from num^0 = 1, num^1 = num, num^2 = num * num,
        and so on.

        Returns:
            int: The next power of the number.

        Raises:
            OverflowError: If the value of the power exceeds system limits
            (typically won't occur for small integers).
        """
        result = self.num ** self.exp

        # Increase the exponent for the next iteration
        self.exp += 1
        return result
