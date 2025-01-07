# Same Digit Set Checker Program 🔢

## Description 📝

This program takes two strings consisting of numbers as input and determines if both strings consist of the same set of digits, regardless of order or frequency of occurrence.

## Purpose 🎯

-   To check if two strings of numbers contain the exact same unique digits.
-   To demonstrate how to compare sets of digits using Python's `set` data structure.

## How It Works 🔍

1. **Function `have_same_digit_set`**:

    - Accepts two strings `first` and `second`, each consisting of digits.
    - Converts both strings into sets, which automatically removes duplicates and preserves only unique digits.
    - Compares the two sets:
        - If both sets are equal, the function returns `"YES"`.
        - If the sets are not equal, the function returns `"NO"`.

2. **Input**:

    - Two strings of digits are taken as input from the user.

3. **Output**:
    - The program outputs `"YES"` if both strings contain the same set of digits, otherwise it outputs `"NO"`.

### Example:

```python
first_input = "12345"
second_input = "54321"
print(have_same_digit_set(first_input, second_input))
```

**Output**:

```
YES
```

```python
first_input = "1234"
second_input = "5678"
print(have_same_digit_set(first_input, second_input))
```

**Output**:

```
NO
```

## Output 📜

-   If the input strings are `"12345"` and `"54321"`, the output will be `"YES"` because both strings contain the same digits, even though the order is different.
-   If the input strings are `"1234"` and `"5678"`, the output will be `"NO"` because the sets of digits are different.

## Conclusion 🚀

This program efficiently compares the sets of digits from two strings by utilizing Python's `set` data structure.
It simplifies the task of determining whether both strings consist of the same set of digits without considering their order or frequency.
