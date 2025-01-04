'''
TODO:
    Write a program to calculate the sum of two matrices.
'''
from typing import List, Tuple


def get_matrix_size() -> Tuple[int, int]:
    """
    Reads the size of the matrices from the user input.

    Returns:
        Tuple[int, int]: The number of rows (n) and columns (m)
                         for the matrices.
    """
    s = input("Enter the number of rows and columns (n m): ").split()
    n = int(s[0])
    m = int(s[1])

    return n, m


def list_convert_to_int_in_place(columns: int, row: List[str]) -> List[int]:
    """
    Converts a list of strings representing a row of the matrix to integers.

    Args:
        columns (int): The number of columns in the matrix.
        row (List[str]): The row represented as a list of strings.

    Returns:
        List[int]: The row represented as a list of integers.
    """
    for cur_column in range(columns):
        row[cur_column] = int(row[cur_column])  # type: ignore

    return row  # type: ignore


def get_int_row(columns: int) -> List[int]:
    """
    Reads a row of integers from the user input.

    Args:
        columns (int): The number of columns in the row.

    Returns:
        List[int]: A list of integers representing the row.
    """
    row = input("Enter row values separated by space: ").split()
    row = list_convert_to_int_in_place(columns, row)  # type: ignore

    return row  # type: ignore


def get_matrix(rows: int, columns: int) -> List[List[int]]:
    """
    Reads a matrix from the user input.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: A matrix represented as a list of rows.
    """
    new_matrix = []

    for i in range(rows):
        row = get_int_row(columns)
        new_matrix.append(row)

    return new_matrix


def sum_of_two_matrices(
    matrix1: List[List[int]], matrix2: List[List[int]], rows: int, columns: int
) -> List[List[int]]:
    """
    Sums two matrices of the same size.

    Args:
        matrix1 (List[List[int]]): The first matrix to sum.
        matrix2 (List[List[int]]): The second matrix to sum.
        rows (int): The number of rows in the matrices.
        columns (int): The number of columns in the matrices.

    Returns:
        List[List[int]]: The resulting matrix, which is the sum of the
                         two matrices.
    """
    result_matrix = []

    for i in range(rows):
        result_row = []

        for j in range(columns):
            result_value = matrix1[i][j] + matrix2[i][j]
            result_row.append(result_value)

        result_matrix.append(result_row)

    return result_matrix


def print_matrix(matrix: List[List[int]], rows: int) -> None:
    """
    Prints the matrix row by row.

    Args:
        matrix (List[List[int]]): The matrix to print.
        rows (int): The number of rows in the matrix.
    """
    for i in range(rows):
        print(*matrix[i])


def main() -> None:
    """
    Main function to drive the program. It reads the matrices, sums them,
    and prints the result.
    """
    # Step 1: Get matrix size from the user
    n, m = get_matrix_size()

    # Step 2: Get the first matrix from the user
    matrix1 = get_matrix(n, m)

    # Step 3: Skip an empty line between matrices
    input("Press Enter to continue to the second matrix...")

    # Step 4: Get the second matrix from the user
    matrix2 = get_matrix(n, m)

    # Step 5: Calculate the sum of the two matrices
    result = sum_of_two_matrices(matrix1, matrix2, n, m)

    # Step 6: Print the result
    print("Resulting matrix:")
    print_matrix(result, n)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
