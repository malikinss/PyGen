'''
TODO:
    Implement the safe_open context manager using the @contextmanager
    decorator, which takes two arguments in the following order:
        filename — the file name
        mode — the file open mode (r, w, a, etc.), defaulting to r

    The context manager must open the file named filename in mode and allow
    the appropriate operations to be performed on it.

    Moreover, if the file was opened without exceptions, the context manager
    must return a tuple of two elements as the value used in the with block,
    the first of which is the required file object, and the second is
    the None value.

    However, if an exception was raised when opening the file, the context
    manager must return a tuple of two elements as the value used in the with
    block, the first of which is the None value, and the second is
    the exception raised when opening.

    The context manager must also close the file it opened after executing
    the code inside the with block.

NOTE:
    Illustrative examples of using the safe_open context manager are
    demonstrated in the test data.

    No additional data validation is required.

    It is guaranteed that the implemented context manager is used only with
    correct data.
'''
from contextlib import contextmanager
from typing import Iterator, Tuple, Optional, IO, Any


@contextmanager
def safe_open(
    filename: str, mode: str = 'r'
) -> Iterator[Tuple[Optional[IO[Any]], Optional[Exception]]]:
    """
    A context manager for safely opening a file, returning a file object
    or exception.

    Args:
        filename: The name of the file to open.
        mode: The mode in which to open the file (e.g., 'r', 'w', 'a').
              Defaults to 'r'.

    Yields:
        Tuple[Optional[IO[Any]], Optional[Exception]]: A tuple containing:
            - The file object and None if opened successfully, or
            - None and the exception if opening failed.
    """
    file: Optional[IO[Any]] = None
    try:
        encoding = 'utf-8' if 'b' not in mode else None
        file = open(filename, mode, encoding=encoding)
        yield (file, None)
    except Exception as e:
        yield (None, e)
    finally:
        if file is not None:
            file.close()
