# Isosceles Star Triangle Printer

## Description 📝

This program prints an isosceles star triangle with a given odd natural number \( n \) as its base.
The height of the triangle is also \( n \), with the number of stars increasing until the middle of the triangle and then decreasing symmetrically.
The triangle is centered and forms a shape that is wide at the middle and tapers towards the top and bottom.

## Purpose 🎯

To generate an isosceles triangle pattern using stars ('\*'), where the base and height are both given as an odd natural number \( n \).
The pattern has an increasing number of stars until the middle, followed by a decreasing number of stars after the middle.

## How It Works 🔍

1. The program takes an odd natural number \( n \) as input.
2. It prints the upper part of the triangle (including the middle) by incrementing the number of stars in each row.
3. Then, it prints the lower part of the triangle by decrementing the number of stars in each row after the middle.
4. The pattern is printed using nested loops, where the outer loop controls the number of rows, and the inner loop prints the stars.

### Example

```bash
Input: 7
Output:
        *
        **
        ***
        ****
        ***
        **
        *
```

In this case:

-   The base and height of the triangle are 7 stars.
-   The number of stars in each row increases until the middle and then decreases symmetrically.

## Output 📜

The program prints an isosceles triangle pattern of stars.
Each row contains a number of stars corresponding to the row number, increasing to the middle and then decreasing.

## Usage 📦

1. Run the script in a Python environment.
2. Enter an odd natural number \( n \) for the base and height of the triangle.
3. The program will print an isosceles triangle with the given number of rows and base.

### Example Usage

1. Run the script.
2. Input: `n = 7`.
3. Output:
    ```bash
    *
    **
    ***
    ****
    ***
    **
    *
    ```

## Conclusion 🚀

This program generates a simple, visually appealing isosceles triangle pattern with stars.
It is a great example of using nested loops to generate a symmetrical pattern, and it provides a good exercise for working with loops in Python.
