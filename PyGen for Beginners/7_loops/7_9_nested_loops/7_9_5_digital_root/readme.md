# Digital Root Calculation

## Description 📝

This program calculates the **digital root** of a given number.
The digital root is obtained by repeatedly summing the digits of a number until a single-digit number is obtained.

## Purpose 🎯

The purpose of this program is to calculate the digital root of any natural number.
It does so by continuously summing the digits of the number until the result is a single-digit number.

### Example:

```bash
Input: 12345
Output: 6
```

In this example:

-   The sum of digits of 12345 is `1 + 2 + 3 + 4 + 5 = 15`.
-   The sum of digits of 15 is `1 + 5 = 6`.
    Thus, the digital root of 12345 is 6.

## How It Works 🔍

1. The program receives a natural number `n` as input.
2. It continuously sums the digits of the number.
3. If the sum results in a number greater than 9, the sum of the digits is calculated again until a single-digit number is obtained.
4. The final single-digit result is the digital root.

## Output 📜

The program will output the **digital root** of the given number.

## Usage 📦

1. Run the Python script.
2. Input a natural number `n`.
3. The program will output the digital root of `n`.

### Example Usage:

1. Run the script.
2. Input: `12345`
3. Output: `6`

## Conclusion 🚀

This program calculates the digital root of a given number, providing an easy way to reduce any number to a single-digit sum.
The method utilizes nested while loops to repeatedly sum the digits until the desired result is achieved.
