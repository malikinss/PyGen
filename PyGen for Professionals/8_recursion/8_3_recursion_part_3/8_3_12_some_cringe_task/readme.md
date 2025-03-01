# Recursive Subtraction and Addition Task 🌀

## Description 📝

The `some_cringe_task()` function uses recursion to subtract 5 from a given number `n` until it becomes non-positive, and then adds 5 back to the number as the recursion unwinds, returning to its original value.
The process includes printing the values during both the subtraction and addition phases.

## Purpose 🎯

The function demonstrates:

-   How recursion can be used for both subtracting and adding values in sequence.
-   How recursion can be effectively used to process numbers and track their values.
-   The concept of the "unwinding" phase of recursion, where operations are applied in reverse order.

## How It Works 🔍

1. **Input Parameters**:

    - `n`: A non-negative integer to process.
    - `original`: An optional parameter to store the original value of `n` for comparison during the addition phase.

2. **Base Case**:

    - When `n` becomes non-positive, the subtraction phase stops and the recursion begins to unwind.

3. **Recursive Flow**:

    - The function first subtracts 5 from `n` until it reaches 0 or below.
    - Once `n` is no longer positive, it starts adding 5 back to the number as the recursive calls return.

4. **Print Statements**:
    - Prints `n` during both the subtraction and addition phases.

For example, if the input is 16:

-   Subtract 5: 16, 11, 6, 1, -4
-   Then, add 5 during unwinding: 1, 6, 11, 16

## Output 📜

For example:

```python
some_cringe_task(16)
```

The function computes:

```
16
11
6
1
-4
1
6
11
16
```

**Output:**

```
16
11
6
1
-4
1
6
11
16
```

## Usage 📦

1. Call the function `some_cringe_task()` with:
    - A non-negative integer `n`.
2. Example:
    ```python
    some_cringe_task(16)  # Output: sequence of numbers during subtraction and addition phases
    ```
3. The function prints:
    - The sequence of numbers as it subtracts 5 and adds 5 recursively.

## Conclusion 🚀

The `some_cringe_task()` function offers a fun and recursive way to subtract and add numbers in sequence, providing a clear example of how recursion can be used for such tasks.
It's a good demonstration of recursion's flexibility for both decrementing and incrementing a value.
