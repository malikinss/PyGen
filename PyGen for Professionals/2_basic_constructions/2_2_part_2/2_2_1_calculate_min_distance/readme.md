# Calculate Minimum Distance Function

## Description 📝

The `calculate_min_distance()` function calculates the minimum distance Timur needs to walk to visit both stores and return home.
It minimizes the total distance by taking the shortest paths available between his house, the two shops, and the connecting path between the shops.

## Purpose 🎯

This function is useful for:

-   Calculating the minimal walking distance when visiting multiple locations and returning home.
-   Optimizing travel routes in scenarios with multiple possible paths.

## How It Works 🔍

1. The function receives three integer arguments:
    - `d1` (int): Distance from Timur's house to the first store.
    - `d2` (int): Distance from Timur's house to the second store.
    - `d3` (int): Distance between the two stores.
2. The function calculates the shortest path to each store and between them:
    - It checks the direct path to each store and the path between the stores, then selects the shortest option.
3. Finally, it adds up the distances for the minimum walk.

## Output 📜

Example usage and expected outputs:

```python
calculate_min_distance(3, 4, 2)
# Returns 9: 3 (home to store 1) + 2 (store 1 to store 2) + 4 (store 2 to home)

calculate_min_distance(5, 6, 1)
# Returns 12: 5 (home to store 1) + 1 (store 1 to store 2) + 6 (store 2 to home)
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the function in your script or interactive Python shell.

Example:

```python
from route_planner import calculate_min_distance

print(calculate_min_distance(5, 6, 1))  # Output: 12
```

## Conclusion 🚀

The `calculate_min_distance()` function optimizes Timur's walking route, ensuring the shortest total distance traveled when visiting both stores and returning home. It's ideal for planning efficient travel paths.
