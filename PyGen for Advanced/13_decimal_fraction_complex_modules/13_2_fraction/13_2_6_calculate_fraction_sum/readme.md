# Sum of Rational Numbers Involving Factorials

## Description 📝

This Python program calculates the sum of a series of rational numbers, where the expression is of the form:

\[
1/1! + 1/2! + 1/3! + \ldots + 1/n!
\]

The sum is computed for a given natural number \( n \), and the result is displayed as a simplified fraction.

## Purpose 🎯

The program computes the sum of the series \( 1/i! \) from \( i = 1 \) to \( i = n \), and outputs the result as a rational number in its simplest form.

## How It Works 🔍

1. **Input**:
    - A natural number \( n \) is provided by the user.
2. **Processing**:
    - The program calculates the sum of the series \( 1/i! \) for each integer \( i \) from 1 to \( n \), using Python’s `math.factorial` function.
    - It uses Python’s `fractions.Fraction` class to ensure that the result is always in the simplest fractional form.
3. **Output**:
    - The program prints the sum of the series as a fraction.

## Output 📜

The program outputs the sum of the series as a rational number in simplified form.

### Example:

For the input:

```
n = 3
```

The output will be:

```
1/1 + 1/2 + 1/6 = 8/6 = 4/3
```

## Usage 📦

1. Save the code in a file, e.g., `factorial_series.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python factorial_series.py`
5. Enter a natural number \( n \) when prompted, and the result will be displayed.

## Conclusion 🚀

This program efficiently calculates and displays the sum of the series \( 1/i! \), providing an exact rational result. It is useful for handling factorial-based summations and ensuring the result is in the simplest form. 🎯
