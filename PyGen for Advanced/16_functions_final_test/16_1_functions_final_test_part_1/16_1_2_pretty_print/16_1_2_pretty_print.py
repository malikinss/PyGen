'''
TODO:
    Write a pretty_print() function that prints the contents of a list with
    a frame.

    The function must receive one mandatory argument data - a list to be
    printed and two optional single-character string arguments side and
    delimiter and print the contents of the list according to the examples.

    If the side argument is missing, then we set side='-', and if
    the delimiter argument is missing, then we set delimiter='|'.
'''
from typing import List


def pretty_print(
    data: List[int], side: str = '-', delimiter: str = '|'
) -> None:
    """
    Prints the contents of a list with a frame around it.

    Parameters:
    - data (List[int]): The list of elements to be printed.
    - side (str, optional): The character used to create the frame.
                            Default is '-'.
    - delimiter (str, optional): The character used to separate the elements
                                 inside the frame.
                                 Default is '|'.

    Returns:
    - None: This function prints the framed list directly.
    """
    # Construct the general row with the list elements
    general_row = ''.join(
        [delimiter, ''.join(str(element) for element in data), delimiter]
    )

    # Construct the frame row based on the general row length
    frame_row = side * len(general_row)

    # Print the frame, general row, and frame again
    print(frame_row)
    print(general_row)
    print(frame_row)
