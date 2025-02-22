# Named Tuple: Fruit 📝

## Description 📝

This program defines a named tuple `Fruit` with three fields: `name`, `color`, and `vitamins`.
Named tuples provide a simple way to create immutable objects with named fields, making the code more readable and self-documenting.

## Purpose 🎯

The purpose of this program is to demonstrate how to create a named tuple using the `namedtuple` function from Python's `collections` module.
Named tuples can be used to represent simple data structures with named fields.

## How It Works 🔍

1. The `namedtuple` function is used to create a new class called `Fruit`, with three fields: `name`, `color`, and `vitamins`.
2. The program does not output anything by design; it simply defines the named tuple.

## Output 📜

There is no output from this program as it only defines the named tuple class.

## Usage 📦

To use the `Fruit` named tuple, you can create instances of it by providing values for `name`, `color`, and `vitamins`:

### Example:

```python
apple = Fruit(name="Apple", color="Red", vitamins="A, C")
print(apple.name)  # Output: Apple
print(apple.color)  # Output: Red
print(apple.vitamins)  # Output: A, C
```

## Conclusion 🚀

This program shows how to create a simple named tuple with Python, which can be used to represent data in a clean and efficient way, making it easier to work with structured data.
