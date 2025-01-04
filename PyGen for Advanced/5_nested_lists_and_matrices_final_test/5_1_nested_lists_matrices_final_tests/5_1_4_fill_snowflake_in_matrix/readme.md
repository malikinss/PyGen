# Snowflake Matrix Generator ❄️

## Description 📝

This Python program generates an `n x n` matrix filled with dots (`.`) and overlays a snowflake pattern using asterisks (`*`). The snowflake pattern consists of the main diagonal, secondary diagonal, middle row, and middle column filled with `*`. The program only accepts odd natural numbers for the matrix size.

## Purpose 🎯

-   Demonstrates matrix manipulation and pattern generation.
-   Enhances skills in working with nested loops and list comprehensions.
-   Provides a fun way to visualize patterns programmatically.

## How It Works 🔍

1. **Function `get_matrix_of_points()`**:

    - Creates an `n x n` matrix filled with `.`.

2. **Functions `fill_middle_column()` and `fill_middle_row()`**:

    - Fill the middle row and column of the matrix with `*`.

3. **Functions `fill_main_diagonal()` and `fill_secondary_diagonal()`**:

    - Fill the main and secondary diagonals with `*`.

4. **Function `fill_snowflake_in_matrix()`**:

    - Combines the above functions to apply the snowflake pattern to the matrix.

5. **Function `print_matrix()`**:

    - Prints the matrix row by row.

6. **Function `main()`**:
    - Prompts the user to input an odd natural number `n`.
    - If the number is even, an error message is displayed.
    - If the number is odd, the snowflake pattern is generated and printed.

## Usage 📦

1. Run the script `snowflake_matrix.py`.
2. Enter an odd natural number for the matrix size.
3. The program will output the matrix with the snowflake pattern.

### Example:

```
Enter an odd natural number: 5
```

**Output**:

```
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *
```

### Explanation:

-   The `5 x 5` matrix initially filled with dots (`.`) is updated to form a snowflake pattern using `*` along:
    -   The main diagonal (`\`)
    -   The secondary diagonal (`/`)
    -   The middle row and middle column

## Output 📜

-   A visual snowflake pattern in an `n x n` matrix.

## Conclusion 🚀

This program creatively demonstrates matrix manipulation by generating snowflake patterns. It's an excellent exercise in nested loops, matrix indexing, and condition-based pattern filling. A great addition to beginner or intermediate Python projects!
