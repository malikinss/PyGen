# Divisibility Graphical Representation

## Description 📝

This program takes a natural number `n` as input and displays a graphical representation of the divisibility of numbers from 1 to `n`.
For each number in this range, the program prints the number followed by as many "+" characters as there are divisors for that number.

## Purpose 🎯

The purpose of this program is to visually represent the divisibility of numbers in the range from 1 to `n`. By counting the divisors of each number and displaying them with "+" characters, the program provides an intuitive way to understand how divisibility works for each number.

### Example:

```bash
Input: 5
Output: 1+
        2++
        3++
        4+++
        5++
```

In this example:

-   1 has 1 divisor (`1`).
-   2 has 2 divisors (`1`, `2`).
-   3 has 2 divisors (`1`, `3`).
-   4 has 3 divisors (`1`, `2`, `4`).
-   5 has 2 divisors (`1`, `5`).

## How It Works 🔍

1. The program receives an input value `n`, which defines the range from 1 to `n` inclusive.
2. For each number in this range, the program calculates the number of divisors.
3. It then prints the number followed by a number of "+" characters equal to the number of divisors of the number.
4. This process continues for all numbers from 1 to `n`.

## Output 📜

The program outputs the number followed by "+" characters corresponding to its divisors for all numbers from 1 to `n`.

### Example Output:

```bash
Output: 1+
        2++
        3++
        4+++
        5++
```

## Usage 📦

1. Run the Python script.
2. Input a natural number `n`.
3. The program will output the divisibility graph for numbers from 1 to `n`.

### Example Usage:

1. Run the script.
2. Input: `5`
3. Output:

```bash
Output: 1+
        2++
        3++
        4+++
        5++
```

## Conclusion 🚀

This program provides a simple yet effective way to visualize the divisibility of numbers.
It can help users better understand the concept of divisors and divisibility in an intuitive and graphical manner.
