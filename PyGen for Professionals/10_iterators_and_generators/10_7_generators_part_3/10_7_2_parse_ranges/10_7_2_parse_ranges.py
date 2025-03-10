'''
TODO:
    Let's call a range a notation of two natural numbers separated by a hyphen
    a-b, where a is the left end of the range, b is the right end of the range,
    and a <= b.

    The range contains all numbers from a to b inclusive. For example,
    the range 1-4 contains the numbers 1, 2, 3, and 4.

    Implement the generator function parse_ranges() that takes one argument:
        - ranges is a string in which the ranges of numbers are specified
          separated by commas

    The function must return a generator that produces a sequence of numbers
    contained in the ranges.
'''


def parse_ranges(ranges: str) -> iter:
    """
    Parses a string containing ranges and returns a generator that produces
    the sequence of numbers contained in the specified ranges.

    Args:
        ranges (str): A string where multiple ranges are separated by commas.
                      Each range is represented as 'a-b', where a and b
                      are natural numbers and a <= b.

    Returns:
        iter: A generator that yields numbers from the ranges in the input
              string.

    Example:
        >>> list(parse_ranges('1-2,4-4,8-10'))
        [1, 2, 4, 8, 9, 10]
    """

    def split_ranges(ranges: str) -> iter:
        """
        Splits the input string into individual range strings.

        Args:
            ranges (str): A string containing multiple ranges separated
                          by commas.

        Returns:
            iter: An iterator over individual range strings.
        """
        return (r for r in ranges.split(','))

    def parse_range(rng: str) -> tuple[int, int]:
        """
        Parses a single range string into a tuple containing the start and
        end values.

        Args:
            rng (str): A range string in the form 'a-b', where a and b
                       are natural numbers.

        Returns:
            tuple[int, int]: A tuple containing the start and end values
                             of the range.
        """
        start, end = map(int, rng.split('-'))
        return start, end

    def generate_numbers(start: int, end: int) -> iter:
        """
        Generates numbers from start to end inclusive.

        Args:
            start (int): The starting number of the range.
            end (int): The ending number of the range.

        Returns:
            iter: A generator that yields numbers from start to end inclusive.
        """
        return (num for num in range(start, end + 1))

    return (
        num
        for rng in split_ranges(ranges)
        for start, end in (parse_range(rng),)
        for num in generate_numbers(start, end)
    )
