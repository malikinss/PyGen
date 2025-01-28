# Irreducible Fractions Between 0 and 1

## Description 📝

This Python program calculates all irreducible fractions between 0 and 1 where the denominator does not exceed a given natural number \( n \). The fractions are output in ascending order.

A fraction is irreducible if the greatest common divisor (GCD) of its numerator and denominator is 1.

## Purpose 🎯

The program finds all irreducible fractions between 0 and 1 where the denominator is less than or equal to \( n \), and prints them in ascending order.

## How It Works 🔍

1. **Input**:
    - A natural number \( n \) is provided by the user, which represents the maximum denominator.
2. **Processing**:
    - The program iterates through all possible denominators from 2 to \( n \).
    - For each denominator, it checks all possible numerators from 1 to \( \text{denominator} - 1 \).
    - The program ensures that the fraction is irreducible by checking if the GCD of the numerator and denominator is 1.
    - It collects all valid irreducible fractions and stores them in a list.
3. **Output**:
    - The program sorts the list of irreducible fractions in ascending order and prints each fraction on a new line.

## Output 📜

The program outputs all irreducible fractions between 0 and 1 with denominators not exceeding the input number \( n \).

### Example:

For the input:

```

n = 6

```

The output will be:

```

1/2
1/3
2/3
1/4
3/4
1/5
2/5
3/5
4/5
1/6
5/6

```

## Usage 📦

1. Save the code in a file, e.g., `irreducible_fractions.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python irreducible_fractions.py`
5. Enter a natural number \( n \) when prompted, and the result will be displayed.

## Conclusion 🚀

This program efficiently computes all irreducible fractions between 0 and 1 with denominators not exceeding \( n \) and outputs them in ascending order. It is useful for exploring the properties of fractions and understanding which fractions are irreducible for a given range of denominators. 🎯

```

```
