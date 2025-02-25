# Handling Division by Zero in Remainder Calculation 📝

## Description 📝

The function calculates the remainder when `36` is divided by each number in the `numbers` list, except for `0`, which is ignored to prevent division errors.

## Purpose 🎯

To safely compute remainders while handling `ZeroDivisionError`.

## How It Works 🔍

1. Iterates through the `numbers` list.
2. Tries to compute `36 % number`.
3. If `number == 0`, a `ZeroDivisionError` occurs and is caught, skipping that value.
4. Stores valid remainders in a new list and returns it.

## Output 📜

**Example Input:**

```python
numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
```

**Example Output:**

```python
[0, 0, 4, 0, 0, 0, 12, 36, 0, 13]
```

## Usage 📦

1. Call `calculate_remainders(numbers)` with a list of integers.
2. The function returns a list of remainders while avoiding division errors.

## Conclusion 🚀

The function now safely computes remainders while ignoring `0`, ensuring error-free execution.
