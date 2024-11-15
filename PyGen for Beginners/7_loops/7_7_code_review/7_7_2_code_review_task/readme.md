# Code Review: Sum and Maximum Negative Number in a Sequence 🧮

## Description 📝

This program processes a sequence of 10 integers and calculates the sum of all negative numbers and the maximum negative number in the sequence.
If no negative numbers are found, it displays "NO".

The program handles edge cases such as the absence of negative numbers and computes the correct sum and maximum negative number even if the sequence contains both positive and negative numbers.

## Purpose 🎯

The purpose of this program is to:

1. Identify and sum the negative numbers in a sequence of 10 integers.
2. Find the maximum negative number in the sequence.
3. Display the sum and maximum negative number if present, or "NO" if no negative numbers exist.

## How It Works 🔍

-   The program loops through a sequence of 10 integers.
-   If a number is negative, it is added to the sum and checked if it is the maximum negative number.
-   After processing all numbers, it prints the sum of negative numbers and the largest negative number.
    If there are no negative numbers, it prints "NO".

## Output 📜

-   If there are negative numbers, the program will print:
    -   The sum of all negative numbers.
    -   The maximum negative number in the sequence.
-   If no negative numbers are found, the program prints `"NO"`.

## Usage 📦

1. Run the program.
2. Enter 10 integers one by one.
3. The program will display either the sum and maximum negative number or `"NO"` if there are no negative numbers.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect range for the loop:

-   Original: `for i in range(11)`
-   The loop needs to process 10 integers, so the range should be from 0 to 9 (not 1 to 10).
-   Fix: `for i in range(10)`

### 2. Incorrect initialization of `s`:

-   Original: `s = x`
-   This overwrites `s` with only the last negative number encountered, instead of summing all negative numbers.
-   Fix: `s += x`

### 3. Incorrect initial value of `mx`:

-   Original: `mx = 0`
-   The program starts `mx` as 0, which may cause issues when all negative numbers are less than 0.
    The correct initial value should be smaller than any possible negative number.
-   Fix: `mx = (-10 ** 6) - 1`

### 4. Incorrect condition for updating `mx`:

-   Original: `if x > mx`
-   This condition checks if the current number is larger than `mx`, but it should only check negative numbers.
-   Fix: `if x < 0 and x > mx`

### 5. Incorrect output when no negative numbers are found:

-   Original: `print(s)` and `print(mx)`
-   If no negative numbers are found, the program should print `"NO"`, not the sum and maximum values.
-   Fix: Add a condition to print `"NO"` if `s` is not negative.

## Fixed Code 🛠:

```python
mx = (-10 ** 6) - 1  # Start with a number smaller than any negative number
s = 0

for i in range(10):  # Loop through 10 numbers
    x = int(input())

    if x < 0:  # Check if the number is negative
        s += x  # Add to the sum

    if x < 0 and x > mx:  # Find the maximum negative number
        mx = x

if s < 0:  # If there are negative numbers, print the sum and maximum
    print(s)
    print(mx)
else:  # If no negative numbers, print "NO"
    print('NO')
```

## Conclusion 🚀

This program allows the user to process a sequence of 10 integers and find the sum and maximum of negative numbers.
It demonstrates basic control flow, conditionals, and handling of edge cases like the absence of negative numbers.
