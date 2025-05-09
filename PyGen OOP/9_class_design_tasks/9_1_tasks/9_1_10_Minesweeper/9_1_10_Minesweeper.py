'''
TODO:
    In this task, you need to implement a Minesweeper board as two classes,
    Game and Cell.

    The first class instance will describe the board itself, and the Cell
    instance will describe one of its cells.

    The Game class instance should be created based on three values:
        the number of rows (the board length),
        the number of columns (the board width),
        and the total number of mines on the board:
            game = Game(14, 18, 40) # 14 rows, 18 columns, and 40 mines

    The number of rows and columns, as well as the total number of mines,
    should be available via the corresponding attributes:
        print(game.rows) # 14
        print(game.cols) # 18
        print(game.mines) # 40

    The Game class instance should also have a board attribute, which
    represents the board as a two-dimensional list.

    The number of sublists in this list should match the number of rows,
    and the number of elements in the sublists should match the number of
    columns.

    Each element of the sublist must be an instance of the Cell class and have
    the corresponding set of attributes:
        cell = game.board[0][0]
        print(cell.row) # 0; cell row
        print(cell.col) # 0; cell column
        print(cell.mine)
        # True or False depending on whether the cell contains a mine or not
        print(cell.neighbours)
        # a number from 0 to 8, the number of mines in neighboring cells

    The game board should be filled with mines randomly when created.

NOTE:
    To check that the Cell class instance stores the correct number of mines
    in neighboring cells, in one of the tests we use our own function
    get_neighbours_count(), which counts this number.
'''
import random
from typing import List


class Game:
    """
    Class representing a Minesweeper game board.
    """
    def __init__(
        self, rows: int, cols: int, mines: int
    ) -> None:
        """
        Initialize board with rows, cols, and mines.

        Args:
            rows: Number of rows.
            cols: Number of columns.
            mines: Number of mines.
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self._init_board()

    def _init_board(self) -> List[List['Cell']]:
        """
        Create board with mines and neighbours.

        Returns:
            2D list of Cell instances.
        """
        board = self._create_empty_board()
        self._place_mines(board)
        for row in board:
            for cell in row:
                cell._init_neighbours(board, self.rows, self.cols)
        return board

    def _create_empty_board(self) -> List[List['Cell']]:
        """
        Create board with no mines.

        Returns:
            2D list of Cell instances with mine=False.
        """
        return [
            [Cell(i, j) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def _place_mines(
        self, board: List[List['Cell']]
    ) -> None:
        """
        Place mines randomly on the board.

        Args:
            board: 2D list of Cell instances.
        """
        # Randomly select mine positions
        positions = random.sample(
            [
                (i, j)
                for i in range(self.rows)
                for j in range(self.cols)
            ],
            self.mines
        )
        for i, j in positions:
            board[i][j].mine = True


class Cell:
    """
    Class representing a cell on the Minesweeper board."""
    def __init__(
        self, row: int, col: int, mine: bool = False,
    ) -> None:
        """
        Initialize cell with position and mine status.

        Args:
            row: Row index (0-based).
            col: Column index (0-based).
            mine: True if cell has a mine, else False.
                  False by default.
        """
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0

    def _init_neighbours(
        self,
        board: List[List['Cell']],
        rows: int, cols: int
    ) -> None:
        """
        Count and set number of mines in neighbouring cells.

        Args:
            board: 2D list of Cell instances.
            rows: Number of board rows.
            cols: Number of board columns.
        """
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = self.row + di, self.col + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if board[ni][nj].mine:
                        count += 1
        self.neighbours = count
