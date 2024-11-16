# Sum of Factorials

## Description 📝

This program calculates the sum of factorials from 1! to n!. The factorial of a number `x`, denoted `x!`, is the product of all positive integers less than or equal to `x`.
The program computes the sum: `1! + 2! + 3! + ... + n!`

## Purpose 🎯

The goal of the program is to calculate the sum of factorials of all numbers from 1 to `n`, where `n` is a natural number input by the user. Factorials are calculated for each number in the range and then summed up to produce the final result.

### Example:

```bash
Input: 4
Output: 33
```

In this example:

-   The sum of factorials is:
    -   `1! = 1`
    -   `2! = 2`
    -   `3! = 6`
    -   `4! = 24`
-   The total sum is `1 + 2 + 6 + 24 = 33`.

## How It Works 🔍

1. The program receives a natural number `n` as input.
2. It calculates the factorial of each integer from 1 to `n`.
3. The factorial of each number is added to the cumulative sum.
4. The final result is the sum of factorials.

## Output 📜

The program outputs the total sum of the factorials from 1! to n!.

## Usage 📦

1. Run the Python script.
2. Input a natural number `n`.
3. The program will output the sum of the factorials from 1! to n!.

### Example Usage:

1. Run the script.
2. Input: 4
3. Output: 33

## Conclusion 🚀

This program efficiently calculates the sum of factorials from 1! to n!, using nested loops to compute each factorial and accumulate the total sum.
