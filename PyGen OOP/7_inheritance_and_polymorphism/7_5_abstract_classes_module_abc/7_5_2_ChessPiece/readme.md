# ChessPiece, King, and Knight Class Implementation

## Description 📝

The provided code implements the `ChessPiece` abstract base class and its subclasses `King` and `Knight`.
The `ChessPiece` class defines a chess piece with horizontal (`a` to `h`) and vertical (1 to 8) coordinates and an abstract `can_move` method.
The `King` and `Knight` classes inherit from `ChessPiece`, implementing `can_move` to check valid moves for each piece type while maintaining the same initialization and coordinate attributes.

## Purpose 🎯

Intended for chess-related applications, such as game logic, move validation, or chess engines, where pieces need to track positions and verify legal moves.
It’s also suitable for educational examples of abstract base classes, inheritance, and chess move mechanics in Python.

## How It Works 🔍

-   **Abstract Base Class (`ChessPiece`)**:
    -   Inherits from `ABC` to enforce abstraction.
    -   **Initialization (`__init__`)**:
        -   Accepts `horizontal` (str, `a` to `h`) and `vertical` (int, 1 to 8).
        -   Stores them as instance attributes (`self.horizontal`, `self.vertical`).
    -   **Helper Method**:
        -   `_get_steps(to_hor, to_ver)`: Calculates absolute horizontal and vertical steps to target coordinates using `ord` for horizontal letter differences.
    -   **Abstract Method**:
        -   `can_move(to_hor, to_ver)`: Must be implemented by subclasses to validate moves.
-   **King Class**:
    -   Inherits from `ChessPiece`.
    -   **Initialization**: Matches `ChessPiece`, storing `horizontal` and `vertical`.
    -   **Method**:
        -   `can_move(to_hor, to_ver)`: Returns `True` if the king can move one square in any direction (horizontal or vertical steps ≤ 1, not same position).
    -   **Attributes**: `horizontal`, `vertical`.
-   **Knight Class**:
    -   Inherits from `ChessPiece`.
    -   **Initialization**: Matches `ChessPiece`, storing `horizontal` and `vertical`.
    -   **Method**:
        -   `can_move(to_hor, to_ver)`: Returns `True` if the knight can move in an L-shape (steps are (1, 2) or (2, 1)).
    -   **Attributes**: `horizontal`, `vertical`.
-   **Behavior**:
    -   All classes store coordinates as attributes.
    -   `can_move` checks move validity based on piece-specific rules.
    -   `_get_steps` simplifies move calculations by converting coordinates to step counts.

## Verification ✅

Implementation satisfies requirements:

-   **ChessPiece**:
    -   Abstract with `horizontal` (str, `a` to `h`) and `vertical` (int, 1 to 8).
    -   Abstract `can_move` method.
    -   E.g., cannot instantiate directly due to `ABC`.
-   **King**:
    -   Initialization: `King("e", 1)` sets `horizontal="e"`, `vertical=1`.
    -   `can_move`:
        -   Valid: `King("e", 4).can_move("e", 5)` → `True` (one square up).
        -   Valid: `King("e", 4).can_move("f", 5)` → `True` (diagonal one square).
        -   Invalid: `King("e", 4).can_move("e", 6)` → `False` (two squares).
        -   Invalid: `King("e", 4).can_move("e", 4)` → `False` (same position).
    -   Attributes: `k = King("a", 8); k.horizontal` → `"a"`, `k.vertical` → `8`.
-   **Knight**:
    -   Initialization: `Knight("g", 1)` sets `horizontal="g"`, `vertical=1`.
    -   `can_move`:
        -   Valid: `Knight("g", 1).can_move("f", 3)` → `True` (L-shape, 1 hor, 2 ver).
        -   Valid: `Knight("g", 1).can_move("h", 3)` → `True` (L-shape, 2 hor, 1 ver).
        -   Invalid: `Knight("g", 1).can_move("g", 2)` → `False` (not L-shape).
    -   Attributes: `n = Knight("b", 1); n.horizontal` → `"b"`, `n.vertical` → `1`.
-   **Inheritance**:
    -   `issubclass(King, ChessPiece)`, `issubclass(Knight, ChessPiece)` → `True`.
-   **No Validation**:
    -   Assumes correct input (e.g., `horizontal` in `a-h`, `vertical` in 1-8) per requirements.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: `ChessPiece` provides a unified interface and helper method. `King` and `Knight` implement `can_move` according to chess rules. No validation needed per requirements.
-   **Performance**:
    -   `_get_steps`: O(1) for simple arithmetic.
    -   `can_move`: O(1) for both `King` (comparison) and `Knight` (tuple check).
    -   Highly efficient for chess move validation.
-   **Design**:
    -   `_get_steps` in `ChessPiece` reduces code duplication for coordinate calculations.
    -   Abstract `can_move` ensures subclasses define move logic.
    -   Minimal implementation avoids unnecessary complexity.
    -   Type hints and docstrings enhance clarity.
-   **Extensibility**: Structure supports adding other pieces (e.g., `Queen`, `Rook`) by inheriting from `ChessPiece` and implementing `can_move`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
king = King("e", 4)
knight = Knight("g", 1)

# Test King moves
print(king.can_move("e", 5))  # True (one square up)
print(king.can_move("f", 5))  # True (diagonal)
print(king.can_move("g", 6))  # False (two squares)
print(king.can_move("e", 4))  # False (same position)

# Test Knight moves
print(knight.can_move("f", 3))  # True (L-shape: 1 hor, 2 ver)
print(knight.can_move("h", 3))  # True (L-shape: 2 hor, 1 ver)
print(knight.can_move("g", 2))  # False (not L-shape)

# Test attributes
print(king.horizontal, king.vertical)  # e 4
print(knight.horizontal, knight.vertical)  # g 1

# Test inheritance
print(isinstance(king, ChessPiece))  # True
print(isinstance(knight, ChessPiece))  # True
```

## Conclusion 🚀

The `ChessPiece`, `King`, and `Knight` implementation is precise, providing an abstract base class with a clear inheritance scheme and correct move validation for each piece.
It’s ideal for chess applications or inheritance education, fully compliant with the task’s requirements.
