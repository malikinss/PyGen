# House Class Simulator

## Description 📝

The `House` class represents a house with customizable properties.
It tracks the house's color and number of rooms, allowing modifications through instance methods.
When instantiated, it requires a color and room count, and provides methods to repaint the house or add more rooms.

## Purpose 🎯

This class is designed to model a house in a simple and flexible way, making it suitable for learning object-oriented programming or as a component in simulations like real estate management or home renovation scenarios.

## How It Works 🔍

-   **Initialization**: The `__init__` method takes `color` and `rooms` as arguments, setting them as instance attributes.
-   **paint() Method**: Accepts a `new_color` string and updates the house's `color` attribute to reflect the new value.
-   **add_rooms() Method**: Takes an integer `n` and increases the `rooms` attribute by that amount using the `+=` operator.

## Output 📜

Example usage:

```python
house = House("blue", 3)
print(f"Color: {house.color}, Rooms: {house.rooms}")  # Output: Color: blue, Rooms: 3
house.paint("red")
house.add_rooms(2)
print(f"Color: {house.color}, Rooms: {house.rooms}")  # Output: Color: red, Rooms: 5
```

## Usage 📦

1. Save the class in a Python file, e.g., `house.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from house import House
my_house = House("green", 4)
my_house.paint("yellow")
my_house.add_rooms(1)
print(f"My house is {my_house.color} with {my_house.rooms} rooms")  # Output: My house is yellow with 5 rooms
```

## Conclusion 🚀

The `House` class offers a practical and intuitive way to simulate a house's basic properties in Python.
With its `paint()` and `add_rooms()` methods, it allows for easy modification of the house's color and size, providing a solid foundation that can be expanded with features like room types or additional attributes for more complex applications.
