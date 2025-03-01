# Traffic Message Printer

## Description 📝

This program prints the message "Do not park" a specified number of times.
The function `traffic()` uses recursion to print the message. It stops when the count reaches zero.

## Purpose 🎯

The purpose of this function is to demonstrate how recursion can replace a while loop for repetitive tasks, such as printing a message multiple times.

## How It Works 🔍

1. The function takes an integer `n` as an argument.
2. It prints the message "Do not park" and then calls itself with the value of `n - 1` until `n` reaches 0.
3. Once `n` becomes 0, the recursion stops, and the function terminates.

## Output 📜

The function prints the message "Do not park" `n` times, where `n` is the number passed as an argument.

## Usage 📦

1. Call the `traffic(n)` function with the number of times you want the message to be printed.
2. The function will print "Do not park" the specified number of times.

### Example:

```python
traffic(3)
```

**Output:**

```
Do not park
Do not park
Do not park
```

## Conclusion 🚀

The recursive approach to printing the message demonstrates an alternative to using a `while` loop.
This solution also highlights the base case in recursion, where the function stops when `n` becomes 0.
