'''
TODO:
    Implement a TicTacToe class for playing TicTacToe.

    A TicTacToe instance should represent a game board with three rows and
    three columns, on which players can take turns marking empty cells.

    The first move is made by the player who places crosses:
        tictactoe = TicTacToe()
        tictactoe.mark(1, 1)
        # mark the cell with coordinates (1; 1) with a cross
        tictactoe.mark(3, 1)
        # mark the cell with coordinates (3; 1) with a zero

    You cannot mark already marked cells.

    When attempting to do this, the text Inaccessible cell should be displayed:
        tictactoe.mark(1, 1) # Inaccessible cell
        tictactoe.mark(1, 3)
        # mark the cell with coordinates (1; 3) with a cross
        tictactoe.mark(1, 2)
        # mark the cell with coordinates (1; 2) with a zero
        tictactoe.mark(3, 3)
        # mark the cell with coordinates (3; 3) with a cross
        tictactoe.mark(2, 2)
        # mark the cell with coordinates (2; 2) with a zero
        tictactoe.mark(2, 3)
        # mark the cell with coordinates (2; 3) with a cross

    It should be possible to find out the winner of the game using
    the winner() method.
    The method should return:
        the character X if the player who puts crosses wins
        the character O if the player who puts noughts wins
        the string Draw if there is a draw
        the value None if the winner has not yet been determined
        print(tictactoe.winner()) # X

    You cannot mark cells after the game has ended.

    Attempts to do so should print the text Game over:
        tictactoe.mark(2, 1) # Game over

    The show() method should be able to show the current state of the game
    board.

    It should be built from the | and - characters, as well as X and O if any
    moves have been made by the players.

    For the tictactoe board above, calling tictactoe.show() should print
    the following:
        X|O|X
        -----
        |O|X
        -----
        O| |X
'''
from typing import List, Optional


class TicTacToe:
    """
    Class for playing TicTacToe on a 3x3 board.
    """
    def __init__(self) -> None:
        """
        Initialize empty 3x3 board with X as first player."""
        self.board: List[List[str]] = [[' ', ' ', ' '] for _ in range(3)]
        self._marks = ['X', 'O']
        self._current = 0

    def mark(self, x: int, y: int) -> None:
        """
        Mark cell (x, y) with X or O if valid.

        Args:
            x: Row coordinate (1-based).
            y: Column coordinate (1-based).
        """
        if self.winner():
            print('Игра окончена')
        elif self.board[x-1][y-1] != ' ':
            print('Недоступная клетка')
        else:
            self.board[x-1][y-1] = self._marks[self._current]
            self._current = (self._current + 1) % 2

    def winner(self) -> Optional[str]:
        """
        Return game result: 'X', 'O', 'Draw', or None.

        Returns:
            'X' or 'O' if a player wins, 'Draw' if full, else None.
        """
        # Check rows, columns, diagonals for winner
        win = self._is_winner()
        if win:
            return win
        return 'Ничья' if not self._is_spare() else None

    def show(self) -> None:
        """
        Display current board state.
        """
        for i, row in enumerate(self.board):
            print('|'.join(row))
            if i < 2:
                print('-' * 5)

    def _is_winner(self) -> Optional[str]:
        """
        Check if there is a winner.

        Returns:
            'X' or 'O' if a player wins, else None.
        """
        for i in range(3):
            if self._is_row(i):
                return self.board[i][0]
            if self._is_col(i):
                return self.board[0][i]
        if self._is_main_diagonal() or self._is_side_diagonal():
            return self.board[1][1]
        return None

    def _is_spare(self) -> bool:
        """
        Check if board has empty cells.

        Returns:
            True if there are empty cells, else False.
        """
        return any(' ' in row for row in self.board)

    @staticmethod
    def _has_same_values(values: List[str]) -> bool:
        """
        Check if all values are same and non-empty.

        Args:
            values: List of cell values.

        Returns:
            True if all values are identical and non-empty, else False.
        """
        return values[0] != ' ' and len(set(values)) == 1

    def _is_row(self, row: int) -> bool:
        """
        Check if row has same non-empty values.

        Args:
            row: Row index.

        Returns:
            True if row is same and non-empty, else False.
        """
        return self._has_same_values(self.board[row])

    def _is_col(self, col: int) -> bool:
        """
        Check if column has same non-empty values.

        Args:
            col: Column index.

        Returns:
            True if column is same and non-empty, else False.
        """
        values = [self.board[i][col] for i in range(3)]
        return self._has_same_values(values)

    def _is_main_diagonal(self) -> bool:
        """
        Check if main diagonal has same non-empty values.

        Returns:
            True if diagonal is same and non-empty, else False.
        """
        values = [self.board[i][i] for i in range(3)]
        return self._has_same_values(values)

    def _is_side_diagonal(self) -> bool:
        """
        Check if side diagonal has same non-empty values.

        Returns:
            True if diagonal is same and non-empty, else False.
        """
        values = [self.board[i][2-i] for i in range(3)]
        return self._has_same_values(values)
