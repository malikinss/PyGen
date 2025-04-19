'''
TODO:
    Implement the safe_write context manager using the @contextmanager
    decorator, which takes one argument:
        filename — file name

    The context manager should allow writing information to a file named
    filename.

    And if any exception was raised while writing to the file, the context
    manager should absorb it, cancel all previously executed writes to
    the file, if any, return the file to its original state and inform about
    the raised exception by outputting the following text:
        An exception <exception type> was raised while writing to the file

NOTE:
    Visual examples of using the safe_write context manager are demonstrated
    in the test data.

    Additional data validation is not required.

    It is guaranteed that the implemented context manager is used only with
    correct data.
'''
import os
from contextlib import contextmanager
from typing import Iterator, TextIO


@contextmanager
def safe_write(filename: str) -> Iterator[TextIO]:
    """
    A context manager for safely writing to a file, reverting changes on
    exception.

    Args:
        filename: The name of the file to write to.

    Yields:
        TextIO: A file-like object for writing.

    Notes:
        If an exception occurs during writing, changes are reverted,
        and the file is restored to its original state.
        An exception message is printed.
    """
    temp_file = filename + '.tmp'
    try:
        with open(temp_file, 'w', encoding='utf-8') as buffer:
            yield buffer
        os.replace(temp_file, filename)
    except Exception as e:
        print(
            f"An exception {type(e).__name__} was raised while writing to file"
        )
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
