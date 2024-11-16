# Third Digit Finder

## Description 📝

This program determines the third digit from the beginning of a given natural number `n` (where `n` is greater than 99).
The program extracts and returns the third digit by first reducing the number to a value that has only three or fewer digits and then extracting the rightmost digit.

## Purpose 🎯

The purpose of this program is to extract and return the third digit from a natural number greater than 99.
It helps practice working with integers, division, and modulus operations.

## How It Works 🔍

1. The program receives a natural number `n` (greater than 99) as input.
2. It uses a loop to divide the number by 10 until it has 3 or fewer digits.
3. It then extracts the third digit by using the modulus operator to get the last digit of the resulting number.
4. The third digit is printed as the output.

## Output 📜

The program prints the third digit from the beginning of the number.

## Usage 📦

1. Run the Python script.
2. Input a natural number `n` (greater than 99).
3. The program will print the third digit from the left.

### Example Usage:

1. Run the script.
2. Input: `12345`
3. Output: `3`

## Conclusion 🚀

This program efficiently extracts the third digit of a given number using basic mathematical operations.
It is a simple but useful exercise for manipulating and accessing digits of large numbers.
