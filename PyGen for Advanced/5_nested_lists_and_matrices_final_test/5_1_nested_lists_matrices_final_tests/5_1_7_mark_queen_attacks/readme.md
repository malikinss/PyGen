# Queen's Attack on Chessboard ♛

## Description 📝

This program simulates a queen's position and captures on an 8x8 chessboard.
It marks the queen's position with a "Q", marks all the squares the queen can attack with "\*" symbols, and fills the rest of the board with dots (".").

## Purpose 🎯

-   Simulate a queen's movement and capture abilities on a chessboard.
-   Demonstrate board manipulation with rows, columns, and diagonals.

## How It Works 🔍

1. **Function `initialize_board()`**:
    - Initializes an 8x8 chessboard with all squares filled with dots (".").
2. **Function `get_queen_position()`**:

    - Reads the queen's position from input (e.g., "a1") and converts it to coordinates on the 8x8 board.

3. **Function `mark_queen_attacks()`**:

    - Marks the queen's position with "Q" and all the squares it can attack with "\*" (row, column, and diagonals).

4. **Function `print_board()`**:

    - Prints the chessboard in a readable format, with each square represented by a character.

5. **Function `main()`**:
    - Initializes the chessboard, gets the queen's position, marks attacks, and prints the final chessboard.

## Usage 📦

1. Run the script `queen_attack.py`.
2. Input the queen's position on the chessboard (e.g., "a1", "e5", etc.).
3. The program will print the chessboard with the queen's position and all attacked squares.

### Example:

```
Input: e4
Output:
. . . * * * * .
. . . * * * * .
. . * * * * * .
. * * * * * * .
* * * Q * * * *
. * * * * * * .
. . * * * * * .
. . . * * * * .
```

## Output 📜

-   The queen's position is marked with "Q".
-   The squares the queen can attack are marked with "\*".
-   All other squares are filled with dots (".").

## Conclusion 🚀

This program efficiently demonstrates how the queen moves and attacks in chess, marking the relevant squares and displaying them in a human-readable format.
