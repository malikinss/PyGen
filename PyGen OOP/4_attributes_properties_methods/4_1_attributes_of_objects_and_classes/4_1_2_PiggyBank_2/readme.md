# PiggyBank Class Implementation 🏦

## Description 📝

The `PiggyBank` class is a simple, empty class that represents a savings container.
Instances of this class can have attributes dynamically added to them.

## Purpose 🎯

This example demonstrates how to:

-   Create an empty class.
-   Instantiate multiple objects from the class.
-   Assign attributes dynamically to individual instances.

## How It Works 🔍

1. **Class Definition**:

    - The `PiggyBank` class is created with the `pass` statement, meaning it has no predefined attributes or methods.

2. **Instance Creation**:

    - Two instances, `money_box1` and `money_box2`, are created from the `PiggyBank` class.

3. **Adding Attributes**:
    - `money_box1` gets an attribute `coins` set to `10`.
    - `money_box2` gets:
        - `coins` set to `15`
        - `color` set to `'pink'`

## Output 📜

There is no direct output, but the attributes can be accessed as follows:

```python
print(money_box1.coins)  # Output: 10
print(money_box2.coins)  # Output: 15
print(money_box2.color)  # Output: pink
```

## Usage 📦

1. Define the `PiggyBank` class.
2. Create instances of the class.
3. Assign attributes dynamically.

## Conclusion 🚀

This implementation showcases how Python allows dynamic attribute assignment to instances.
While this is useful for quick prototyping, a more structured approach would involve defining an `__init__` method in the class.
