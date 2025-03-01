# Hourglass Shape with Recursion

## Description 📝

This program uses recursion to print an hourglass shape made up of the digits 1, 2, 3, and 4.
The hourglass consists of two halves: the top half with decreasing digits and the bottom half with increasing digits.
The number of digits in each row decreases from 16 to 4 and then increases back to 16.

## Purpose 🎯

The program demonstrates recursion by drawing a symmetrical hourglass shape with numbers.
The shape starts with 16 instances of the digit `1` and decreases by 4 digits at each level, eventually reaching `4`.
After that, it mirrors the top half to complete the hourglass shape.

## How It Works 🔍

1. The function `draw_hourglass` is called, which initializes the recursive process.
2. The `draw_layer` function is responsible for drawing individual layers of the hourglass by repeatedly decreasing the count of digits from 16 to 4.
3. The recursion happens in the `draw_layer` function, which prints the layer and calls itself with adjusted values until the base case is met.
4. The `display_layer` function centers each layer in a 16-character wide field to maintain the symmetrical shape.

## Output 📜

The program prints an hourglass shape as follows:

```
1111111111111111
 2222222222222
  33333333
   4444
  33333333
 2222222222222
1111111111111111
```

## Usage 📦

1. Copy the provided Python code into a `.py` file.
2. Run the script using a Python interpreter.
3. The hourglass shape will be printed on the console.

## Conclusion 🚀

This program is an excellent example of how recursion can be used to solve problems involving repeated patterns and symmetry.
It effectively demonstrates the power of recursion for managing iterative processes and printing complex shapes.
