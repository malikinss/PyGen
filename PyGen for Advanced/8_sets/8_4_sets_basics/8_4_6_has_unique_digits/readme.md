# Unique Digits Checker Program 🔢

## Description 📝

This program takes a string consisting of numbers as input and checks if all digits in the string are unique.
It utilizes Python's `set` to remove duplicate digits and compares the size of the set with the length of the original string to determine uniqueness.

## Purpose 🎯

-   To determine whether a string of digits contains all unique digits.
-   To showcase the use of Python's `set` data structure to check for uniqueness.

## How It Works 🔍

1. **Function `has_unique_digits`**:

    - Accepts a string `number_string` representing a number.
    - Converts the string into a set, which automatically removes any duplicate digits.
    - Compares the length of the set with the original string's length:
        - If the lengths match, all digits are unique, and the function returns `"YES"`.
        - If the lengths do not match, there are repeated digits, and the function returns `"NO"`.

2. **Input**:

    - A string of digits is taken as input from the user.

3. **Output**:
    - The program outputs `"YES"` if all digits are unique, otherwise it outputs `"NO"`.

### Example:

```python
number_string = "123456"
print(has_unique_digits(number_string))
```

**Output**:

```
YES
```

```python
number_string = "112233"
print(has_unique_digits(number_string))
```

**Output**:

```
NO
```

## Output 📜

-   If the input string is `"123456"`, the output will be `"YES"` because all digits are unique.
-   If the input string is `"112233"`, the output will be `"NO"` because the digits are repeated.

## Conclusion 🚀

This program demonstrates how to easily check for uniqueness of characters in a string using Python's `set`.
It is efficient and handles strings of digits quickly, providing a straightforward solution to the problem.
