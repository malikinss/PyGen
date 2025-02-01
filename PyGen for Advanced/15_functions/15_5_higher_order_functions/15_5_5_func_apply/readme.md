# Function to Apply a Given Function to Each Item in a List

## Description

This program defines a function `func_apply()` that takes a function and a list of values as input and returns a new list where each value is the result of applying the passed function to the corresponding element in the list. It demonstrates the functionality with two example functions: adding 3 to each number and multiplying each number by 7.

## Purpose

The purpose of this program is to provide a reusable function that can apply any function to a list of numbers, allowing flexibility to modify or extend the behavior based on the passed function.

## How It Works

1. The `func_apply()` function iterates through each item in the list, applies the given function to the item, and collects the results in a new list.
2. Two example functions (`add3` and `mul7`) are defined to demonstrate the functionality of applying operations on numbers.

## Output

```
Add 3 to each number: [4, 5, 6, 7, 8]
Multiply each number by 7: [7, 14, 21, 28, 35]
```

## Conclusion

The `func_apply()` function successfully applies any given function to each element of a list, making it a flexible tool for transforming lists based on different operations. It is demonstrated here with addition and multiplication operations, but it can be extended to apply any function that takes and returns an integer.
