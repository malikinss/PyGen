# Shopping List Program

## Description 📝

This Python program helps Timur with his shopping list by counting the number of occurrences of each item in the list, which he enters in a special format.
The items are input as lowercase, separated by commas, and the program outputs each item along with its quantity in lexicographic order.

## Purpose 🎯

The purpose of this program is to organize and count the occurrences of shopping list items that are input without specifying quantities directly.
This can be useful when a keyboard is malfunctioning, and the user is unable to type numbers.

## How It Works 🔍

1. The program takes a user input string containing items separated by commas (no spaces).
2. The input string is split into individual items.
3. The occurrences of each item are counted using Python's `Counter`.
4. The items are sorted lexicographically.
5. The program then prints each item along with its quantity in the specified format.

## Output 📜

The program outputs each item followed by its quantity in the following format:

```
<item>: <quantity>
```

### Example:

Input:

```
apple,banana,apple,orange,banana,apple
```

Output:

```
apple: 3
banana: 2
orange: 1
```

## Usage 📦

1. Copy the code into a Python file.
2. Run the program.
3. Enter the shopping list items, separated by commas (no spaces).

### Example:

```python
# Input:
apple,banana,apple,orange,banana,apple

# Output:
apple: 3
banana: 2
orange: 1
```

## Conclusion 🚀

The shopping list program efficiently counts the occurrences of items and displays them in an organized manner.
It is particularly helpful for users who are unable to type numbers directly due to a malfunctioning keyboard.
