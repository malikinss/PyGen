# Sum of Max and Min as Fraction

## Description 📝

This Python program takes a string of decimal numbers separated by spaces, finds the maximum and minimum values among them, calculates their sum, and returns the result as a simplified fraction.

## Purpose 🎯

The program demonstrates how to process a list of decimal numbers, find the largest and smallest, and compute their sum in fractional form using Python's `fractions.Fraction` class.

## How It Works 🔍

1. **Input**:
    - A string containing decimal numbers separated by spaces.
2. **Processing**:
    - The program converts the string into a list of `Decimal` objects for precision.
    - It then finds the largest and smallest numbers in the list.
    - The sum of the largest and smallest numbers is calculated.
3. **Output**:
    - The program outputs the sum of the largest and smallest numbers as a simplified common fraction.

## Output 📜

The program will print the sum of the largest and smallest decimal numbers in the list as a fraction.

### Example:

For the input string:

```

'0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

```

The output will be:

```

Fraction(10, 1)

```

## Usage 📦

1. Save the code in a file, e.g., `sum_max_min_as_fraction.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python sum_max_min_as_fraction.py`
5. The result will be printed to the console.

## Conclusion 🚀

This program provides a simple way to calculate the sum of the maximum and minimum decimal numbers from a list and return it as a fraction. It can be useful for mathematical or financial applications requiring precise fractional representations. 🎯
