'''
TODO:
    Implement a Knight class that describes a chess knight.

    When creating an instance, the class must accept three arguments in the
    following order:
        - horizontal — the knight's coordinate along the horizontal axis,
                       represented by a Latin letter from a to h
        - vertical — the knight's coordinate along the vertical axis,
                     represented by an integer from 1 to 8 inclusive
        - color — the knight's color (black or white)

    An instance of the Knight class must have three attributes:
        - horizontal — the knight's coordinate on the chessboard along
                       the horizontal axis
        - vertical — the knight's coordinate on the chessboard along
                     the vertical axis
        - color — the knight's color

    The Knight class must have four instance methods:
        - get_char() — a method that returns the character N
        - can_move() — a method that accepts the cell's coordinates along
                       the horizontal and vertical axes as arguments and
                       returns True if the knight can move to the cell with
                       these coordinates, or False otherwise
        - move_to() — a method that accepts the cell's coordinates along
                      the horizontal and vertical axes as arguments and
                      replaces the current coordinates knight to the passed
                      ones.
                      If the knight from the current cell cannot move to the
                      cell with the specified coordinates, its coordinates
                      should remain unchanged
        - draw_board() — a method that prints a chessboard, marking the knight
                         on this board and the cells to which the knight can
                         move.
                         Empty cells should be displayed as ., the knight as N,
                         and the cells to which the knight can move as *

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.
'''
from typing import List, Tuple

BOARD_SIZE = 8


class Knight:
    """A class representing a chess knight piece on an 8x8 chessboard.

    This class encapsulates the properties and behaviors of a knight,
    including its position (horizontal and vertical coordinates) and color.

    It provides methods to check possible moves, update its position, and
    visualize its state on a chessboard.

    The knight moves in an L-shape:
        two squares in one direction and one perpendicular, or vice versa.

    Attributes:
        horizontal (str): The knight's horizontal position, a letter from 'a'
            to 'h' representing columns 1 to 8.
        vertical (int): The knight's vertical position, an integer from 1 to 8
            representing rows from bottom to top.
        color (str): The knight's color, either 'black' or 'white'.
        EMPTY (str): Symbol used for empty cells on the board ('.').
        MOVE (str): Symbol marking cells the knight can move to ('*').
        KNIGHT (str): Symbol representing the knight's position ('N').
    """

    EMPTY = '.'
    MOVE = '*'
    KNIGHT = 'N'

    def __init__(self, horizontal: str, vertical: int, color: str) -> None:
        """
        Initialize a Knight instance with its starting position and color.

        Sets up the knight with the specified coordinates and color, storing
        them as instance attributes.

        The horizontal coordinate is a letter, and the vertical coordinate is
        an integer, mapping to a standard chessboard layout.

        Args:
            horizontal (str): A single Latin letter from 'a' to 'h' indicating
                the column (e.g., 'a' is column 1, 'h' is column 8).
            vertical (int): An integer from 1 to 8 indicating the row, where
                1 is the bottom row and 8 is the top row.
            color (str): The knight's color, either 'black' or 'white'.

        Returns:
            None
        """
        self.horizontal: str = horizontal
        self.vertical: int = vertical
        self.color: str = color

    def _to_indices(self, horizontal: str, vertical: int) -> Tuple[int, int]:
        """
        Convert chess coordinates to 0-based board indices.

        Transforms the knight's standard chess notation (e.g., 'a' and 1)
        into 0-based indices for internal use, where 'a' becomes 0 and
        1 becomes 7 (top row is 0).

        Args:
            horizontal (str): A letter from 'a' to 'h' for the column.
            vertical (int): An integer from 1 to 8 for the row.

        Returns:
            tuple[int, int]: A tuple (y, x) where y is the row index (0-7)
                and x is the column index (0-7).
        """
        x = ord(horizontal) - 97  # Convert 'a'-'h' to 0-7
        y = BOARD_SIZE - vertical  # Convert 1-8 to 0-7
        return (y, x)

    def get_char(self) -> str:
        """
        Return the character symbol representing the knight.

        Provides the standard chess notation symbol for a knight, which is 'N'.

        This is used for visualization purposes, such as in the draw_board
        method.

        Returns:
            str: The character 'N' representing the knight.
        """
        return self.KNIGHT

    def _get_possible_moves(self) -> List[Tuple[int, int]]:
        """
        Calculate and return all possible moves the knight can make.

        Generates a list of coordinates (row, column) that the knight can
        legally reach from its current position, following the knight's
        L-shaped movement pattern: (±1, ±2) or (±2, ±1).

        Coordinates are returned in internal 0-based indices (0-7).

        Returns:
            list[tuple[int, int]]: A list of tuples, each containing
            (row, column) coordinates where the knight can move.
            Row and column are 0-based.
        """
        y, x = self._to_indices(self.horizontal, self.vertical)

        # Knight's possible moves: (±1, ±2) or (±2, ±1)
        offsets = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        possible_moves = []

        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
                possible_moves.append((new_y, new_x))

        return possible_moves

    def can_move(self, horizontal: str, vertical: int) -> bool:
        """
        Determine if the knight can move to the specified coordinates.

        Checks whether the given position is a valid move for the knight from
        its current location, based on the knight's movement rules.

        The target coordinates are converted to internal indices for
        comparison.

        Args:
            horizontal (str): Target horizontal coordinate, a letter from 'a'
                to 'h'.
            vertical (int): Target vertical coordinate, an integer from 1 to 8.

        Returns:
            bool: True if the knight can move to the specified cell,
            False otherwise.
        """
        y, x = self._to_indices(horizontal, vertical)

        return (y, x) in self._get_possible_moves()

    def move_to(self, horizontal: str, vertical: int) -> None:
        """
        Move the knight to the specified coordinates if the move is valid.

        Updates the knight's position to the new coordinates only if the move
        is legal according to the knight's movement rules.

        If the move is not possible, the knight's position remains unchanged.

        Args:
            horizontal (str): New horizontal coordinate, a letter from
            'a' to 'h'.
            vertical (int): New vertical coordinate, an integer from 1 to 8.

        Returns:
            None
        """
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def _get_empty_board(self) -> List[List[str]]:
        """
        Create and return an empty 8x8 chessboard.

        Generates a 2D list filled with the EMPTY symbol ('.') to represent
        an initial blank chessboard.

        Returns:
            list[list[str]]: An 8x8 grid of strings, all initialized to '.'.
        """
        return [[self.EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def draw_board(self) -> None:
        """
        Visualize the chessboard with the knight and its possible moves.

        Prints an 8x8 grid representing the chessboard, where the knight's
        current position is marked with 'N', cells it can move to are marked
        with '*', and all other cells are marked with '.'.

        The board is oriented with row 8 at the top and column 'a' on the left.

        Returns:
            None
        """
        y, x = self._to_indices(self.horizontal, self.vertical)
        moves = set(self._get_possible_moves())
        board = self._get_empty_board()

        board[y][x] = self.KNIGHT

        for move_y, move_x in moves:
            board[move_y][move_x] = self.MOVE

        for row in board:
            print(*row, sep='')
