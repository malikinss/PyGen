# Decimal to Fraction Converter

## Description 📝

This Python program takes a list of decimal numbers (stored as strings) and converts each of them to its equivalent representation as a common fraction.
It then prints each decimal number along with its simplified fraction.

## Purpose 🎯

The program demonstrates how to convert decimal numbers to fractions using Python's `fractions.Fraction` class. It simplifies the fractions and displays them in an easy-to-read format.

## How It Works 🔍

1. **Input**:
    - The program uses a list of decimal numbers stored as strings.
2. **Conversion**:
    - For each decimal number in the list, the program converts the string to a `Fraction` and simplifies it using the `limit_denominator()` method.
3. **Output**:
    - The program prints each decimal number and its equivalent fraction in the format `decimal_number = common_fraction`.

## Output 📜

The output will show the decimal number and its equivalent fraction.

### Example:

For the decimal string `6.34`, the output will be:

```
6.34 = 317/50
```

For the decimal string `0.75`, the output will be:

```
0.75 = 3/4
```

## Usage 📦

1. Save the code in a file named `decimal_to_fraction.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python decimal_to_fraction.py`
5. The results will be printed directly to the console.

## Conclusion 🚀

This program provides a simple and efficient way to convert decimal numbers to fractions and display them in a readable format. It’s useful for applications where exact fractional representations are needed. 🎯
