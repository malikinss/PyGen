# Reverse Sequence Printer (Recursive)

## Description 📝

This program takes a sequence of integers, each entered on a separate line, and prints them in reverse order.
The sequence ends with the number `0`. The number `0` marks the end of the input but is also printed as part of the output.

The program uses recursion to reverse the sequence of numbers by reading inputs one by one and printing them once the recursion unwinds after encountering the number `0`.

## Purpose 🎯

The goal of this program is to demonstrate recursion in handling input and output.
It processes a sequence of integers and prints them in reverse order.
Recursion is utilized to delay printing until the base case (`0`) is encountered.

## How It Works 🔍

1. The program continuously reads integer inputs using `input()` and processes them.
2. It uses a helper function `_print_element_recursive()` to recursively read inputs until `0` is entered.
3. Once `0` is encountered, the recursion unwinds and the previously read integers are printed in reverse order.
4. Each number is printed in reverse as the recursion unwinds.

## Output 📜

For example, if the user enters the following sequence of integers:

```
1
2
3
4
0
```

The output will be:

```
4
3
2
1
0
```

## Usage 📦

1. Call the `reverse_sequence()` function, which will handle user input and print the sequence in reverse order.
2. The function will print the numbers in reverse after receiving the `0` that indicates the end of the sequence.

### Example:

```python
reverse_sequence()
```

**Output for input `1 2 3 4 0`:**

```
4
3
2
1
0
```

## Conclusion 🚀

This solution demonstrates the use of recursion to handle user input and print the sequence of numbers in reverse.
By recursively reading and printing each number, the program offers an elegant solution to reversing the sequence without needing to store the entire sequence in memory.
