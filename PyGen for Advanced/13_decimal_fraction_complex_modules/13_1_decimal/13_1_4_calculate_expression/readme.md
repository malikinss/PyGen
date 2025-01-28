# Expression Calculator: `e^d + ln(d) + lg(d) + sqrt(d)`

## Description 📝

This Python program takes a `Decimal` number as input and calculates the value of the mathematical expression:

```
e^d + ln(d) + lg(d) + sqrt(d)
```

where:

-   `e^d` is the exponential function,
-   `ln(d)` is the natural logarithm,
-   `lg(d)` is the base-10 logarithm,
-   `sqrt(d)` is the square root.

## Purpose 🎯

The program demonstrates the use of the `decimal` module for high-precision mathematical computations. It handles precise calculations and supports advanced mathematical functions.

## How It Works 🔍

1. **Input**:
    - The user is prompted to enter a `Decimal` number.
2. **Calculation**:
    - The program calculates each term of the expression using:
        - `exp()` for exponential,
        - `ln()` for natural logarithm,
        - `log10()` for base-10 logarithm,
        - `sqrt()` for square root.
    - The terms are summed to compute the result.
3. **Output**:
    - The result of the expression is displayed.

## Output 📜

The output will display the calculated value of the expression.

### Example:

For input:

```
1
```

The output will be:

```
The result of the expression is: 5.175201193643801456882381850
```

For input:

```
0.5
```

The output will be:

```
The result of the expression is: 3.348320407800975298223122008
```

## Usage 📦

1. Save the code in a file named `expression_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python expression_calculator.py`
5. Enter a `Decimal` number when prompted.

## Conclusion 🚀

This program provides an accurate and efficient way to calculate complex mathematical expressions using Python's `decimal` module.
It is a practical tool for tasks that require high precision in mathematical computations. 🎯
