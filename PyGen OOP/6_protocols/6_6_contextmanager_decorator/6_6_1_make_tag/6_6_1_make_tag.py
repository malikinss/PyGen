'''
TODO:
    Implement the context manager make_tag using the @contextmanager decorator,
    which takes one argument:
        tag - an arbitrary string

    The context manager should output the string tag when entering the with
    block and after exiting the with block.

NOTE:
    Visual examples of using the context manager make_tag are demonstrated in
    the test data.

    No additional data validation is required.

    It is guaranteed that the implemented context manager is used only with
    correct data.
'''
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def make_tag(tag: str) -> Iterator[None]:
    """
    A context manager that prints a tag string upon entering and exiting
    a with block.

    Args:
        tag: The string to print when entering and exiting the context.

    Yields:
        None: The context manager yields control to the with block.
    """
    print(tag)
    yield
    print(tag)
