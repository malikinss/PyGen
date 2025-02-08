# Sphere Point Location Checker 🌐

## Description 📝

This program checks if a set of 3D points, defined by their abscissas (x), ordinates (y), and applicates (z), lie inside or on the surface of a sphere centered at the origin with a radius of 2 units.

## Purpose 🎯

The goal is to determine whether each point in the 3D space falls within the boundary of a sphere with a radius of 2, using the equation of a sphere:  
\[
x^2 + y^2 + z^2 \leq R^2
\]

## How It Works 🔍

1. The function `is_inside_sphere(x, y, z)` computes whether a single point lies inside or on the sphere by checking if the sum of squares of its coordinates is less than or equal to the square of the radius (4 in this case).
2. The function `all_points_inside()` uses `zip()` to iterate through the three lists (abscissas, ordinates, applicates) and checks if all points satisfy the condition using the `all()` function.
3. `read_floats()` is used to read and convert input data into lists of floats.
4. The program checks whether all points are inside or on the sphere and outputs the result as `True` or `False`.

## Output 📜

-   **True** if all points are inside or on the surface of the sphere.
-   **False** if any point is outside the sphere.

### Example Output:

```
True
```

## Usage 📦

1. Input three lines of space-separated real numbers representing the coordinates (x, y, z) of points.
2. The program checks if all points are inside or on the surface of the sphere.
3. The result is printed: `True` if all points are inside or on the sphere, otherwise `False`.

## Conclusion 🚀

This program efficiently determines the location of 3D points relative to a sphere using mathematical conditions and Python's built-in functions for iteration and logical checking.
