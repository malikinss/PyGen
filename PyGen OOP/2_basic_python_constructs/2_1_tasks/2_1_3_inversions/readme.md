# Inversion Counter 🔄

## Description 📝

This program counts the number of **inversions** in a sequence of numbers.
An inversion is a pair `(aᵢ, aⱼ)` where `i < j` and `aᵢ > aⱼ`.
Inversions indicate disorder in the sequence, which can be useful in sorting algorithms and data analysis.

## Purpose 🎯

The purpose of this program is to efficiently determine how "out of order" a sequence is by counting the number of inversions using a **modified merge sort** approach.

## How It Works 🔍

1. **Input**:

    - The program receives a sequence of numbers as input.

2. **Processing**:

    - It uses a **divide-and-conquer strategy** (Merge Sort) to count inversions efficiently.
    - The algorithm:
        1. **Splits** the sequence into halves recursively.
        2. **Counts** inversions in each half.
        3. **Merges** the halves back while counting **cross inversions**.

3. **Output**:
    - The program outputs the total number of inversions in the sequence.

## Output 📜

### Example Input:

```sh
3 1 4 2
```

### Example Output:

```sh
3
```

(There are three inversions: `(3,1)`, `(3,2)`, and `(4,2)`)

## Usage 📦

1. Run the script:
    ```sh
    python inversion_counter.py
    ```
2. Enter a sequence of space-separated numbers.
3. The output will be the number of inversions.

## Complexity Analysis ⏳

-   **Naïve Approach**: `O(n²)` using a brute-force comparison of all pairs.
-   **Merge Sort Approach**: `O(n log n)`, significantly more efficient for large datasets.

## Conclusion 🚀

This program provides an optimized way to count inversions using **Merge Sort**, making it ideal for large datasets where a brute-force approach would be too slow.
