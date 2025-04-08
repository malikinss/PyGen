'''
TODO:
    Implement a Matrix class that describes a two-dimensional matrix.

    When instantiated, the class must accept three arguments in the following
    order:
        rows — the number of rows in the matrix
        cols — the number of columns in the matrix
        value — the initial value for the matrix elements, defaults to 0

    An instance of the Matrix class must have two attributes:
        rows — the number of rows in the matrix
        cols — the number of columns in the matrix

    The Matrix class must have two instance methods:
        - get_value() — a method that takes a row row and a column col
                        as arguments and returns the matrix element with row
                        row and column col
        - set_value() — a method that takes a row row, a column col, and
                        a value as arguments and sets the value of the matrix
                        element with row row and column col to value

    An instance of the Matrix class must have the following formal string
    representation:
        Matrix(<number of rows in matrix>, <number of columns in matrix>)

    The informal string representation must be be a string that lists all
    the elements of the matrix.

    The elements of a matrix row must be separated by a space, and the rows of
    a matrix must be separated by the line feed character "\n".

    For example, for a Matrix(2, 3) object, the informal string representation
    should be 0 0 0\n0 0 0, which would be displayed as follows when printed:
        0 0 0
        0 0 0

    Also, a Matrix instance should support the unary operators +, -, and ~:
        - the result of a unary + should be a new Matrix instance with
          the original number of rows and columns and with the original
          elements
        - the result of a unary - should be a new Matrix instance with
          the original number of rows and columns and with the elements taken
          with the opposite sign
        - the result of a unary ~ should be a new Matrix instance representing
          the transposed matrix

    Finally, when passing a Matrix instance to the round() function,
    a new Matrix instance should be returned with the original number of rows
    and columns and with the elements rounded using the round() function.

    When passing to the round() function, it must be possible to specify
    an integer as a second optional argument, which determines the number
    of decimal places when rounding.

NOTE:
    The indexing of rows and columns in the matrix starts from zero.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the Matrix class,
    it can be arbitrary.
'''
from typing import Union


class Matrix:
    """
    A class representing a two-dimensional matrix.
    """

    def __init__(
        self, rows: int, cols: int, value: Union[float, int] = 0
    ) -> None:
        """
        Initialize a Matrix with specified rows, columns, and initial value.

        Args:
            rows (int): Number of rows in the matrix.
            cols (int): Number of columns in the matrix.
            value (float | int): Initial value for all elements, defaults to 0.
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def __repr__(self) -> str:
        """
        Formal string representation of the Matrix.

        Returns:
            str: Representation like 'Matrix(2, 3)'.
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self) -> str:
        """
        Informal string representation of the Matrix.

        Returns:
            str: Matrix elements with spaces between columns and newlines
                 between rows.
        """
        return "\n".join(
            " ".join(str(elem) for elem in row)
            for row in self.matrix
        )

    def get_value(self, row: int, col: int) -> Union[float, int]:
        """
        Get the value at the specified row and column.

        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).

        Returns:
            float | int: The value at the specified position.
        """
        return self.matrix[row][col]

    def set_value(self, row: int, col: int, value: Union[float, int]) -> None:
        """
        Set the value at the specified row and column.

        Args:
            row (int): Row index (0-based).
            col (int): Column index (0-based).
            value (float | int): Value to set.
        """
        self.matrix[row][col] = value

    def __pos__(self) -> 'Matrix':
        """
        Unary + operator: returns a new Matrix with the same elements.

        Returns:
            Matrix: A new instance with original values.
        """
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, self.get_value(i, j))
        return result

    def __neg__(self) -> 'Matrix':
        """
        Unary - operator: returns a new Matrix with negated elements.

        Returns:
            Matrix: A new instance with negated values.
        """
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, -self.get_value(i, j))
        return result

    def __invert__(self) -> 'Matrix':
        """
        Unary ~ operator: returns a new Matrix with transposed elements.

        Returns:
            Matrix: A new instance representing the transposed matrix.
        """
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(j, i, self.get_value(i, j))
        return result

    def __round__(self, n: int = 0) -> 'Matrix':
        """
        Round elements of the Matrix to the specified number of decimal places.

        Args:
            n (int): Number of decimal places to round to, defaults to 0.

        Returns:
            Matrix: A new instance with rounded values.
        """
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, round(self.get_value(i, j), n))
        return result
