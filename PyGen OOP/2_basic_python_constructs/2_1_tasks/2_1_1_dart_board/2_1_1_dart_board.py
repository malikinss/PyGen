'''
TODO:
    We will assume that the playing field for darts is a square matrix filled
    with natural numbers arranged in ascending order from the edges to
    the center.

    The side of the playing field is the side of the square matrix that this
    field represents.

    Write a program that creates a darts field of a certain size.

    The program receives a single natural number as input — the side of the
    playing field.

    The program must create and output a playing field with a given side.

NOTE:
    It is guaranteed that the side of the playing field does not exceed 18.
'''


def display_dart_board(board: list[list[int]]) -> None:
    """
    Prints the dart board row by row.

    Args:
        board (list[list[int]]): The dart board matrix to display.
    """
    for row in board:
        print(" ".join(map(str, row)))


def calculate_distance_to_edges(row: int, col: int, size: int) -> int:
    """
    Calculate the minimum distance from the given cell to any edge of
    the dartboard.

    Args:
        row (int): The row number of the cell.
        col (int): The column number of the cell.
        size (int): The size of the dartboard (side of the square matrix).

    Returns:
        int: The minimum distance from the given cell to any edge.
    """
    top = row - 1
    bottom = size - row
    left = col - 1
    right = size - col

    return min(top, bottom, left, right)


def create_dart_board(size: int) -> list[list[int]]:
    """
    Creates a square dart board matrix with natural numbers arranged in
    ascending order from the edges to the center.

    Args:
        size (int): The size of the dart board (side of the square matrix).

    Returns:
        list[list[int]]: The generated dart board matrix.
    """
    board = []

    for row in range(1, size + 1):
        row_values = []

        for col in range(1, size + 1):
            # Calculate the minimum distance to the edge
            min_distance = calculate_distance_to_edges(row, col, size) + 1
            row_values.append(min_distance)

        board.append(row_values)

    return board


if __name__ == "__main__":
    darts = create_dart_board(int(input()))
    display_dart_board(darts)
