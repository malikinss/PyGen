# Code Review: Display the First (Highest) Digit of a Natural Number 🔢

## Description 📝

This program takes a natural number as input and aims to display its first (highest) digit.
The original program contains errors that need to be identified and fixed.

## Purpose 🎯

The goal of the program is to:

1. Take a natural number as input.
2. Extract and display the first (highest) digit of the number.

## How It Works 🔍

-   The program reads an integer from the user input.
-   It iterates through the digits of the number, gradually removing the last digits until only the first (highest) digit remains.
-   The first digit is then printed as the result.

## Output 📜

-   The program outputs the first (highest) digit of the given natural number.

## Usage 📦

1. Run the program.
2. Enter a natural number.
3. The program will output the first (highest) digit of the number.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect modulus operation to get the first digit:

-   Original: `n %= 10`
-   This operation keeps getting the last digit of `n`, which will not help in finding the first digit.
    We need to remove the last digits of the number until only the first digit remains.
-   Fix: Use integer division (`//= 10`) to remove the last digit repeatedly.

### 2. Infinite loop due to incorrect condition in the while loop:

-   Original: `while n > 0:`
-   The loop condition does not stop correctly when the number has been reduced to its first digit.
    We need to ensure the loop stops once we have the highest digit.
-   Fix: Change the loop condition to `while n > 9` to keep dividing until `n` is reduced to a single-digit number.

## Fixed Code 🛠:

```python
n = int(input())  # Input the number

while n > 9:  # Keep removing digits until the first digit is left
    n //= 10  # Integer division to remove the last digit

print(n)  # Output the first (highest) digit
```

## Conclusion 🚀

This program now correctly extracts the first digit of a natural number by repeatedly dividing by 10 until only the first digit remains.
It ensures the correct handling of the number and terminates when the first digit is obtained.
