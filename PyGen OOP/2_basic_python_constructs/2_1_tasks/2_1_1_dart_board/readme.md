# Darts Field Generator 🎯

## Description 📝

This program generates a **dartboard field** represented by a square matrix.
The field's values are arranged in **ascending order** from the edges of the board to the center.
The program calculates and arranges these values based on the **minimum distance** from each cell to the nearest edge.

## Purpose 🎯

The purpose of this program is to simulate the creation of a dartboard matrix where the values reflect increasing numbers as they move from the edges of the field toward the center.

## How It Works 🔍

1. **Input**:

    - The program takes a single integer representing the **side length** of the square matrix (dartboard).

2. **Matrix Creation**:

    - It calculates the minimum distance from each cell to the nearest edge of the matrix.
    - The matrix is filled with values where the value in each cell represents the distance from that cell to the nearest edge plus one.

3. **Display**:
    - The dartboard matrix is printed row by row.

## Output 📜

### Example Input:

```sh
5
```

### Example Output:

```sh
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
```

## Usage 📦

1. Run the script:
    ```sh
    python darts_field.py
    ```
2. Input the side of the dartboard matrix (e.g., `5`).
3. The output will display the dartboard matrix, where the values represent the distance from the edges to the center.

## Conclusion 🚀

This program efficiently generates and displays a dartboard matrix with values arranged according to the distance from the edges to the center, providing an interesting pattern useful for simulations or visualizations related to darts or similar games.
