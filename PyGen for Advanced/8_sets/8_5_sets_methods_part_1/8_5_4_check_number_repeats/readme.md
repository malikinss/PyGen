# Number Repeat Checker Program 📝

## Description 📝

This program processes a sequence of numbers given as input and checks whether each number has appeared before in the sequence.
It prints "YES" if the number has appeared earlier, and "NO" if it has not.
Leading zeros in the numbers are ignored.

## Purpose 🎯

-   Detect repeated numbers in a sequence while disregarding leading zeros.
-   Provide quick feedback on whether a number is a repeat of a previously seen number.

## How It Works 🔍

1. **Function `check_number_repeats`**:
    - Takes a list of numbers in string format as input.
    - For each number in the sequence:
        - Converts the number string to an integer to ignore leading zeros.
        - Checks if the number has been encountered before using a set (`seen_numbers`).
        - Prints "YES" if the number has appeared before, otherwise prints "NO".
    - The set stores numbers as integers, ensuring that leading zeros are ignored.

### Example:

**Input**:

```
0012 34 56 0012 34 789
```

**Output**:

```
NO
NO
NO
YES
YES
NO
```

-   After parsing and ignoring leading zeros, the sequence is: `12, 34, 56, 12, 34, 789`.
-   "12" appears twice, "34" appears twice, and the others appear only once.

## Output 📜

-   For each number, print "YES" if it has appeared before or "NO" if it is the first appearance.

## Usage 📦

1. Run the program.
2. Enter a sequence of numbers.
3. The program will print "YES" or "NO" based on whether each number has appeared before.

## Conclusion 🚀

This program helps efficiently check if any numbers in a sequence are repeated, ignoring leading zeros, and provides immediate feedback in a user-friendly format.
