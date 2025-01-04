# Parabola Vertex Calculation 📐

## Description 📝

This program calculates the vertex of a parabola given its coefficients from the equation \(y = ax^2 + bx + c\), where \(a \neq 0\).
The vertex of the parabola is determined by the formulas:

-   \( x = \frac{-b}{2a} \)
-   \( y = \frac{4ac - b^2}{4a} \)

## Purpose 🎯

-   To calculate the vertex coordinates (x, y) of a parabola from its coefficients.
-   To demonstrate the use of mathematical formulas in a program.

## How It Works 🔍

1. **Function `find_parabola_vertex(a, b, c)`**:

    - Takes the coefficients of the parabola equation \(a\), \(b\), and \(c\).
    - Calculates the x-coordinate using \( x = \frac{-b}{2a} \).
    - Calculates the y-coordinate using \( y = \frac{4ac - b^2}{4a} \).
    - Returns a tuple with the coordinates of the vertex.

2. **Input**:

    - The program receives three integer inputs: \(a\), \(b\), and \(c\).

3. **Output**:
    - The program prints the coordinates of the vertex as a tuple \((x, y)\).

### Example:

```
Input:
2
3
1

Output:
(-0.75, 0.125)
```

## Output 📜

The output will be the coordinates of the parabola's vertex, like:

```
(-0.75, 0.125)
```

## Conclusion 🚀

The program successfully calculates and outputs the vertex of a parabola given its equation coefficients \(a\), \(b\), and \(c\).
