# Polynomial Evaluation

## Description

This program evaluates a polynomial at a given value of **x**.
The polynomial is represented as a series of coefficients provided by the user.

The polynomial is of the form:

```
a(n) * x^n + a(n-1) * x^(n-1) + ... + a(2) * x^2 + a(1) * x + a(0)
```

Where `a(n), a(n-1), ..., a(2), a(1), a(0)` are the coefficients of the polynomial, and `x` is the input value at which the polynomial is evaluated.

## Purpose

-   This program helps in evaluating polynomials efficiently using **Horner's method**, which reduces the number of multiplications and additions.

## How It Works

1. **Input**: The user provides the polynomial's coefficients as a space-separated list and an integer value **x**.
2. **Processing**: The polynomial is evaluated using **map()** to convert the coefficients to integers, and **reduce()** to compute the accumulated polynomial value using Horner's method.
3. **Output**: The result is printed as the evaluated value of the polynomial at the given **x**.

### Example

#### Input

```
1 0 -2 3
2
```

#### Output

```
7
```

Explanation:
For the polynomial `x^3 - 2x + 3`, evaluating at `x = 2` results in:

```
2^3 - 2(2) + 3 = 8 - 4 + 3 = 7
```

## Usage

1. Input the list of coefficients of the polynomial, separated by a space.
2. Input the value of **x** at which the polynomial should be evaluated.
3. The program outputs the result of the polynomial evaluation.

## Conclusion

This program provides an efficient method of evaluating polynomials, and it is built using Python's `map()` and `reduce()` functions, ensuring clear and compact code for mathematical computations.
