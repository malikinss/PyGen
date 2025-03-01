'''
TODO:
    Implement a print_operation_table() function that takes three
    arguments in the following order:
        operation — a function that characterizes some binary operation
        rows — a natural number
        cols — a natural number

    The function should create and output a table of rows rows and cols
    columns, in which the element with row n and column m has the value
    operation(n, m).

NOTE:
    The numbering of rows and columns in the table starts with one.

    The elements in the table rows should be separated by a single space,
    and it is not necessary to align the table.

    A binary operation is a mathematical operation that takes two
    arguments and returns one result.
'''
from typing import Callable


def print_operation_table(
    operation: Callable[[int, int], int],
    rows: int,
    cols: int
) -> None:
    """
    Prints a table where each element is the result of applying the given
    binary operation to the row and column indices.

    Args:
        operation (Callable[[int, int], int]): A binary operation that takes
        two integers (row and column indices) and returns an integer result.
        rows (int): The number of rows in the table.
        cols (int): The number of columns in the table.

    Returns:
        None: The function prints the table directly and does not return
              anything.

    Example:
        print_operation_table(lambda x, y: x * y, 5, 5)
        # This will print a multiplication table with 5 rows and 5 columns.
    """
    for n in range(1, rows + 1):
        row = [str(operation(n, m)) for m in range(1, cols + 1)]
        print(' '.join(row))
