# Finding the Largest Numeric Value in a Mixed List

## Description

This program extracts the **largest numeric value** from a **mixed list** containing both **numbers and strings**.

## Purpose

The goal is to practice:

1. **Filtering numeric values** from a heterogeneous list.
2. **Using `max()` with a lambda function** to ignore non-numeric values.

## How It Works

1. **Helper Function `is_num()`**:

    - Checks if an element is an **integer** or **float**.

2. **Finding Maximum Numeric Value**:
    - Uses `max()` with `key=lambda x: x if is_num(x) else float('-inf')`.
    - Assigns `float('-inf')` to **ignore strings** during comparison.

## Output Example

```
2950603
```

## Usage

1. **Provide a list (`mixed_list`)** containing numbers and strings.
2. **Call `max_numeric_value(mixed_list)`**.
3. **Print the result**, which is the highest number in the list.

## Conclusion

This approach efficiently finds the largest number **without errors** when encountering **string values**.
