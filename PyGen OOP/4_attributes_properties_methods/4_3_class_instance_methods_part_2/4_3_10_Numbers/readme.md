# Numbers Class Organizer

## Description 📝

The `Numbers` class represents a dynamic collection of integers that starts empty and can be extended over time.
It provides methods to add integers to the collection and retrieve lists of either all even or all odd numbers, preserving the order in which they were added.
The class requires no arguments upon instantiation.

## Purpose 🎯

This class is designed to manage and categorize a set of integers, making it useful for teaching list manipulation, filtering techniques, or as a utility in applications requiring separation of even and odd numbers.

## How It Works 🔍

-   **Initialization**: The `__init__` method creates an empty list `numbers` to store the integers.
-   **add_number() Method**: Appends a given integer to the `numbers` list.
-   **get_even() Method**: Uses a list comprehension to return all even numbers (divisible by 2) from the list in their original order.
-   **get_odd() Method**: Uses a list comprehension to return all odd numbers (not divisible by 2) from the list in their original order.

## Output 📜

Example usage:

```python
nums = Numbers()
nums.add_number(1)
nums.add_number(2)
nums.add_number(3)
nums.add_number(4)
print(nums.get_even())  # Output: [2, 4]
print(nums.get_odd())   # Output: [1, 3]
```

## Usage 📦

1. Save the class in a Python file, e.g., `numbers.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from numbers import Numbers
my_nums = Numbers()
my_nums.add_number(5)
my_nums.add_number(6)
my_nums.add_number(7)
my_nums.add_number(8)
print(f"Even numbers: {my_nums.get_even()}")  # Output: Even numbers: [6, 8]
print(f"Odd numbers: {my_nums.get_odd()}")    # Output: Odd numbers: [5, 7]
```

## Conclusion 🚀

The `Numbers` class offers a simple and effective way to collect integers and separate them into even and odd categories while maintaining their insertion order.
Its straightforward design makes it a great tool for basic data organization, and it can be extended with features like number removal or statistical analysis for more advanced use cases.
