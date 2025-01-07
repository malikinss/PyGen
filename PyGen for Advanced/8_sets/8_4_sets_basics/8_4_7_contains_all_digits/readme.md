# All Digits Checker Program 🔢

## Description 📝

This program takes two strings consisting of numbers as input and checks if all ten digits from 0 to 9 are present in the combination of both strings.
It uses the `set` data structure to determine the presence of all digits.

## Purpose 🎯

-   To determine whether the combination of two strings contains every digit from 0 to 9.
-   To demonstrate how to use sets to compare the presence of elements in a string.

## How It Works 🔍

1. **Function `contains_all_digits`**:

    - Accepts two strings `first` and `second`, which represent numbers.
    - Combines the two strings and converts the result into a set of unique digits.
    - Compares the set of digits from the combined strings with the set of all digits `0123456789`:
        - If the combined set contains all ten digits, the function returns `"YES"`.
        - Otherwise, it returns `"NO"`.

2. **Input**:

    - Two strings of digits are taken as input from the user.

3. **Output**:
    - The program outputs `"YES"` if all digits from 0 to 9 are present in the combination of the two input strings, otherwise it outputs `"NO"`.

### Example:

```python
first_input = "12345"
second_input = "67890"
print(contains_all_digits(first_input, second_input))
```

**Output**:

```
YES
```

```python
first_input = "1234"
second_input = "5678"
print(contains_all_digits(first_input, second_input))
```

**Output**:

```
NO
```

## Output 📜

-   If the input strings are `"12345"` and `"67890"`, the output will be `"YES"` because all digits from 0 to 9 are present.
-   If the input strings are `"1234"` and `"5678"`, the output will be `"NO"` because not all digits are covered.

## Conclusion 🚀

This program efficiently checks for the presence of all ten digits in two strings by using Python's `set` data structure, which simplifies the task of identifying unique digits and comparing sets.
