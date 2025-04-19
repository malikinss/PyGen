'''
TODO:
    Implement the reversed_print context manager using the @contextmanager
    decorator, which takes no arguments.

    The reversed_print context manager must allow all writes to the standard
    output stream sys.stdout inside the with block to be performed in reverse
    order.

NOTE:
    Visual examples of using the reversed_print context manager are
    demonstrated in the test data.

    No additional data validation is required.

    It is guaranteed that the implemented context manager is used only with
    valid data.
'''
import sys
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def reversed_print() -> Iterator[None]:
    """
    A context manager that reverses text written to sys.stdout in a with block.

    Yields:
        None: The context manager yields control to the with block.
    """
    def new_write(text: str) -> None:
        old_write(text[::-1])

    old_write = sys.stdout.write
    sys.stdout.write = new_write
    try:
        yield
    finally:
        sys.stdout.write = old_write
