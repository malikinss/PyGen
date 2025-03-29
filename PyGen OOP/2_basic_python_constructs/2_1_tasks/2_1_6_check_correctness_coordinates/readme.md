# Geographic Coordinates Validator 🌍

## Description 📝

This program checks whether a given sequence of strings represents valid geographic coordinates.
The coordinates must be in the format `(x, y)` where `x` is the latitude (between -90 and 90) and `y` is the longitude (between -180 and 180).

## Purpose 🎯

The purpose of this program is to validate strings representing geographic coordinates to ensure they are within the valid ranges for latitude and longitude.
It helps in determining whether the given coordinate strings are correct for use in geographic applications.

## How It Works 🔍

1. The program takes an arbitrary number of input strings, each representing geographic coordinates.
2. For each string, the program checks:
    - Whether it follows the format `(x, y)` where `x` is the latitude and `y` is the longitude.
    - Whether `x` is within the valid range for latitude (-90 ≤ x ≤ 90).
    - Whether `y` is within the valid range for longitude (-180 ≤ y ≤ 180).
3. The program outputs `True` for each valid coordinate and `False` otherwise.

### Example Input:

```
(45, 180)
(-91, 45)
(60, -200)
(23.5, -78)
```

### Example Output:

```
True
False
False
True
```

## Output 📜

The program prints `True` for valid geographic coordinates and `False` for invalid ones.

## Usage 📦

1. Input the coordinate strings in the format `(latitude, longitude)`.
2. The program will check each string and output `True` or `False` for each one based on its validity.

### Example:

```python
input_data = [
    "(45, 180)",
    "(-91, 45)",
    "(60, -200)",
    "(23.5, -78)"
]
result = check_correctness_coordinates(input_data)
print(*result, sep="\n")  # Output: True False False True
```

## Conclusion 🚀

This program ensures that the coordinates provided for geographic operations are valid and within the acceptable range, making it suitable for applications that require geographic data validation.
