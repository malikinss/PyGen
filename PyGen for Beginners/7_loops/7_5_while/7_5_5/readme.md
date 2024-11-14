# Second Digit Finder

## Description 📝

This program takes a natural number `n` (where `n > 9`) as input and returns its second digit from the left.
It extracts the second digit by first reducing the number to a two-digit number and then obtaining the first digit of the reduced number.

## Purpose 🎯

The purpose of this program is to demonstrate how to extract a specific digit (in this case, the second digit from the left) from a natural number. This task involves integer division to reduce the number to the desired length and then using the modulus operation to obtain the specific digit.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. It continuously divides `n` by 10 until only two digits remain.
3. After reducing the number to two digits, the program uses the modulus operator (`% 10`) to extract the second digit from the left.
4. The second digit is returned and printed.

### Example

```bash
Input: 2857
Output: 8

```

In this example:

-   The second digit from the left of `2857` is `8`.

## Output 📜

The program outputs the second digit from the left of the given natural number.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number `n` (where `n > 9`).
3. The program will output the second digit from the left.

## Conclusion 🚀

This program showcases how to extract a specific digit from a natural number by reducing it to the desired number of digits and using basic mathematical operations.
