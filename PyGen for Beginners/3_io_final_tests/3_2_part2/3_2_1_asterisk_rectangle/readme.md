# Asterisk Rectangle Perimeter

## Description 📝
This Python script prints a rectangle with asterisks (`*`) forming its perimeter.
The rectangle has fixed dimensions where the width is 17 characters and the height is 3 lines, with the interior of the rectangle being empty.

## Purpose 🎯
The purpose of this program is to illustrate how to use string multiplication and the `print()` function in Python to create shapes with characters.
This exercise helps in understanding basic string manipulation and output formatting.

## How It Works 🔍
1. **Top and Bottom Border**: 
   - The top and bottom of the rectangle are created by printing 17 asterisks (`*`), which is done using string multiplication: `'*' * 17`.
2. **Sides of the Rectangle**:
   - The sides are printed with an asterisk at the beginning and the end, leaving a 15-character gap in between, which represents the empty space inside the rectangle. This is done using the `sep` argument in the `print()` function to add the space between the two asterisks: `print('*', '*', sep=' ' * 15)`.
3. **Overall Structure**:
   - The rectangle has a height of three lines: one for the top border, two for the sides, and one for the bottom border.

## Output 📜
The script produces the following output:
    rectangle with its perimeter formed by asterisks and an empty interior.

## Usage 📦
1. Save the code to a file named `3_2_1_asterisk_rectangle.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 3_2_1_asterisk_rectangle.py`
5. The program will print a rectangle with asterisks forming the perimeter as described.

## Conclusion 🚀
This exercise provides a simple introduction to working with strings, the `print()` function, and basic formatting in Python.
It's a great way to understand how to manipulate output to create shapes and patterns.
Happy coding! 😊