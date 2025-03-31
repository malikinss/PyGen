# Gun Class with Shot Tracking

## Description 📝

The `Gun` class simulates a firearm that alternates between "pif" and "paf" sounds with each shot.
It requires no arguments upon instantiation and includes methods to shoot, track the number of shots fired, and reset the shot count.
The class uses an internal counter to manage the alternating sound pattern and shot statistics.

## Purpose 🎯

This class is designed to demonstrate state management and method interaction in Python.
It can be used for educational purposes, simple simulations, or as a building block for more complex systems requiring action tracking and reset functionality.

## How It Works 🔍

-   **Initialization**: The `__init__` method initializes the `counter` attribute to 0.
-   **shoot() Method**: Increments the `counter`, then prints "pif" for odd counts and "paf" for even counts using modulo (`%`) logic.
-   **shots_count() Method**: Returns the current value of the `counter`.
-   **shots_reset() Method**: Resets the `counter` to 0, restarting the sequence.

## Output 📜

Example usage:

```python
gun = Gun()
gun.shoot()           # Output: pif
gun.shoot()           # Output: paf
print(gun.shots_count())  # Output: 2
gun.shots_reset()
print(gun.shots_count())  # Output: 0
gun.shoot()           # Output: pif
```

## Usage 📦

1. Save the class in a Python file, e.g., `gun.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from gun import Gun
my_gun = Gun()
my_gun.shoot()  # Outputs: pif
my_gun.shoot()  # Outputs: paf
print(f"Shots fired: {my_gun.shots_count()}")  # Outputs: Shots fired: 2
my_gun.shots_reset()
print(f"After reset: {my_gun.shots_count()}")  # Outputs: After reset: 0
```

## Conclusion 🚀

The `Gun` class provides a robust and interactive way to simulate a firearm with alternating sounds and shot tracking.
Its combination of sound alternation, count retrieval, and reset functionality makes it a versatile tool that can be extended with features like ammo limits or sound customization for more advanced applications.
