# Remove Extremes from List 📝

## Description 📝

This Python program removes the smallest and largest values from a list of natural numbers while maintaining the order of the remaining numbers. The user inputs a set of natural numbers, and the program outputs the list after removing the extreme values.

## Purpose 🎯

The program helps in scientific data analysis where removing outliers (smallest and largest values) can provide a more accurate representation of the data set, especially when extreme values might skew results.

## How It Works 🔍

1. The program first takes an integer `n` as input, representing the number of integers the user will provide.
2. Then, it reads `n` natural numbers from the user.
3. The program identifies the smallest and largest numbers in the list.
4. It removes both the smallest and largest values while preserving the order of the remaining numbers.
5. Finally, the program prints the updated list with each number on a separate line.

## Output 📜

```bash
Example Input:
Enter the number of integers: 5
Enter a number: 1
Enter a number: 3
Enter a number: 5
Enter a number: 2
Enter a number: 4

Example Output:
2
3
4
```

## Usage 📦

1. Save the script as `remove_extremes.py`.
2. Run the script in a Python environment.
3. Input the number `n`.
4. Input `n` different natural numbers.
5. The program will display the remaining numbers after removing the smallest and largest ones.

## Conclusion 🚀

This program demonstrates a simple yet effective way of removing the smallest and largest values from a data set, useful in various analytical contexts where such extremes might skew the results.
