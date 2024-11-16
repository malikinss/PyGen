# Code review task 4 🪲

## Description 📝

This program takes a sequence of 4 integers as input and determines the number of odd numbers in the sequence. It also calculates the maximum odd number. If there are no odd numbers in the sequence, the program will output `"NO"`.

## Purpose 🎯

The purpose of this program is to:

1. Count how many odd numbers exist in a given sequence of 4 integers.
2. Find the maximum odd number in the sequence.
3. Handle edge cases where no odd numbers are found.

## How It Works 🔍

-   The program loops through the 4 integers, checking each one to determine if it is odd (`x % 2 != 0`).
-   If the number is odd, it updates the count and checks if the number is greater than the current maximum odd number.
-   If no odd numbers are found, the program outputs `"NO"`.
-   Otherwise, it prints the count of odd numbers and the maximum odd number.

## Output 📜

-   If there are odd numbers, it prints:
    -   The count of odd numbers.
    -   The maximum odd number.
-   If there are no odd numbers, it prints `"NO"`.

## Usage 📦

1. Run the program.
2. Enter 4 integers one by one.
3. The program will display either the count and maximum odd number, or `"NO"` if there are no odd numbers.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect initialization of `maximum`:

-   Original: `maximum = 999`
-   The program needs to find the maximum odd number. Starting with `999` could cause issues if all numbers are smaller or if no odd numbers are present.
-   Fix: `maximum = -1` (or another value that won't conflict with possible input values).

### 2. Incorrect handling of the maximum value update:

-   Original: `maximum = i`
-   This sets `maximum` to the loop index, not the value of `x`, which is incorrect.
-   Fix: `maximum = x` to properly update the maximum value when an odd number is found.

### 3. Unnecessary `break` after updating the maximum:

-   Original: `break`
-   The program should continue processing all numbers and not stop after finding one odd number.
-   Fix: Remove the `break` statement to ensure the loop continues until all 4 integers are processed.

## Fixed code 🛠:

```python
count = 0
maximum = -1

for i in range(4):
    x = int(input())

    if x % 2 != 0:
        count += 1

        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
```

## Explanation of Changes 🧾:

1. **Initialization of `maximum`**: Changed `maximum = 999` to `maximum = -1` to properly handle edge cases where no odd numbers are present.
2. **Updating `maximum` correctly**: Changed `maximum = i` to `maximum = x` to ensure the maximum odd number is correctly updated.
3. **Removed `break`**: The loop now continues processing all 4 numbers, ensuring the correct count and maximum are calculated.

## Conclusion 🚀

This program now correctly counts and identifies the maximum odd number in a sequence of 4 integers.
It demonstrates the use of conditional checks and simple looping to handle edge cases and process input data effectively.
