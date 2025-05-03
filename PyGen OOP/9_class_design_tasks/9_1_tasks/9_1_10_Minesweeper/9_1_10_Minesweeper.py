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
