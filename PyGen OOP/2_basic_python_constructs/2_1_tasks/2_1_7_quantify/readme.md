# Quantify Function 🧮

## Description 📝

The `quantify()` function counts how many elements in an iterable satisfy a specified condition defined by a predicate function.
If no predicate function is provided, it defaults to using the `bool()` function to count truthy values.

## Purpose 🎯

This function allows you to count how many elements of an iterable meet a given condition.
It's useful when you need to filter elements based on a condition and want to know how many pass the test.

## How It Works 🔍

1. The function takes an iterable (e.g., a list, range, etc.) and a predicate function as arguments.
2. If the predicate function is provided, it is applied to each element of the iterable to determine if the element satisfies the condition.
3. If the predicate is `None`, the function will count the truthy values in the iterable, similar to how `bool()` works.
4. The function returns the number of elements that meet the condition specified by the predicate.

## Output 📜

The program outputs the number of elements in the iterable for which the predicate function returns `True`.

## Usage 📦

1. Provide an iterable (like a list or range) and an optional predicate function.
2. The function will return the count of elements that satisfy the condition defined by the predicate.

### Example:

```python
numbers = list(range(1, 11))
predicate = lambda x: x > 1
print(quantify(numbers, predicate))  # Output: 9
```

## Conclusion 🚀

The `quantify()` function is a flexible way to count elements in an iterable that meet a specified condition, and it can easily default to counting truthy values when no predicate is provided.
