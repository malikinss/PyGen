# List Division into Sublists Program 📋

## Description 📝

This Python program divides a list of elements into nested sublists, ensuring that `n` consecutive elements belong to different sublists. It efficiently rearranges elements to avoid consecutive grouping, distributing them in a round-robin manner.

## Purpose 🎯

-   Divide a list of elements (e.g., characters or words) into `n` sublists.
-   Ensure balanced distribution by placing consecutive elements in different sublists.
-   Useful for distributing tasks, balancing workloads, or partitioning data for parallel processing.

## How It Works 🔍

1. **Function `divide_list_into_sublists()`**:

    - Accepts a list of elements and the desired number of sublists `n`.
    - Initializes `n` empty sublists.
    - Distributes elements across sublists in a round-robin pattern:
        - The first element goes to the first sublist, the second to the second sublist, and so on.
        - After reaching the last sublist, distribution loops back to the first.

2. **Function `main()`**:
    - Takes user input (list of elements and number of sublists).
    - Calls the function to divide the list and prints the resulting nested sublists.

## Usage 📦

1. Run the Python script `list_divider.py`.
2. Enter a list of space-separated elements.
3. Specify the number of sublists to divide the list into.
4. The program prints the nested sublists.

### Example:

```
Enter a list of elements (space-separated): a b c d e f g h
Enter the number of sublists: 3
[['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f']]
```

### How the Example Works:

-   The list `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']` is divided into 3 sublists:
    -   1st sublist: `['a', 'd', 'g']` (1st, 4th, 7th elements)
    -   2nd sublist: `['b', 'e', 'h']` (2nd, 5th, 8th elements)
    -   3rd sublist: `['c', 'f']` (3rd, 6th elements)

## Output 📜

-   The result is a nested list, where each sublist contains non-consecutive elements.

## Conclusion 🚀

This program provides a simple and efficient solution to partition lists into sublists with non-consecutive distribution.
It highlights important programming concepts such as list comprehension, iteration, and modular arithmetic.
