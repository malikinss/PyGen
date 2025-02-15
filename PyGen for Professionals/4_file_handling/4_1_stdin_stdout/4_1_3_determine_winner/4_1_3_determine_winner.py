'''
TODO:
    Anri and Dima, having a box with an endless number of socks on their hands,
    decided to play a game.

    The guys take turns taking an arbitrary number of socks out of the box,
    and after an indefinite number of moves the game ends.

    If the one who made the last move drew an even number of socks, he wins,
    otherwise he loses.

    Write a program that determines the winner of this game if Anri makes the
    first move.
'''
import sys
from typing import List

PLAYERS = ['ANRI', 'DIMA']


def get_next_player(moves: List[int]) -> str:
    """
    Determines the next player based on the last move.

    Args:
        moves (List[int]): A list of all previous moves.

    Returns:
        str: The name of the next player.
    """
    if get_last_player(moves) == PLAYERS[1]:
        return PLAYERS[0]
    elif get_last_player(moves) == PLAYERS[0]:
        return PLAYERS[1]
    return ''


def get_last_player(moves: List[int]) -> str:
    """
    Determines the last player who made a move.

    Args:
        moves (List[int]): A list of all previous moves.

    Returns:
        str: The name of the last player.
    """
    if len(moves) % 2 == 0:
        return PLAYERS[1]
    return PLAYERS[0]


def is_win(move: int) -> bool:
    """
    Determines if the player who made this move won.

    Args:
        move (int): The number of socks drawn in the last move.

    Returns:
        bool: True if the move is even, indicating a win; False otherwise.
    """
    return move % 2 == 0


def get_moves_values() -> List[int]:
    """
    Reads the input and returns a list of the moves made during the game.

    Returns:
        List[int]: A list of integers representing the number of socks drawn
                   in each move.
    """
    return [int(line.strip()) for line in sys.stdin.readlines()]


def determine_winner() -> None:
    """
    Determines the winner of the game based on the last move made.

    If the last move was even, the player who made it wins; otherwise,
    the opponent wins.
    """
    moves_values = get_moves_values()

    if is_win(moves_values[-1]):
        print(get_last_player(moves_values))
    else:
        print(get_next_player(moves_values))


determine_winner()
