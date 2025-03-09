'''
TODO:
    Implement a generator function dates() that takes two arguments in the
    following order:
        - start — a date, of type date
        - count — a positive integer, defaulting to None

    If count is None, the function should return a generator that produces
    a sequence of up to the maximum number of dates (type date), starting with
    the start date.

    If count is a positive integer, the function should return a generator
    that produces a sequence of count dates (type date), starting with the
    start date, and then raises a StopIteration exception.
'''
from datetime import date, timedelta
from typing import Generator


def dates(
    start: date,
    count: int | None = None
) -> Generator[date, None, None]:
    """
    Generate a sequence of dates starting from the given start date.

    Args:
        start (date): The start date.
        count (int | None, optional): Number of dates to generate.
            If None, generates an infinite sequence. Defaults to None.

    Yields:
        date: A sequence of dates.
    """
    if count is not None:
        yield from (
            start + timedelta(days=i) for i in range(count)
        )
    else:
        current = start
        while True:
            yield current
            if current == date.max:
                return
            current += timedelta(days=1)
