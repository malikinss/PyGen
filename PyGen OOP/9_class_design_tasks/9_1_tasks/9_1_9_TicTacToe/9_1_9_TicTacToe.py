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
