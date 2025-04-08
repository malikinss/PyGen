# FoodInfo Class Nutrition Calculator

## Description 📝

The `FoodInfo` class represents the nutritional value of food with `proteins`, `fats`, and `carbohydrates` in grams, set during instantiation.
It provides a formal string representation via `__repr__` and supports addition (`+`) between `FoodInfo` instances, as well as multiplication (`*`), division (`/`), and integer division (`//`) by scalars, returning new instances with adjusted values or `NotImplemented` for invalid operands.

## Purpose 🎯

This class is designed for nutritional data management, suitable for diet tracking, educational examples of operator overloading, or applications needing food composition calculations.

## How It Works 🔍

-   **Initialization**: Sets `proteins`, `fats`, and `carbohydrates` attributes.
-   **`__repr__()`**: Returns `FoodInfo(<proteins>, <fats>, <carbohydrates>)`.
-   **`__add__()`**: Adds two `FoodInfo` instances, summing their nutritional values.
-   **`__mul__()`**: Multiplies nutritional values by a scalar (int or float).
-   **`__rmul__()`**: Handles right multiplication (e.g., `2 * food`) by reusing `__mul__`.
-   **`__truediv__()`**: Divides nutritional values by a scalar.
-   **`__floordiv__()`**: Integer divides nutritional values by a scalar.
-   **Error Handling**: Returns `NotImplemented` for unsupported operand types.

## Usage 📦

1. Save the class in a Python file, e.g., `food_info.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from food_info import FoodInfo
f1 = FoodInfo(10, 20, 30)
f2 = FoodInfo(5, 10, 15)
print(f1 + f2)
print(f1 * 2)
print(2 * f1)
print(f1 / 2)
print(f1 // 2)
```

## Conclusion 🚀

The `FoodInfo` class provides a robust way to handle nutritional data in Python, with intuitive arithmetic operations for combining and scaling values.
Its design is flexible, making it a strong base for adding features like calorie calculation or nutritional validation for more advanced dietary applications.
