# Gun Class with Alternating Sounds

## Description 📝

The `Gun` class simulates a firearm that alternates between two distinct shooting sounds: "pif" and "paf".
It requires no arguments upon instantiation and uses an internal counter to track the number of shots fired, producing "pif" on odd-numbered shots and "paf" on even-numbered shots.

## Purpose 🎯

This class is intended to demonstrate basic state management in object-oriented programming by maintaining an internal counter to alternate outputs.
It can be used for educational purposes or as a playful component in simple simulations or games.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets an internal `counter` attribute to 1, preparing the gun for its first shot.
-   **shoot() Method**: Checks if the `counter` is odd or even using the modulo operator (`%`), prints "pif" for odd counts and "paf" for even counts, then increments the `counter`.

## Output 📜

Example usage:

```python
gun = Gun()
gun.shoot()  # Output: pif
gun.shoot()  # Output: paf
gun.shoot()  # Output: pif
gun.shoot()  # Output: paf
```

## Usage 📦

1. Save the class in a Python file, e.g., `gun.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from gun import Gun
my_gun = Gun()
for _ in range(4):
    my_gun.shoot()  # Outputs: pif, paf, pif, paf
```

## Conclusion 🚀

The `Gun` class offers a straightforward yet engaging way to simulate a firearm with alternating shot sounds.
Its use of an internal counter to toggle between "pif" and "paf" makes it a great example of state tracking in Python, and it can be enhanced with features like ammo limits or different sound patterns for more advanced applications.
