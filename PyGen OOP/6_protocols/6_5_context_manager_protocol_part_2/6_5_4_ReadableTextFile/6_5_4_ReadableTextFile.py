'''
TODO:
    Implement the ReadableTextFile class.

    When creating an instance, the class must accept one argument:
        filename — the name of the text file

    An instance of the ReadableTextFile class must be a context manager
    that opens a file named filename for reading in UTF-8 encoding and allows
    you to get its lines without the line break character \n at the end.

    The context manager must also close the file it opened after executing
    the code inside the with block.

NOTE:
    Visual examples of using the ReadableTextFile class are demonstrated in
    the test data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The ReadableTextFile class must satisfy the context manager protocol,
    that is, have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import TextIO, Any


class ReadableTextFile:
    """
    A context manager for reading text files with lines stripped of trailing
    newlines.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize with the name of the text file.

        Args:
            filename: Name of the text file.
        """
        self.filename = filename
        self.data: TextIO = None  # Initialize to avoid undefined state

    def __enter__(self) -> TextIO:
        """
        Open the file for reading in UTF-8 and return it.

        Returns:
            TextIO: File object that yields lines without trailing newlines.
        """
        self.data = open(self.filename, 'r', encoding='utf-8')
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Close the file.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        if self.data:
            self.data.close()

    def __iter__(self) -> TextIO:
        """
        Allow iteration over the file lines.

        Returns:
            TextIO: Iterator over lines with trailing newlines removed.
        """
        return self

    def __next__(self) -> str:
        """
        Get the next line from the file, stripped of trailing newlines.

        Returns:
            str: The next line without trailing newlines.

        Raises:
            StopIteration: When there are no more lines.
        """
        line = self.data.readline()
        if not line:
            raise StopIteration
        return line.rstrip('\n')
