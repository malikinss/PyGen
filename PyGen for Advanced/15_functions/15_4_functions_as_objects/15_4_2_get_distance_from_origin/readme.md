# Sorting Points by Distance from Origin

## Description

The program sorts a list of points in a 2D plane based on their distance from the origin (0, 0). The distance is calculated using the formula \( \text{OA} = \sqrt{x^2 + y^2} \), where \( (x, y) \) are the coordinates of the point.

## Purpose

This program demonstrates how to sort a list of tuples (representing points) by their calculated distance from the origin using Python's built-in `sort()` function and a custom key function.

## How It Works

1. The `get_distance_from_origin()` function calculates the Euclidean distance from the origin to a given point using the formula \( \sqrt{x^2 + y^2} \).
2. The `points` list contains tuples of integer coordinates, each representing a point in the 2D plane.
3. The `sort()` method is applied to the list of points, using `get_distance_from_origin` as the key function to sort the points by their distance from the origin.
4. The sorted list of points is then printed.

## Usage

Example:

```python
points = [
    (-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0),
    (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)
]

# Sort the list of points by distance from the origin
points.sort(key=get_distance_from_origin)

print(points)
```

## Output

```
[(0, 0), (0, 1), (2, 0), (3, 0), (-1, 1), (-3, 2), (4, 3), (3, 6), (5, 6), (12, 0), (-1, 3), (8, 8), (-9, 1)]
```

## Conclusion

This program successfully sorts a list of points based on their distance from the origin, utilizing the Euclidean distance formula and Python's sorting capabilities. The sorted list provides a quick overview of the points ordered by proximity to the origin.
