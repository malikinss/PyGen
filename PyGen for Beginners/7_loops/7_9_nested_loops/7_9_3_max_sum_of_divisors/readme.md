# Max Sum of Divisors Finder

## Description 📝

This program finds the natural number within a given range [a, b] that has the maximum sum of divisors.
If there are multiple numbers with the same sum, the largest number is selected.

## Purpose 🎯

To find and print the natural number in the interval [a, b] that has the highest sum of divisors.
The program iterates through all numbers in the range and computes the sum of their divisors, then identifies the number with the maximum sum.

### Example

```bash
Input: a = 10 b = 20
Output: 18 39
```

In this case:

-   The sum of divisors of 18 is 39.
-   The program finds 18 as the number with the highest sum of divisors in the range [10, 20].

## How It Works 🔍

1. The program receives two natural numbers \(a\) and \(b\), where \(a < b\), as input.
2. It then iterates through each number in the range [a, b].
3. For each number, it calculates the sum of its divisors.
4. The program keeps track of the number with the maximum sum of divisors.
5. If multiple numbers have the same sum, it chooses the largest number.
6. Finally, the program prints the number with the maximum sum of divisors and the sum.

## Output 📜

The program prints:

-   The number with the maximum sum of divisors.
-   The sum of divisors of that number.

### Example Output

```bash
18 39
```

## Usage 📦

1. Run the Python script.
2. Input two natural numbers \(a\) and \(b\) where \(a < b\).
3. The program will print the number with the highest sum of divisors in the range [a, b] and the sum itself.

### Example Usage

1. Run the script.
2. Input: `a = 10 b = 20`
3. Output: `18 39`

## Conclusion 🚀

This program demonstrates how to compute the sum of divisors of numbers within a range and how to track the number with the largest sum, which is a useful exercise in number theory and Python programming.
