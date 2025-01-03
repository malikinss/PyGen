# Knight's Moves on Chessboard ♞

## Description 📝

This program simulates a knight's possible moves on an 8x8 chessboard.
It marks the knight's current position and highlights all the squares that the knight can capture from its current position.

## Purpose 🎯

The goal is to visualize the knight's movement on a chessboard by:

-   Placing the knight at a specified position.
-   Marking the knight's position with the letter `N`.
-   Highlighting squares the knight can move to with the symbol `*`.
-   Filling the remaining squares with dots `.`.

## How It Works 🔍

1. The program takes the knight's initial position as input in the form of standard chess notation (e.g., `d5`).
2. The board is represented by an 8x8 grid.
3. The knight's possible moves are calculated using the standard movement pattern of two squares in one direction and one square in a perpendicular direction.
4. The program marks the knight's position and possible moves on the board.
5. The result is printed as an 8x8 grid.

## Output 📜

The program outputs an 8x8 chessboard where:

-   `N` marks the knight's position.
-   `*` marks the squares the knight can move to.
-   `.` marks the empty squares.

## Usage 📦

1. Run the program.
2. Enter the knight's position (e.g., `e4` or `b7`).
3. The board will display the knight's possible moves.

### Example:

```bash
Input:
d5

Output:
. . . . . . . .
. . * . * . . .
. * . . . * . .
. . . N . . . .
. * . . . * . .
. . * . * . . .
. . . . . . . .
. . . . . . . .
```

## Conclusion 🚀

This program provides a simple way to visualize the knight's movements on a chessboard.
It's useful for beginners learning chess or developers interested in game simulations.
