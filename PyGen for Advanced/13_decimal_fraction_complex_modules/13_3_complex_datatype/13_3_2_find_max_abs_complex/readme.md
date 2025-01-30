# Complex Number with Maximum Absolute Value

## Description 📝

This Python program receives a list of complex numbers and calculates the complex number with the largest absolute value.
The program then prints the complex number and its absolute value.

## Purpose 🎯

The purpose of this program is to demonstrate how to find and print the complex number with the largest absolute value from a list of complex numbers.
The absolute value is calculated using Python's built-in `abs()` function.

## How It Works 🔍

1. **Input**:
    - The program uses a predefined list of complex numbers. You can modify this list to include any complex numbers you'd like to test.
2. **Processing**:
    - The program calculates the absolute value of each complex number using the built-in `abs()` function.
    - It finds the complex number with the maximum absolute value using Python’s `max()` function, with `abs` as the key for comparison.
3. **Output**:
    - The program prints the complex number with the largest absolute value and its absolute value on separate lines.

## Output 📜

The program outputs the complex number with the largest absolute value and its absolute value.

### Example:

For the list of complex numbers:

```
[3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
```

The output will be:

```
(-20+15j)
25.0
```

## Usage 📦

1. Save the code in a file, e.g., `max_abs_complex.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python max_abs_complex.py`
5. The program will print the complex number with the largest absolute value and its absolute value.

## Conclusion 🚀

This program efficiently identifies the complex number with the largest absolute value from a list of complex numbers and outputs the result.
It demonstrates how to use Python's built-in functions for handling complex numbers and computing their absolute values.
