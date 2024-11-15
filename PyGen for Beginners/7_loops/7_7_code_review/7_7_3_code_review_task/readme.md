# Code Review: Sum of Even Numbers in a Sequence 🔢

## Description 📝

This program processes a sequence of 7 integers and calculates the sum of all even numbers in the sequence.
If no even numbers are present, it will output 0.
The program is designed to handle a sequence of integers, ensuring it correctly identifies and sums even numbers.

## Purpose 🎯

The purpose of this program is to:

1. Identify all even numbers in a sequence of 7 integers.
2. Compute the sum of all even numbers.
3. Output the sum of even numbers, or 0 if no even numbers are found.

## How It Works 🔍

-   The program loops through a sequence of 7 integers.
-   It checks if each number is even (i.e., divisible by 2).
-   If the number is even, it adds it to the sum.
-   After processing all numbers, it prints the total sum of the even numbers, or 0 if no even numbers are found.

## Output 📜

-   The program will output:
    -   The sum of all even numbers in the sequence if there are any.
    -   0 if there are no even numbers in the sequence.

## Usage 📦

1. Run the program.
2. Enter 7 integers, one by one.
3. The program will output the sum of even numbers or 0 if none are found.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect initialization of `s`:

-   Original: `s = 1`
-   The sum should start at 0 to correctly sum the even numbers.
-   Fix: `s = 0`

### 2. Incorrect range in the loop:

-   Original: `for i in range(1, 7)`
-   The loop should run exactly 7 times to process 7 integers.
    The range should be from 0 to 6 (inclusive).
-   Fix: `for i in range(7)`

### 3. `n` is not converted to an integer:

-   Original: `n = input()`
-   The input is received as a string, but we need to convert it to an integer before performing any calculations.
-   Fix: `n = int(input())`

### 4. Incorrect condition for identifying even numbers:

-   Original: `if i % 2 == 0`
-   The condition should check if the number `n` is even, not the loop index `i`.
-   Fix: `if n % 2 == 0`

## Fixed Code 🛠:

```python
s = 0  # Initialize sum to 0

for i in range(7):  # Loop through exactly 7 integers
    n = int(input())  # Convert input to integer

    if n % 2 == 0:  # Check if the number is even
        s += n  # Add even number to sum

print(s)  # Output the sum of even numbers
```

## Conclusion 🚀

This program correctly processes a sequence of 7 integers to compute the sum of all even numbers.
It properly identifies even numbers, handles the input conversion, and provides the correct output, including returning 0 if no even numbers are found.
