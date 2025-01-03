'''
TODO:
    There is a knight on an 8x8 chessboard.

    Write a program that marks the knight's position on the board and all
    the squares that the knight captures.

    Mark the square where the knight stands with the English letter N,
    and mark the squares that the knight captures with * symbols,
    and fill the remaining squares with dots.
'''


def mark_knight_moves(x: str, y: str) -> None:
    """
    Marks the knight's position and possible moves on an 8x8 chessboard.

    Args:
        x (str): The column position of the knight (a-h).
        y (str): The row position of the knight (1-8).

    Returns:
        None. Prints the board to the console.
    """
    n = 8
    board = [['.'] * n for _ in range(n)]

    # Convert coordinates to array indices
    col = ord(x) - 97  # Convert 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    row = n - int(y)   # Convert 1 -> 7, 8 -> 0

    # Place the knight on the board
    board[row][col] = 'N'

    # Possible knight moves
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    # Mark possible moves
    for dx, dy in knight_moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < n and 0 <= new_col < n:
            board[new_row][new_col] = '*'

    # Print the board
    for row in board:   # type: ignore
        print(*row)     # type: ignore


# Read knight's position from input
x, y = input()  # type: ignore
mark_knight_moves(x, y)  # type: ignore
