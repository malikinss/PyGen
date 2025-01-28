# Largest Proper Irreducible Fraction

## Description 📝

This Python program calculates the largest proper irreducible fraction where the sum of the numerator and denominator equals a given natural number \( n \). A fraction is considered proper if its numerator is smaller than the denominator, and irreducible if there is no fraction with smaller natural numerator and denominator that is equal to it.

## Purpose 🎯

The program determines the largest proper irreducible fraction where the sum of the numerator and denominator is equal to a given natural number \( n \), and outputs the fraction in the form "numerator/denominator".

## How It Works 🔍

1. **Input**:
    - A natural number \( n \) is provided by the user.
2. **Processing**:
    - The program iterates through possible numerators from 1 to \( n-1 \).
    - For each numerator, it computes the corresponding denominator as \( n - \text{numerator} \).
    - The program checks whether the fraction is proper (i.e., the numerator is smaller than the denominator) and irreducible (i.e., the greatest common divisor of the numerator and denominator is 1).
    - Among all valid proper irreducible fractions, the program selects the one with the largest value.
3. **Output**:
    - The program prints the largest proper irreducible fraction in the form "numerator/denominator".

## Output 📜

The program outputs the largest proper irreducible fraction where the sum of the numerator and denominator equals the input number \( n \).

### Example:

For the input:

```
n = 12
```

The output will be:

```
5/7
```

## Usage 📦

1. Save the code in a file, e.g., `largest_fraction.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python largest_fraction.py`
5. Enter a natural number \( n \) when prompted, and the result will be displayed.

## Conclusion 🚀

This program efficiently computes the largest proper irreducible fraction for a given \( n \). It is useful for exploring properties of fractions and finding the largest possible proper irreducible fraction with a given sum of the numerator and denominator. 🎯
