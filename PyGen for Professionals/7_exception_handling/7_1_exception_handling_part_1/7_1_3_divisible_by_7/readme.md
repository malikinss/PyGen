# Divisible by 7 Finder 📝

## Description 📝

This program takes two integers as input and returns a list of all integers between them (inclusive) that are divisible by 7.

## Purpose 🎯

The goal is to fix a previously incorrect implementation and provide a correct version that efficiently finds numbers divisible by 7.

## How It Works 🔍

1. The function `divisible_by_seven(a, b)`:
    - Takes two integer inputs: `a` (start) and `b` (end).
    - Uses list comprehension to iterate over the range `[a, b]`.
    - Filters numbers that are divisible by 7 (`i % 7 == 0`).
    - Returns the list of valid numbers.
2. The user inputs two integers.
3. The function is called with the provided inputs.
4. The resulting list is printed.

## Output 📜

**Example Input:**

```
Enter first number: 10
Enter second number: 30
```

**Example Output:**

```python
[14, 21, 28]
```

## Usage 📦

1. Run the script.
2. Enter two integers.
3. The script will print all numbers between them that are divisible by 7.

## Conclusion 🚀

The fixed implementation correctly handles input parsing, list creation, and filtering.
It ensures proper type conversion, uses modulo for divisibility, and efficiently constructs the output list.
