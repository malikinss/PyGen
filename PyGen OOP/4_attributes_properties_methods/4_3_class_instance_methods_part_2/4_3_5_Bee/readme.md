# Bee Movement Simulator

## Description 📝

The `Bee` class simulates a bee moving in a 2D coordinate plane.
It tracks the bee's position using x and y coordinates and provides methods to move the bee in four directions: up, down, left, and right.
The class accepts optional initial coordinates during instantiation, defaulting to (0, 0) if none are provided.

## Purpose 🎯

This class is designed to model basic movement in a coordinate system, making it ideal for teaching object-oriented programming, simulating simple navigation, or serving as a foundation for games or spatial tracking applications.

## How It Works 🔍

-   **Initialization**: The `__init__` method takes optional `x` and `y` parameters to set the bee's starting position, defaulting to (0, 0).
-   **Movement Methods**: Four methods (`move_up()`, `move_down()`, `move_right()`, `move_left()`) adjust the bee's coordinates by an integer `n`:
    -   `move_up()` increases `y`
    -   `move_down()` decreases `y`
    -   `move_right()` increases `x`
    -   `move_left()` decreases `x`

## Output 📜

Example usage:

```python
bee = Bee(1, 2)
print(f"Position: ({bee.x}, {bee.y})")  # Output: Position: (1, 2)
bee.move_up(3)
bee.move_right(2)
print(f"Position: ({bee.x}, {bee.y})")  # Output: Position: (3, 5)
bee.move_down(1)
bee.move_left(4)
print(f"Position: ({bee.x}, {bee.y})")  # Output: Position: (-1, 4)
```

## Usage 📦

1. Save the class in a Python file, e.g., `bee.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from bee import Bee
my_bee = Bee()
my_bee.move_right(5)
my_bee.move_up(2)
print(f"Bee position: ({my_bee.x}, {my_bee.y})")  # Output: Bee position: (5, 2)
```

## Conclusion 🚀

The `Bee` class provides a simple yet effective way to simulate movement in a 2D plane.
Its intuitive methods make it easy to track and adjust the bee's position, offering a versatile tool that can be extended with features like boundary checking, distance tracking, or additional movement patterns for more complex simulations.
