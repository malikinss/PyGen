# Code Review Task 1 🪲

## Description 📝

This program processes a natural number and calculates the sum of its even digits.
If the number contains no even digits, the program outputs `0`.

## Purpose 🎯

The purpose of this program is to:

1. Identify and sum all even digits in a given natural number.
2. Handle cases where no even digits are found by outputting `0`.
3. Correct logical and syntactical errors in the initial implementation.

## How It Works 🔍

-   The program converts the user input into an integer.
-   It loops through the digits of the number by repeatedly dividing it by 10.
-   For each digit, the program checks if it is even.
-   If the digit is even, it adds it to the running total `s`.
-   After processing all digits, it outputs the sum.

## Output 📜

-   If the number contains even digits, the program prints the sum of those digits.
-   If no even digits are found, it prints `0`.

## Identified Errors in the Original Code 🕵🏾:

1. Incorrect data type for input:

-   Original: `n = input()`
-   The `input()` function returns a string, but the program treats `n` as an integer during calculations.
-   Fix: Convert the input to an integer using `n = int(input())`.

2. Incorrect loop condition:

-   Original: `while n > 10`
-   The loop exits prematurely if the number becomes a single-digit number (`n ≤ 10`).
-   Fix: Change the condition to `while n > 0` to ensure all digits are processed.

3. Incorrect condition for even digits:

-   Original: `if n % 2 == 1`
-   This checks for odd digits instead of even digits.
-   Fix: Change the condition to `if n % 2 == 0`.

4. Incorrect update of the sum:

-   Original: `s = n % 10`
-   This overwrites `s` with the current digit instead of adding the digit to the sum.
-   Fix: Use `s += n % 10`.

## Fixed Code 🛠:

```python
n = int(input())  # Convert input to integer
s = 0  # Initialize the sum of even digits

while n > 0:  # Process all digits
    if n % 2 == 0:  # Check if the current digit is even
        s += n % 10  # Add the even digit to the sum
    n //= 10  # Remove the last digit

print(s)  # Output the sum of even digits
```

## Explanation of Changes 🧾:

1. **Input conversion**: Converted the input to an integer for numerical operations.
2. **Loop condition**: Ensured all digits of the number are processed by updating the condition to `while n > 0`.
3. **Condition for even digits**: Fixed the check to correctly identify even digits.
4. **Sum calculation**: Adjusted the calculation to accumulate the sum of even digits instead of overwriting the variable.

## Conclusion 🚀

This program effectively processes a natural number to find and sum its even digits.
By identifying and fixing the logical and syntactical errors, the program now functions as intended, demonstrating the importance of thorough code review.
