'''
TODO:
    Write a program that multiplies two matrices.
'''
from typing import List, Tuple


def get_matrix_size() -> Tuple[int, int]:
    """
    Reads the size of the matrix from user input (rows and columns).

    Returns:
        Tuple[int, int]: A tuple containing the number of rows and columns.
    """
    rows, columns = map(int, input("Enter rows and columns: ").split())
    return rows, columns


def list_convert_to_int_in_place(columns: int, row: List[str]) -> List[int]:
    """
    Converts a list of strings representing a row into a list of integers.

    Args:
        columns (int): The number of columns in the matrix.
        row (List[str]): The list of strings representing a row in the matrix.

    Returns:
        List[int]: The row represented as a list of integers.
    """
    for cur_column in range(columns):
        row[cur_column] = int(row[cur_column])  # type: ignore

    return row  # type: ignore


def get_int_row(columns: int) -> List[int]:
    """
    Reads a row of integers from user input.

    Args:
        columns (int): The number of columns in the row.

    Returns:
        List[int]: The list of integers representing the row.
    """
    row = input("Enter row values separated by space: ").split()
    row = list_convert_to_int_in_place(columns, row)  # type: ignore

    return row  # type: ignore


def get_matrix(rows: int, columns: int) -> List[List[int]]:
    """
    Reads a matrix from user input.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: The matrix represented as a list of rows.
    """
    new_matrix = []

    for i in range(rows):
        row = get_int_row(columns)
        new_matrix.append(row)

    return new_matrix


def matrix_multiplication(
    matrix1: List[List[int]], matrix2: List[List[int]],
    rows1: int, rows2: int, columns1: int, columns2: int
) -> List[List[int]]:
    """
    Multiplies two matrices and returns the resulting matrix.

    Args:
        matrix1 (List[List[int]]): The first matrix.
        matrix2 (List[List[int]]): The second matrix.
        rows1 (int): The number of rows in matrix1.
        rows2 (int): The number of rows in matrix2.
        columns1 (int): The number of columns in matrix1.
        columns2 (int): The number of columns in matrix2.

    Returns:
        List[List[int]]: The resulting matrix after multiplication.
    """
    result_matrix = []

    # Perform matrix multiplication
    for i in range(rows1):
        result_row = []
        for j in range(columns2):
            value = 0
            for k in range(columns1):
                value += matrix1[i][k] * matrix2[k][j]
            result_row.append(value)
        result_matrix.append(result_row)

    return result_matrix


def print_matrix(matrix: List[List[int]], rows: int) -> None:
    """
    Prints the matrix in a readable format.

    Args:
        matrix (List[List[int]]): The matrix to print.
        rows (int): The number of rows in the matrix.
    """
    for i in range(rows):
        print(*matrix[i])


def main() -> None:
    """
    Main function that drives the program: reads matrices, multiplies them,
    and prints the result.
    """
    # Step 1: Get matrix sizes from user input
    rows1, columns1 = get_matrix_size()

    # Step 2: Get the first matrix
    matrix1 = get_matrix(rows1, columns1)

    # Step 3: Get the second matrix size
    # and validate multiplication compatibility
    rows2, columns2 = get_matrix_size()

    # Check if multiplication is possible
    if columns1 != rows2:
        print("Matrix multiplication is not possible.")
        print("Columns of matrix 1 must equal rows of matrix 2.")
        return

    # Step 4: Get the second matrix
    matrix2 = get_matrix(rows2, columns2)

    # Step 5: Perform matrix multiplication
    result = matrix_multiplication(
        matrix1,
        matrix2,
        rows1,
        rows2,
        columns1,
        columns2
    )

    # Step 6: Print the result matrix
    print("Resulting matrix:")
    print_matrix(result, rows1)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
