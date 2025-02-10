# Index of Nearest Number

## Description 📝

The `index_of_nearest()` function finds the index of the number closest to a given number within a list of integers.
If multiple numbers have the same closest difference, the function returns the smallest index.

## Purpose 🎯

This function is useful for searching the nearest value in a list, which can be applied in:

-   Data analysis
-   Finding the closest reference point
-   Optimizing search algorithms

## How It Works 🔍

1. The function takes a list of integers and a target integer.
2. It calculates the absolute difference between each list element and the target number.
3. It finds the minimum difference.
4. If multiple numbers have the same difference, it selects the one with the smallest index.
5. If the list is empty, it returns `-1`.

## Output 📜

Example usage and expected outputs:

```python
index_of_nearest([4, 1, 88, 12], 10)
# 3 (12 is the closest to 10)

index_of_nearest([7, 13, 20, 25], 19)
# 2 (20 is the closest to 19)

index_of_nearest([5, 10, 15, 20], 12)
# 2 (10 and 15 are both 2 away, but 10 appears first)

index_of_nearest([], 5)
# -1 (empty list)
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Call the `index_of_nearest()` function in your script or interactive Python shell.

Example:

```python
from nearest_finder import index_of_nearest

print(index_of_nearest([3, 8, 15], 9))
```

## Conclusion 🚀

The `index_of_nearest()` function provides an efficient way to find the closest number in a list while handling edge cases like multiple nearest numbers and empty lists.
