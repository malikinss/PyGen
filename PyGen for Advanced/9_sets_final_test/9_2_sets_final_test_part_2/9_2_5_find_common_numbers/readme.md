# Common Numbers Finder 🤓

## Description 📝

Timur, a mathematician with a love for solving puzzles, tackles two challenging math problems daily. He writes down all the numbers from each problem and then checks for any common numbers between the two. If common numbers are found, the day is considered a success. If no common numbers exist, Timur concludes it was a "BAD DAY."

This program helps Timur automate the process by finding and displaying the common numbers between the two problems or reporting that no common numbers exist.

## Purpose 🎯

To identify and display the common numbers between two math problems solved by Timur or indicate the absence of common numbers.

## How It Works 🔍

1. **Inputs**:
    - A list of numbers from the first math problem.
    - A list of numbers from the second math problem.
2. **Logic**:
    - Find the intersection of the two sets of numbers.
    - If common numbers exist, sort them in descending order and display them.
    - If no common numbers exist, print `"BAD DAY"`.
3. **Outputs**:
    - The common numbers in descending order (if any).
    - `"BAD DAY"` if no common numbers are found.

## Output 📜

The program outputs:

-   Common numbers sorted in descending order.
-   `"BAD DAY"` if no common numbers are found.

### Example:

**Input**:

```
3 7 8 1 2
5 2 8 3
```

**Output**:

```
8 3 2
```

### Explanation:

-   Numbers from the first problem: `{3, 7, 8, 1, 2}`
-   Numbers from the second problem: `{5, 2, 8, 3}`
-   Common numbers: `{8, 3, 2}`, sorted in descending order.

## Usage 📦

1. Save the code in a Python file, e.g., `common_numbers_finder.py`.
2. Run the script.
3. Provide inputs:
    - First, a space-separated list of numbers from the first task.
    - Second, a space-separated list of numbers from the second task.
4. View the result:
    - Common numbers, sorted in descending order.
    - `"BAD DAY"` if no common numbers exist.

### Example Run:

```plaintext
Input:
10 20 30 40 50
15 25 35 45

Output:
BAD DAY
```

## Conclusion 🚀

This program is a simple yet effective way to find and display the common numbers between two lists. It's especially useful for tasks like comparing datasets, solving puzzles, or even for mathematicians like Timur who enjoy keeping their day successful!
