# Sum of Sequence Until Negative Number

## Description 📝

This program reads a sequence of integers from user input and calculates the sum of all non-negative integers in the sequence.
The sequence ends when a negative integer is entered, which signals termination but is not included in the sum.

## Purpose 🎯

The program demonstrates basic looping, conditional checks, and summation of inputs.
It allows continuous input processing until a specific condition (negative number) is met to end the loop.

## How It Works 🔍

1. The program initializes a sum variable, `sequence_sum`, to zero.
2. It enters a loop to continuously read integers from user input.
3. For each integer:
    - If it is non-negative, the program adds it to `sequence_sum`.
    - If it is negative, the program exits the loop.
4. Finally, it prints the total sum of all non-negative integers entered.

## Output 📜

The output is the total sum of all non-negative integers in the sequence.

### Example

```bash
Input: 5 10 15 -3
Output: Sum of the sequence: 30

```

## Usage 📦

1. Run the script in a Python environment.
2. Enter integers one at a time.
3. The program sums each non-negative integer until a negative integer is entered, which will end the input and trigger the result display.

## Conclusion 🚀

This program efficiently handles input summation with conditional termination, showcasing basic control flow and input validation in Python.
