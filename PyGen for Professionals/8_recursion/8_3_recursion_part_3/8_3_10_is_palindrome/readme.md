# Palindrome Checker Function 🔍

## Description 📝

The `is_palindrome()` function checks if a given string is a palindrome using recursion.
A palindrome is a string that reads the same forwards and backwards.
The function works by comparing the first and last characters of the string and recursively checking the remaining characters.

## Purpose 🎯

The purpose of this function is:

-   To determine whether a given string is a palindrome.
-   To demonstrate the use of recursion to solve string manipulation problems.

## How It Works 🔍

1. The function takes one argument:
    - `string`: The string to be checked for being a palindrome.
2. Base case:
    - If the string is empty or consists of only one character, it is considered a palindrome.
3. The first and last characters of the string are compared:
    - If they are not equal, the string is not a palindrome.
4. The function then recursively checks the substring excluding the first and last characters until the base case is reached.

## Output 📜

For example:

```python
print(is_palindrome('level'))
```

The function computes:

```
'level' is a palindrome.
```

**Output:**

```
True
```

## Usage 📦

1. Call the function `is_palindrome()` with:
    - A string to check for palindrome properties.
2. Example:
    ```python
    result = is_palindrome("madam")  # Output: True
    print(result)
    ```
3. The function returns:
    - `True` if the string is a palindrome.
    - `False` otherwise.

## Conclusion 🚀

The `is_palindrome()` function demonstrates how recursion can be applied to string problems to efficiently check for palindromes, highlighting a straightforward and elegant solution for string manipulation challenges.
