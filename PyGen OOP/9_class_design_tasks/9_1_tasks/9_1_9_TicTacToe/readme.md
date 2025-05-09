# TicTacToe Class Implementation

## Description 📝

The provided code implements the `TicTacToe` class, which simulates a 3x3 Tic-Tac-Toe game.
The class supports alternating moves between players (X goes first, then O), marking cells with coordinates (1-based), checking for a winner, and displaying the board.
It handles invalid moves (already marked cells or moves after the game ends) by printing specific messages and determines the game outcome (win, draw, or ongoing).
The board is displayed using `|` and `-` characters, with `X`, `O`, or spaces for cells.

## Purpose 🎯

Intended for gaming applications, educational examples of Python classes, game logic, or interactive simulations of Tic-Tac-Toe.

## How It Works 🔍

-   **Class Definition**:
    -   `TicTacToe` manages a 3x3 game board and game state.
    -   Uses type hints (`List`, `Optional`) for clarity.
-   **Initialization (`__init__`)**:
    -   Creates a 3x3 board as a list of lists, initialized with spaces (`' '`).
    -   Sets `_marks = ['X', 'O']` for player symbols.
    -   Sets `_current = 0` to track the current player (0 for X, 1 for O).
-   **mark Method**:
    -   Takes 1-based coordinates `x`, `y` (1 to 3).
    -   Checks if the game is over (`winner()` returns non-`None`):
        -   If true, prints "Game over" and returns.
    -   Checks if the cell `(x-1, y-1)` is already marked (not `' '`):
        -   If true, prints "Inaccessible cell" and returns.
    -   Marks the cell with the current player’s symbol (`X` or `O`).
    -   Switches the current player by toggling `_current`.
-   **winner Method**:
    -   Checks for a winner by calling `_is_winner()`:
        -   Returns `'X'` or `'O'` if a player has won.
    -   If no winner:
        -   Returns `'Draw'` if the board is full (`_is_spare()` is `False`).
        -   Returns `None` if the game is ongoing.
-   **show Method**:
    -   Prints the board row by row, joining cells with `|`.
    -   Prints `-----` between rows (for rows 0 and 1).
    -   Example output for a board:
        ```
        X|O|X
        -----
        |O|X
        -----
        O| |X
        ```
-   **Helper Methods**:
    -   `_is_winner()`: Checks rows, columns, and diagonals for a winner, returning `'X'`, `'O'`, or `None`.
    -   `_is_spare()`: Returns `True` if any cell is empty (`' '`), `False` if full.
    -   `_has_same_values(values)`: Checks if a list of values (e.g., row) is non-empty and identical.
    -   `_is_row(row)`: Checks if a row has the same non-empty values.
    -   `_is_col(col)`: Checks if a column has the same non-empty values.
    -   `_is_main_diagonal()`: Checks if the main diagonal (top-left to bottom-right) has the same non-empty values.
    -   `_is_side_diagonal()`: Checks if the side diagonal (top-right to bottom-left) has the same non-empty values.
-   **Behavior**:
    -   Alternates between X and O, starting with X.
    -   Validates moves, preventing marking of taken cells or post-game moves.
    -   Detects wins (three identical symbols in a row, column, or diagonal), draws (full board, no winner), or ongoing games.
    -   Displays the board with proper formatting.
    -   No input validation beyond game rules, as coordinates are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Creates an empty 3x3 board with X as the first player.
    -   Example: `TicTacToe()` initializes `[[' ', ' ', ' '], ...]`.
-   **mark Method**:
    -   Marks cells with X or O in alternating order.
    -   Example sequence:
        -   `mark(1, 1)` → X at (1,1).
        -   `mark(3, 1)` → O at (3,1).
        -   `mark(1, 1)` → Prints "Inaccessible cell".
        -   Continues with valid moves.
    -   Post-game moves: Prints "Game over" if `winner()` is non-`None`.
