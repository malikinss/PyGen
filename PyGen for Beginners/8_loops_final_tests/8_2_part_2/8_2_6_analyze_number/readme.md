# Number Analyzer

## Description 📝

This program analyzes a given natural number and calculates various properties about its digits.
It performs the following calculations:

1. The number of occurrences of the digit `3`.
2. The frequency of the last digit in the number.
3. The count of even digits.
4. The sum of digits greater than five.
5. The result of multiplying digits greater than seven (or 1 if none are found).
6. The total count of occurrences of the digits `0` and `5`.

## Purpose 🎯

The purpose of this program is to perform a detailed analysis of a natural number by evaluating its digits.
It helps in practicing basic arithmetic operations, loops, and conditionals in Python.

## How It Works 🔍

1. The program receives a natural number as input.
2. It iterates through the digits of the number using modulus and integer division to extract each digit.
3. For each digit, the program checks if it matches certain criteria:
    - It counts how many times the digit `3` appears.
    - It counts how many times the last digit appears.
    - It counts how many even digits are present.
    - It calculates the sum of digits greater than five.
    - It multiplies digits greater than seven.
    - It counts occurrences of `0` and `5`.
4. Finally, the results are printed.

## Output 📜

The program outputs six integers representing the results of the analysis:

-   The number of `3` digits.
-   The number of times the last digit appears.
-   The number of even digits.
-   The sum of digits greater than five.
-   The product of digits greater than seven (or 1 if none are found).
-   The count of `0` and `5` digits.

## Usage 📦

1. Run the Python script.
2. Input a natural number.
3. The program will print the six calculated values.

### Example Usage:

1. Run the script.
2. Input: `357975`
3. Output: `1 2 3 15 35 2`

## Conclusion 🚀

This program provides a detailed breakdown of the digits in a number, including counts, sums, and products.
It is a great tool for practicing digit manipulation and basic arithmetic in Python.
