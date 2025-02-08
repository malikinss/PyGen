# Product of Odd Numbers in a List 🎯

## Description 📝

The `product_of_odds()` function calculates the product of all odd numbers in a given list of integers. This solution is implemented in a functional programming style using the built-in `filter()` and `reduce()` functions.

## Purpose 🎯

This function filters out all the even numbers from the list and multiplies all the remaining odd numbers together. If there are no odd numbers, the result will be 1 (default value for the product).

## How It Works 🔍

1. **`filter()`**: The function filters the list, keeping only the odd numbers.
2. **`reduce()`**: The `reduce()` function then multiplies the filtered odd numbers together. The initial value for the multiplication is `1`, which is the identity for multiplication.

## Example Output:

```python
>>> product_of_odds([1, 2, 3, 4, 5])
15  # (1 * 3 * 5)

>>> product_of_odds([2, 4, 6])
1  # No odd numbers, returns 1
```

## Usage 📦

1. The `product_of_odds()` function takes a list of integers as input.
2. It first filters out even numbers using `filter()`.
3. Then it multiplies the remaining odd numbers using `reduce()`.
4. The function returns the product of all odd numbers or 1 if no odd numbers exist.

## Conclusion 🚀

This version of `product_of_odds()` is implemented in a functional style, utilizing `filter()` to select the odd numbers and `reduce()` to calculate their product. It's concise and leverages Python's powerful functional programming tools.
