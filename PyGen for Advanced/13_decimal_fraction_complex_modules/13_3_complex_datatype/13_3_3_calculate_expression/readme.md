# Complex Expression Calculation

## Description 📝

This Python program calculates the value of the expression involving two complex numbers and their conjugates.
Given a natural number `n` and two complex numbers `z1` and `z2`, the program computes:

```
z1^n + z2^n + conj(z1)^n + conj(z2)^(n+1)
```

Where `conj(z)` is the complex conjugate of `z`.

## Purpose 🎯

The purpose of this program is to compute and output the result of a mathematical expression involving powers and conjugates of complex numbers.
The program uses Python's built-in capabilities for complex number arithmetic, including the conjugate and exponentiation operations.

## How It Works 🔍

1. **Input**:
    - The program reads a natural number `n` and two complex numbers `z1` and `z2`.
2. **Processing**:
    - The program calculates each term in the expression:
        - `z1^n`
        - `z2^n`
        - `conj(z1)^n`
        - `conj(z2)^(n+1)`
    - It sums all four terms.
3. **Output**:
    - The result of the expression is printed as a complex number.

## Output 📜

The program outputs the result of the expression as a complex number.

### Example:

For the input:

```
n = 2
z1 = 3 + 4j
z2 = 1 + 2j
```

The output will be:

```
(49+58j)
```

## Usage 📦

1. Save the code in a file, e.g., `complex_expression.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python complex_expression.py`
5. Enter the values of `n`, `z1`, and `z2` when prompted.

## Conclusion 🚀

This program demonstrates how to perform arithmetic operations on complex numbers in Python, including exponentiation and conjugation, and outputs the result as a complex number.
