'''
TODO:
    There is a queen on an 8x8 chessboard.

    Mark the queen's position on the board and all the squares that
    the queen captures.

    Mark the square where the queen stands with the letter Q, mark the squares
    that the queen captures with * symbols, and fill the rest of the squares
    with dots.
'''
from typing import List, Tuple


def initialize_board(size: int = 8) -> List[List[str]]:
    """
    Initializes an 8x8 chessboard with all squares filled with dots.

    Args:
        size (int): Size of the chessboard (default is 8x8).

    Returns:
        List[List[str]]: Initialized chessboard.
    """
    return [["."] * size for _ in range(size)]


def get_queen_position() -> Tuple[int, int]:
    """
    Reads the queen's position from input and converts it to board coordinates.

    Returns:
        Tuple[int, int]: Coordinates (x, y) representing the queen's position.
    """
    coordinate = input()
    x = coordinate[0]
    y = coordinate[1]

    row = 8 - int(y)
    column = ord(x) - ord('a')
    return column, row


def mark_queen_attacks(
    board: List[List[str]], x: int, y: int, size: int = 8
) -> None:
    """
    Marks the queen's position and all the squares it can capture
    on the chessboard.

    Args:
        board (List[List[str]]): The chessboard to modify.
        x (int): The column where the queen is placed (0 to 7).
        y (int): The row where the queen is placed (0 to 7).
        size (int): Size of the chessboard (default is 8x8).
    """
    for i in range(size):
        # Mark row and column
        board[y][i] = "*"
        board[i][x] = "*"

        # Mark diagonals
        if 0 <= y + (x - i) < size:
            board[y + (x - i)][i] = "*"
        if 0 <= y - (x - i) < size:
            board[y - (x - i)][i] = "*"

    # Place the queen at the correct position
    board[y][x] = "Q"


def print_board(board: List[List[str]]) -> None:
    """
    Prints the chessboard in a readable format.

    Args:
        board (List[List[str]]): The chessboard to print.
    """
    for row in board:
        print(" ".join(row))


def main() -> None:
    """
    Main function to initialize the board, place the queen, mark attacks,
    and print the result.
    """
    board = initialize_board()
    x, y = get_queen_position()
    mark_queen_attacks(board, x, y)
    print_board(board)


if __name__ == "__main__":
    main()
