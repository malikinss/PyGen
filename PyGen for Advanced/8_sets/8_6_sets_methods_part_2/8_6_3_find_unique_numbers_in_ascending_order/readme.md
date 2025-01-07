# Unique Numbers in Ascending Order Program 📝

## Description 📝

This program takes two lines of text as input, each containing a sequence of numbers.
It determines and outputs all the numbers that are in the first sequence but not in the second sequence, sorted in ascending order.

## Purpose 🎯

The program helps identify numbers that are unique to the first sequence by comparing it against the second sequence.
It then outputs these numbers in ascending order, making it useful for tasks like set differences or finding exclusive data points.

## How It Works 🔍

1. **Input**:
    - The program first reads two lines of input, each containing a space-separated list of numbers.
2. **Logic**:
    - Both lines are converted into sets of integers.
    - The program calculates the difference between the two sets (i.e., numbers that are in the first set but not in the second).
    - The result is then sorted in ascending order.
3. **Output**:
    - The program prints the numbers that are in the first sequence but not in the second, sorted in ascending order.

### Example:

**Input**:

```
1 2 3 4 5
3 4 5 6 7
```

**Output**:

```
1 2
```

-   In this example, the numbers 1 and 2 appear in the first sequence but not in the second, and they are printed in ascending order.

## Output 📜

-   The program outputs all the numbers that are in the first sequence but not in the second, sorted in ascending order.

## Usage 📦

1. Run the program.
2. Enter the first sequence of numbers (space-separated).
3. Enter the second sequence of numbers (space-separated).
4. The program will print the numbers that are only in the first sequence, sorted in ascending order.

## Conclusion 🚀

This program provides a straightforward way to find and display numbers that are unique to the first sequence, making it useful for data comparison tasks where you need to highlight exclusive elements in one set over another.
