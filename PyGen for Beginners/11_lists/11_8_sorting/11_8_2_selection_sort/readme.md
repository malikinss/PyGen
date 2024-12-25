# Selection Sort Algorithm

## Description 📝

This Python program implements the **selection sort** algorithm to sort a list of integers in ascending order.
Selection sort repeatedly selects the smallest element from the unsorted portion of the list and moves it to the sorted section.

## Purpose 🎯

The program aims to:

-   Illustrate the workings of the selection sort algorithm.
-   Sort a list of integers in ascending order through step-by-step comparisons and swaps.
-   Provide a simple, easy-to-understand sorting algorithm useful for learning basic sorting techniques.

## How It Works 🔍

1. **Initialization**: The program accepts a list of integers.
2. **Outer Loop**: Iterates over each element in the list.
3. **Inner Loop**: Finds the smallest element from the unsorted portion of the list.
4. **Swapping**: The smallest element found is swapped with the element at the current position of the outer loop.
5. **Completion**: The process repeats until the entire list is sorted.

### Key Points:

-   Selection sort has a time complexity of \(O(n^2)\).
-   It is not the most efficient sorting algorithm for large datasets but is simple and easy to implement.

## Output 📜

The program prints the sorted list in ascending order.  
**Example Output:**

```
[-97, -96, -94, -94, -79, -77, -72, -72, -71, -71, -67, -67, -64, -64, -63, -62, -62, -61, -60, -58, -56, -52, -48, -47, -42, -41, -39, -36, -32, -31, -30, -26, -24, -23, -22, -21, -19, -16, -16, -14, -10, -8, -5, -3, -1, 0, 2, 2, 3, 3, 5, 9, 9, 14, 20, 22, 27, 32, 32, 35, 35, 39, 39, 41, 41, 43, 48, 53, 57, 57, 58, 59, 59, 59, 60, 60, 61, 62, 63, 63, 64, 66, 71, 72, 76, 78, 78, 80, 82, 84, 87, 87, 89, 90, 92, 92, 93, 94, 96, 98]
```

## Usage 📦

1. Copy the code to a file named `selection_sort.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:  
   `python selection_sort.py`
5. The sorted list will appear in the terminal.

## Conclusion 🚀

The selection sort algorithm is a great introductory sorting technique for beginners in programming.
Although not the fastest for large datasets, it provides a foundational understanding of how sorting algorithms operate.
This project demonstrates how simple yet effective algorithms can solve basic computational problems. 🌟
