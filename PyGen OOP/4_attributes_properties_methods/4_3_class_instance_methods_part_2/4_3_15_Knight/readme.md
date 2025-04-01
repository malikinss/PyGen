# Knight Class Chess Simulator

## Description 📝

The `Knight` class models a chess knight on an 8x8 chessboard, tracking its position (horizontal 'a'-'h', vertical 1-8) and color ('black' or 'white').
It provides methods to identify the knight's symbol, check valid moves, update its position, and visualize the board with the knight and its possible moves marked.

## Purpose 🎯

This class is designed to simulate a knight's behavior in chess, making it useful for chess-related programming exercises, game development, or educational tools to explore knight movement patterns.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the knight’s `horizontal`, `vertical`, and `color` attributes.
-   **get_char() Method**: Returns 'N', the knight’s standard symbol.
-   **can_move() Method**: Checks if a target cell is reachable via the knight’s L-shaped moves (±1,±2 or ±2,±1).
-   **move_to() Method**: Updates the knight’s position if the move is valid; otherwise, it remains unchanged.
-   **draw_board() Method**: Prints an 8x8 grid with '.' for empty cells, 'N' for the knight, and '\*' for valid move destinations.
-   **Helper Methods**: Convert coordinates to indices, calculate possible moves, and generate an empty board.

## Output 📜

Example usage:

```python
knight = Knight('b', 1, 'white')
print(knight.get_char())          # Output: N
print(knight.can_move('c', 3))    # Output: True
knight.draw_board()
knight.move_to('c', 3)
knight.draw_board()
```

## Usage 📦

1. Save the class in a Python file, e.g., `knight.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from knight import Knight
my_knight = Knight('d', 4, 'black')
print(f"Can move to e6? {my_knight.can_move('e', 6)}")  # Output: Can move to e6? True
my_knight.move_to('e', 6)
my_knight.draw_board()
```

## Conclusion 🚀

The `Knight` class provides a comprehensive and visual way to simulate a chess knight’s movement in Python.
Its ability to validate moves and display the board makes it a practical tool for chess simulations, easily extensible with features like move history or integration into a full chess game.
