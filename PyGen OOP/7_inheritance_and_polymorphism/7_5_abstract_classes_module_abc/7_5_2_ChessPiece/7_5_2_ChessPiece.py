'''
TODO:
    Implement an abstract class ChessPiece that describes a chess piece.

    The class initializer must accept two arguments in the following order:
        horizontal — the coordinate of the piece along the horizontal axis,
                     represented by a Latin letter from a to h
        vertical — the coordinate of the piece along the vertical axis,
                   represented by an integer from 1 to 8 inclusive

    The ChessPiece class must have one instance method:
        can_move() — an empty abstract method

    Also implement the King class, a descendant of the ChessPiece class,
    describing the chess king.

    The process of creating an instance of the King class must coincide with
    the process of creating an instance of the ChessPiece class.

    The King class must have one instance method:
        can_move() — a method that takes horizontal and vertical chess
                     coordinates as arguments and returns True if the piece
                     can move along the specified coordinates, or False
                     otherwise

    An instance of the King class must have two attributes:
        horizontal — the piece's coordinate along the horizontal axis,
                     represented by a Latin letter from a to h
        vertical — the piece's coordinate along the vertical axis, represented
                   by an integer from 1 to 8 inclusive

    Finally, implement the Knight class, a descendant of the ChessPiece class,
    describing a chess knight.

    The process of creating an instance of the Knight class must coincide with
    the process of creating an instance of the ChessPiece class.

    The Knight class must have one instance method:
        can_move() — an overridden parent method that takes horizontal and
                     vertical coordinates as arguments and returns True if
                     the figure can move along the specified coordinates,
                     and False otherwise

    A Knight class instance must have two attributes:
        horizontal — the figure's coordinate along the horizontal axis,
                     represented by a Latin letter from a to h
        vertical — the figure's coordinate along the vertical axis,
                   represented by an integer from 1 to 8 inclusive

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding class implementations, they can be
    arbitrary.
'''
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    """
    Abstract base class for chess pieces.

    Defines piece coordinates and requires a can_move method.
    """

    def __init__(self, horizontal: str, vertical: int) -> None:
        """
        Initialize with horizontal and vertical coordinates.

        Args:
            horizontal: Letter from 'a' to 'h' for horizontal position.
            vertical: Integer from 1 to 8 for vertical position.
        """
        self.horizontal = horizontal
        self.vertical = vertical

    def _get_steps(self, to_hor: str, to_ver: int) -> tuple[int, int]:
        """
        Calculate absolute steps to target coordinates.

        Args:
            to_hor: Target horizontal coordinate ('a' to 'h').
            to_ver: Target vertical coordinate (1 to 8).

        Returns:
            Tuple of (horizontal steps, vertical steps).
        """
        hor_steps = abs(ord(to_hor) - ord(self.horizontal))
        ver_steps = abs(to_ver - self.vertical)
        return hor_steps, ver_steps

    @abstractmethod
    def can_move(self, to_hor: str, to_ver: int) -> bool:
        """
        Check if the piece can move to the specified coordinates.

        Args:
            to_hor: Target horizontal coordinate ('a' to 'h').
            to_ver: Target vertical coordinate (1 to 8).

        Returns:
            True if the move is valid, False otherwise.
        """
        pass


class King(ChessPiece):
    """
    Class representing a chess king.
    """

    def can_move(self, to_hor: str, to_ver: int) -> bool:
        """
        Check if the king can move to the specified coordinates.

        Args:
            to_hor: Target horizontal coordinate ('a' to 'h').
            to_ver: Target vertical coordinate (1 to 8).

        Returns:
            True if the king can move one square in any direction,
            False otherwise.
        """
        hor_steps, ver_steps = self._get_steps(to_hor, to_ver)
        not_same = (hor_steps, ver_steps) != (0, 0)
        return hor_steps <= 1 and ver_steps <= 1 and not_same


class Knight(ChessPiece):
    """
    Class representing a chess knight.
    """

    def can_move(self, to_hor: str, to_ver: int) -> bool:
        """
        Check if the knight can move to the specified coordinates.

        Args:
            to_hor: Target horizontal coordinate ('a' to 'h').
            to_ver: Target vertical coordinate (1 to 8).

        Returns:
            True if the knight can move in an L-shape, False otherwise.
        """
        hor_steps, ver_steps = self._get_steps(to_hor, to_ver)
        return (hor_steps, ver_steps) in [(1, 2), (2, 1)]
