# PiggyBank Class Implementation 🏦

## Description 📝

The `PiggyBank` class represents a simple savings container, commonly known as a piggy bank.
This class has two predefined attributes.

## Purpose 🎯

This example demonstrates how to:

-   Define a class with class attributes.
-   Create an instance of the class.
-   Access the attributes from an instance.

## How It Works 🔍

1. **Class Definition**:

    - The `PiggyBank` class is defined with two class attributes:
        - `content`: Represents what the piggy bank holds, set to `"coins"`.
        - `alternate_name`: Another name for the piggy bank, set to `"penny bank"`.

2. **Instance Creation**:

    - The variable `money_box` is assigned an instance of the `PiggyBank` class.

3. **Accessing Attributes**:
    - The attributes can be accessed using `money_box.content` and `money_box.alternate_name`.

## Output 📜

Although this code does not print anything by default, the attributes can be accessed like this:

```python
print(money_box.content)  # Output: coins
print(money_box.alternate_name)  # Output: penny bank
```

## Usage 📦

1. Define the `PiggyBank` class with predefined attributes.
2. Create an instance of the class.
3. Access the attributes.

## Conclusion 🚀

This implementation shows how to use class attributes to store shared values across all instances of a class.
If each instance needed unique values, instance attributes should be defined in an `__init__` method.
