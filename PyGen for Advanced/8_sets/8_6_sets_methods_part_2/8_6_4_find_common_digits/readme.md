# Common Digits Finder Program 📝

## Description 📝

This program takes a sequence of natural numbers as input and determines the common digits that appear in all the input numbers.
The digits are then output in ascending order.

## Purpose 🎯

The program is useful for identifying shared digits across a series of numbers, which can be applied in scenarios like data matching or pattern recognition.

## How It Works 🔍

1. **Input**:
    - The program first reads an integer `n`, which represents the number of natural numbers that will follow.
    - It then reads `n` numbers, each on a separate line.
2. **Logic**:
    - The program starts with the digits of the first number and iterates through the rest of the numbers.
    - For each number, it performs an intersection operation to retain only those digits that are common between the current set of digits and the digits of the number being processed.
3. **Output**:
    - The program outputs all the common digits in ascending order.

### Example:

**Input**:

```
3
123
345
567
```

**Output**:

```
3
```

-   In this example, the common digit across all three numbers is 3, so it is printed in ascending order.

## Output 📜

-   The program outputs the common digits between all the input numbers, sorted in ascending order.

## Usage 📦

1. Run the program.
2. Enter the total number of natural numbers (`n`).
3. Enter the `n` natural numbers, each on a separate line.
4. The program will print the common digits, sorted in ascending order.

## Conclusion 🚀

This program provides a method to identify and display common digits between multiple numbers, which can be useful for analyzing patterns or common features across datasets.
