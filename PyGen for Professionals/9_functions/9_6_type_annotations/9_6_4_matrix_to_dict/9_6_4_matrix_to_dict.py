'''
TODO:
    Implement the matrix_to_dict() function using type annotations that takes
    one argument:
        matrix — a matrix of arbitrary dimension whose elements are integers
        or real numbers

    The function must return a dictionary whose key is the matrix row number
    and whose value is a list of elements of this row.

NOTE:
    Use built-in types (list, tuple, ...), not types from the typing module.

    Also use the | notation, not the Union type from the typing module.

    Matrix refers exclusively to nested lists.

    The matrix rows in the dictionary returned by the function must
    be numbered starting with one.

    The matrix elements in the list must be in their original order.
'''
# Define a type for the rows of the matrix
MatrixRow = list[int | float]


def matrix_to_dict(matrix: list[MatrixRow]) -> dict[int, MatrixRow]:
    """
    Convert a matrix to a dictionary where each key is the row number.

    Args:
        matrix (list[list[int | float]]): A matrix of arbitrary dimension
        whose elements are integers or real numbers.

    Returns:
        dict[int, list[int | float]]: A dictionary where the key is the matrix
        row number (starting from 1) and the value is a list of
        elements of this row.
    """
    # Convert the matrix into a dictionary with row numbers as keys
    return {index: row for index, row in enumerate(matrix, start=1)}
