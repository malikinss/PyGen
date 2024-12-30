'''
TODO:
    The input to the program is two natural numbers n and m - the number
    of rows and columns in the matrix, then n rows with m integers in each,
    separated by a space character.

    Write a program that finds the indices (row and column) of the
    first occurrence of the maximum element.

NOTE:
    Assume that the numbering of rows and columns starts from zero.
'''


def find_max_element_indices(
    n: int, m: int, matrix: list[list[int]]
) -> tuple[int, int]:
    """
    Finds the indices (row and column) of the first occurrence of the maximum
    element in a matrix.

    Args:
        n (int): Number of rows in the matrix.
        m (int): Number of columns in the matrix.
        matrix (list[list[int]]): The matrix of integers.

    Returns:
        tuple[int, int]: Indices (row, column) of the first occurrence
        of the maximum element.
    """
    row, col = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > matrix[row][col]:
                row, col = i, j
    return row, col


def main() -> None:
    """
    Main function to read input, find the maximum element's indices,
    and print them.
    """
    n: int = int(input())  # Number of rows
    m: int = int(input())  # Number of columns

    matrix: list[list[int]] = [
        list(map(int, input().split())) for _ in range(n)
    ]

    row, col = find_max_element_indices(n, m, matrix)
    print(row, col)


if __name__ == "__main__":
    main()
