# Postman Class Delivery Manager

## Description 📝

The `Postman` class simulates a postman's delivery schedule by maintaining a list of addresses, each represented as a tuple of street, house number, and apartment number.
It starts empty and provides methods to add delivery addresses and retrieve unique houses for a street or unique apartments for a specific house, preserving the order of first appearance.

## Purpose 🎯

This class is designed to organize and query delivery data, making it suitable for logistical simulations, educational examples of list processing, or as a component in a mail delivery system prototype.

## How It Works 🔍

-   **Initialization**: The `__init__` method creates an empty list `delivery_data` for storing address tuples.
-   **add_delivery() Method**: Adds a `(street, house, apartment)` tuple to the `delivery_data` list.
-   **get_houses_for_street() Method**: Filters addresses by street and returns a list of unique house numbers in their order of first addition, using a set to track seen houses.
-   **get_flats_for_house() Method**: Filters addresses by street and house, returning a list of unique apartment numbers in their order of first addition, using a set to track seen apartments.

## Output 📜

Example usage:

```python
postman = Postman()
postman.add_delivery("Main St", 1, 101)
postman.add_delivery("Main St", 2, 201)
postman.add_delivery("Main St", 1, 102)
print(postman.get_houses_for_street("Main St"))  # Output: [1, 2]
print(postman.get_flats_for_house("Main St", 1))  # Output: [101, 102]
```

## Usage 📦

1. Save the class in a Python file, e.g., `postman.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from postman import Postman
my_postman = Postman()
my_postman.add_delivery("Elm St", 10, 1)
my_postman.add_delivery("Elm St", 10, 2)
my_postman.add_delivery("Elm St", 11, 1)
print(f"Houses on Elm St: {my_postman.get_houses_for_street('Elm St')}")  # Output: Houses on Elm St: [10, 11]
print(f"Flats in house 10: {my_postman.get_flats_for_house('Elm St', 10)}")  # Output: Flats in house 10: [1, 2]
```

## Conclusion 🚀

The `Postman` class provides an efficient and organized way to manage delivery addresses in Python, ensuring unique house and apartment listings while preserving order.
Its design is practical for basic delivery tracking and can be extended with features like address removal or sorting for more sophisticated logistics applications.
