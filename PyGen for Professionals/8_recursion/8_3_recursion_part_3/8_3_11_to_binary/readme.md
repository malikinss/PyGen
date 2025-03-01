# Binary Representation Function 🔢

## Description 📝

The `to_binary()` function converts a non-negative integer to its binary representation using recursion.
The function works by repeatedly dividing the number by 2 and appending the remainder (either 0 or 1) to form the binary string.

## Purpose 🎯

The purpose of this function is:

-   To convert a given non-negative integer into its binary string representation.
-   To demonstrate how recursion can be applied to number representation problems.

## How It Works 🔍

1. The function takes one argument:
    - `number`: A non-negative integer to convert to binary.
2. Base case:
    - If the number is 0 or 1, the function returns the number as a string ('0' or '1').
3. The function recursively divides the number by 2 and appends the remainder to form the binary representation.

For example, to convert 5 to binary:

-   `5 // 2 = 2`, remainder `5 % 2 = 1`
-   `2 // 2 = 1`, remainder `2 % 2 = 0`
-   `1 // 2 = 0`, remainder `1 % 2 = 1`

The binary representation of 5 is `'101'`.

## Output 📜

For example:

```python
print(to_binary(5))
```

The function computes:

```
5 in binary is '101'.
```

**Output:**

```
'101'
```

## Usage 📦

1. Call the function `to_binary()` with:
    - A non-negative integer.
2. Example:
    ```python
    result = to_binary(10)  # Output: '1010'
    print(result)
    ```
3. The function returns:
    - A string representing the binary notation of the input number.

## Conclusion 🚀

The `to_binary()` function effectively demonstrates how recursion can be used to convert an integer into its binary representation.
This solution is an elegant way to handle number conversion problems in a recursive manner.
