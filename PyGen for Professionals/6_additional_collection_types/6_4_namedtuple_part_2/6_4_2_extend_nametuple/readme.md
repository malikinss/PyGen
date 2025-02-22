# Named Tuple: ExtendedGame 📝

## Description 📝

This program extends an existing named tuple `Game` by creating a new named tuple `ExtendedGame`.
The `ExtendedGame` tuple retains all the fields of `Game`, and adds two new fields: `release_date` and `price`.

## Purpose 🎯

The purpose of this program is to demonstrate how to extend a named tuple by adding new fields to it, while still preserving the fields of the original named tuple.

## How It Works 🔍

1. The original `Game` named tuple is defined with three fields: `name`, `developer`, and `publisher`.
2. The `ExtendedGame` named tuple is then defined by using the `Game._fields` attribute to get the fields of the `Game` tuple and adding two additional fields: `release_date` and `price`.

## Output 📜

There is no output from this program as it only defines the `ExtendedGame` named tuple.

## Usage 📦

To use the `ExtendedGame` named tuple, you can create instances of it by providing values for all the original fields from `Game` along with the two new fields:

### Example:

```python
# Create an instance of ExtendedGame
game = ExtendedGame(name="Super Mario", developer="Nintendo", publisher="Nintendo", release_date="2025-05-01", price=59.99)

print(game.name)  # Output: Super Mario
print(game.developer)  # Output: Nintendo
print(game.publisher)  # Output: Nintendo
print(game.release_date)  # Output: 2025-05-01
print(game.price)  # Output: 59.99
```

## Conclusion 🚀

This program shows how to extend a named tuple in Python, adding new fields while keeping the original fields intact.
It’s a great way to create more complex data structures while maintaining the clarity and immutability of named tuples.
