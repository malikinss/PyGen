# Dice Class Random Roller

## Description 📝

The `Dice` class models a die with a specified number of sides, set during instantiation.
It’s a callable object that, when invoked with no arguments, returns a random integer from 1 to the number of sides, simulating a dice roll using `random.randint`.

## Purpose 🎯

This class is designed for random number generation within a range, ideal for games, simulations, educational examples of callable objects, or applications needing dice-like randomness.

## How It Works 🔍

-   **Initialization**: Stores the number of `sides` as an instance attribute.
-   ****call**()**: Makes instances callable, returning a random value from 1 to `sides` using `random.randint`.

## Usage 📦

1. Save the class in a Python file, e.g., `dice.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from dice import Dice
d6 = Dice(6)
print(d6())  # Random number between 1 and 6
print(d6())  # Another random roll
d20 = Dice(20)
print(d20()) # Random number between 1 and 20
```

## Conclusion 🚀

The `Dice` class provides a straightforward and fun way to simulate dice rolls in Python, leveraging the callable pattern for simplicity.
Its design is lightweight and can be extended with features like roll history or multiple dice for more complex gaming scenarios.