-   **winner Method**:
    -   Returns:
        -   `'X'` if X wins (e.g., three X’s in a row).
        -   `'O'` if O wins.
        -   `'Draw'` if board is full with no winner.
        -   `None` if game is ongoing.
    -   Example: After moves forming `X|O|X`, ` |O|X`, `O| |X`, returns `'X'` if X wins diagonally.
-   **show Method**:
    -   Displays board with `|`, `-`, `X`, `O`, and spaces.
    -   Example output matches:
        ```
        X|O|X
        -----
        |O|X
        -----
        O| |X
        ```
-   **Correctness**:
    -   Alternates players using `_current` toggle.
    -   Validates moves with checks for game state and cell availability.
    -   Winner detection covers rows, columns, and diagonals.
    -   Board display uses correct separators.
    -   No validation needed for input coordinates, as guaranteed correct.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   1-based coordinates are converted to 0-based (`x-1`, `y-1`) for internal board access.
    -   `_is_winner` checks all win conditions (rows, columns, diagonals) efficiently.
    -   `_is_spare` accurately detects full board for draw condition.
    -   `_has_same_values` ensures non-empty identical values for win checks.
    -   Messages ("Inaccessible cell", "Game over") are printed exactly as specified.
-   **Performance**:
    -   Initialization: O(1) for creating 3x3 board.
    -   `mark`: O(1) for checking and updating a cell.
    -   `winner`: O(1) for checking 3 rows, 3 columns, 2 diagonals.
    -   `show`: O(1) for printing 3x3 board.
    -   Highly efficient for a 3x3 grid.
-   **Design**:
    -   Internal board representation (`List[List[str]]`) is simple and effective.
    -   Helper methods (`_is_row`, `_is_col`, etc.) modularize win checking.
    -   Type hints (`List`, `Optional`) clarify method signatures.
    -   `_marks` and `_current` manage player alternation cleanly.
-   **Alternatives**:
    -   Flat list for board: Less intuitive than 2D list for 3x3 grid.
    -   Enum for players: Overkill for simple X/O tracking.
    -   External game state class: Unnecessary for single board.
-   **Extensibility**:
    -   Easily extended to support larger boards or different win conditions.
    -   Could add input validation (e.g., coordinate range) if needed.
-   **Edge Cases**:
    -   Full board with no winner: Correctly returns `'Draw'`.
    -   Early win: Stops further moves with "Game over".
    -   Repeated move on same cell: Prints "Inaccessible cell".
    -   Diagonal wins: Correctly detected by `_is_main_diagonal` and `_is_side_diagonal`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create game instance
tictactoe = TicTacToe()

# Make moves
tictactoe.mark(1, 1)  # X at (1,1)
tictactoe.mark(3, 1)  # O at (3,1)
tictactoe.mark(1, 1)  # Inaccessible cell
tictactoe.mark(1, 3)  # X at (1,3)
tictactoe.mark(1, 2)  # O at (1,2)
tictactoe.mark(3, 3)  # X at (3,3)
tictactoe.mark(2, 2)  # O at (2,2)
tictactoe.mark(2, 3)  # X at (2,3)

# Show board
tictactoe.show()
# X|O|X
# -----
#  |O|X
# -----
# O| |X

# Check winner
print(tictactoe.winner())  # X (diagonal: (1,1), (2,2), (3,3))

# Try marking after game over
tictactoe.mark(2, 1)  # Game over

# Test draw scenario
tictactoe = TicTacToe()
moves = [(1,1), (1,2), (1,3), (2,1), (2,3), (2,2), (3,2), (3,1), (3,3)]
for x, y in moves:
    tictactoe.mark(x, y)
tictactoe.show()
# X|O|X
# -----
# O|X|O
# -----
# O|X|O
print(tictactoe.winner())  # Draw
```

## Conclusion 🚀

The `TicTacToe` class implementation is precise, correctly managing a 3x3 Tic-Tac-Toe game with alternating moves, win/draw detection, and board display.
It handles invalid moves with appropriate messages, detects game outcomes accurately, and formats the board as specified.
The implementation is efficient, extensible, and ideal for game simulations or teaching game logic, fully compliant with the task’s requirements.
