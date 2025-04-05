# HourClock Class Time Keeper

## Description 📝

The `HourClock` class models a simplified clock with only an hour hand, accepting an initial hour value between 1 and 12.
It uses a read-write property `hours` to access and update the time, enforcing validation to ensure the value remains an integer within the valid range.

## Purpose 🎯

This class is designed for basic time tracking scenarios, educational demonstrations of properties in Python, or as a component in systems requiring a simple hour-based clock.

## How It Works 🔍

-   **Initialization**: The `__init__` method validates and sets the initial `_hours` value.
-   **\_validate_hours() Method**: Ensures the provided value is an integer in [1; 12], raising a `ValueError` if not.
-   **get_hours() Method**: Returns the current `_hours`.
-   **set_hours() Method**: Updates `_hours` after validation.
-   **Property**: `hours` is defined as a read-write property using `property()`, linking to the getter and setter.

## Usage 📦

1. Save the class in a Python file, e.g., `hour_clock.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from hour_clock import HourClock
clock = HourClock(6)
print(f"Current time: {clock.hours}")
clock.hours = 9
print(f"Updated time: {clock.hours}")
```

## Conclusion 🚀

The `HourClock` class provides a concise and validated way to manage an hour-only clock in Python.
Its property-based design ensures controlled access and updates, making it a reliable tool that can be extended with features like hour incrementing or formatting for broader timekeeping applications.
