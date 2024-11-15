# Code review task 1 🪲

## Description 📝

This program takes a sequence of 10 integers as input and determines the number of non-negative numbers (including zero) in the sequence.
It also calculates their product. If there are no non-negative numbers in the sequence, the program will output `"NO"`.
Otherwise, it will print the count of non-negative numbers and their product.

## Purpose 🎯

The purpose of this program is to:

1. Count how many non-negative numbers exist in a given sequence of 10 integers.
2. Calculate the product of those non-negative numbers.
3. Handle edge cases where no non-negative numbers are found.

## How It Works 🔍

-   The program loops through 10 integers, checking each one to determine if it is non-negative (greater than or equal to 0).
-   If the number is non-negative, the program updates the count and multiplies it with the running product.
-   If no non-negative numbers are found, the program outputs `"NO"`.
-   Otherwise, it prints the count of non-negative numbers and their product.

## Output 📜

-   If there are non-negative numbers, it prints two values:
    -   The count of non-negative numbers.
    -   The product of those non-negative numbers.
-   If there are no non-negative numbers, it prints `"NO"`.

## Usage 📦

1. Run the program.
2. Enter 10 integers one by one.
3. The program will display either the count and product of non-negative numbers, or `"NO"` if there are no non-negative numbers.

## Identified Errors in the Original Code 🕵🏾:

### 1. Incorrect range for the loop:

-   Original: `for i in range(1, 10)`
-   The program needs to process 10 integers, so the range should be from 1 to 11 (not 1 to 10).
-   Fix: `for i in range(1, 11)`

### 2. Incorrect initial value of p:

-   Original: `p = 0`
-   If the product starts at 0, multiplying any number by it will always result in 0.
    The correct initial value should be 1.
-   Fix: `p = 1`

### 3. Incorrect check for non-negative numbers:

-   Original: `if x > 0`
-   This condition checks if the number is strictly positive.
    However, the task requires checking for non-negative numbers **(i.e., x≥0)**.
-   Fix: `if x >= 0`

### 4.Incorrect output for the product:

-   Original: `print(x)`
-   The program prints `x` after checking the count of non-negative numbers.
    This is incorrect since we need to print the product of the non-negative numbers, not the last entered number.
-   Fix: print(p)

## Fixed code 🛠:

```python
count = 0
p = 1  # Start with 1, since multiplying by 0 will always result in 0
for i in range(1, 11):  # We need to process 10 integers
    x = int(input())
    if x >= 0:  # Check if the number is non-negative
        p *= x
        count += 1
if count > 0:
    print(count)  # Print the count of non-negative numbers
    print(p)  # Print the product of non-negative numbers
else:
    print('NO')  # If no non-negative numbers are found
```

## Explanation of Changes 🧾:

1. **Range adjusted**: Changed the loop range to process exactly 10 integers.
2. **Initialization of `p`**: Set `p = 1` to correctly calculate the product.
3. **Condition for non-negative numbers**: Changed the check to `x >= 0` to include zero as a non-negative number.
4. **Correct output for product**: Changed the output to print the product (`p`) instead of the last number entered (`x`).

## Conclusion 🚀

This program helps to process sequences of integers and find specific patterns related to non-negative numbers.
It demonstrates basic control flow, conditional checks, and mathematical operations like multiplication and counting.
