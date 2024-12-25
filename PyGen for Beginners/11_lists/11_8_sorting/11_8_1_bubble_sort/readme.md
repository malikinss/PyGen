# Optimized Bubble Sort Algorithm

## Description 📝

This Python program implements an optimized version of the bubble sort algorithm to sort a list of integers in ascending order.
The optimization reduces unnecessary comparisons by keeping track of the last exchange position, minimizing redundant passes through the list.

## Purpose 🎯

The purpose of this program is to:

-   Demonstrate the implementation of an efficient bubble sort algorithm.
-   Highlight techniques to optimize sorting by reducing the number of comparisons and improving performance for nearly sorted arrays.

## How It Works 🔍

1. **Initial Setup**: The program accepts a list of integers as input.
2. **Outer Loop**: Iterates over the list \( n-1 \) times.
3. **Inner Loop**: Compares adjacent elements and swaps them if they are out of order.
4. **Optimization**:
    - A `swapped` flag detects if any swaps occurred during a pass. If no swaps occur, the list is already sorted, and the loop exits early.
    - `last_exchange` stores the index of the last swap. This reduces the size of the unsorted portion of the list for the next pass.
5. **Output**: The sorted list is returned and printed.

## Output 📜

The program outputs the sorted list in ascending order. For example:

```
[-97, -96, -95, -94, -91, -84, -84, -84, -83, -78, -78, -78, -76, -76, -75, -74, -74, -73, -71, -71, -71, -68, -68, -66, -65, -62, -61, -58, -56, -55, -55, -51, -47, -41, -40, -37, -32, -29, -27, -26, -26, -24, -20, -19, -17, -17, -16, -16, -13, -11, -9, -8, 0, 1, 7, 7, 11, 14, 16, 17, 17, 21, 21, 24, 25, 32, 36, 38, 38, 39, 44, 44, 47, 48, 50, 52, 56, 58, 63, 67, 69, 70, 75, 78, 79, 79, 88, 88, 88, 91, 92, 93, 93, 94, 96, 96, 97, 98]
```

## Usage 📦

1. Save the code in a file named `bubble_sort.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:  
   `python bubble_sort.py`
5. The sorted list will be printed in the terminal.

## Conclusion 🚀

This program efficiently sorts a list using an optimized bubble sort algorithm.
By reducing unnecessary comparisons, it enhances performance, making the algorithm suitable for partially sorted lists.
This project serves as a practical example of improving classical algorithms through simple optimizations. 🔄
