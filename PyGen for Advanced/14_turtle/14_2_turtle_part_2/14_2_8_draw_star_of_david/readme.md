# Drawing the Star of David

## Description 📝

This Python program uses the Turtle graphics module to draw a Star of David. The star is made from two overlapping equilateral triangles. The pen is lifted and moved to the correct position between drawing the two triangles, as they cannot be drawn as a continuous line.

## Purpose 🎯

The purpose of this program is to demonstrate how to draw a geometric shape (the Star of David) using Turtle graphics. It showcases the process of drawing two triangles, one rotated to form a star shape.

## How It Works 🔍

1. **First Triangle**:

    - The turtle begins by drawing the first equilateral triangle.
    - The turtle moves forward by the given `size` for each side of the triangle and turns 120 degrees to form the corners.

2. **Second Triangle**:

    - After completing the first triangle, the pen is lifted to move the turtle to the starting position of the second triangle.
    - The second triangle is drawn in the same manner as the first triangle but rotated by 120 degrees in the opposite direction.
    - The result is two overlapping triangles that form the Star of David.

3. **Final Shape**:
    - The final result is a Star of David, consisting of two overlapping equilateral triangles.

## Output 📜

The program will display the Star of David, which is created by drawing two equilateral triangles that intersect and form a six-pointed star.

### Example:

For the input:

```
Size: 100
```

The output will be a Star of David with each triangle side being 100 units long.

## Usage 📦

1. Save the code in a file, e.g., `star_of_david.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python star_of_david.py`
5. The program will open a Turtle graphics window and draw the Star of David.

## Conclusion 🚀

This program demonstrates how to use Turtle graphics to draw geometric shapes. By drawing two equilateral triangles with careful positioning and rotation, the Star of David is formed. You can experiment with different sizes to change the appearance of the star.
