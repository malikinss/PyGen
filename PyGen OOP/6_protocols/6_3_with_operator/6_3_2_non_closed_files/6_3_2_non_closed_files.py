'''
TODO:
    Implement a non_closed_files() function that takes one argument:
        files — a list of file objects

    The function should return a list whose elements are the open file objects
    in the files list.

NOTE:
    The file objects in the list returned by the function must be in
    their original order.
'''
from typing import List, IO


def non_closed_files(files: List[IO]) -> List[IO]:
    """
    Return a list of open file objects from the input list.

    Args:
        files: List of file objects.

    Returns:
        List[IO]: List of open file objects in their original order.
    """
    return [file for file in files if not file.closed]
