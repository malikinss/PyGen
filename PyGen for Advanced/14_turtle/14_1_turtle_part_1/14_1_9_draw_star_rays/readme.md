# Drawing the Rays of a Star

## Description 📝

This Python program uses the Turtle graphics module to draw the rays of a star. The `draw_star_rays(length)` function creates the rays by drawing lines that extend outwards and then rotating to form a star pattern.

## Purpose 🎯

The purpose of this program is to illustrate how to draw a star with multiple rays using Turtle graphics. It demonstrates the concept of repeated line drawing and rotation to form a symmetrical pattern.

## How It Works 🔍

1. **Star Rays Drawing**:
    - The `draw_star_rays(length)` function draws one ray of the star, moves back to the starting point, and then rotates by 30 degrees to draw the next ray. This process repeats for 6 rays to complete the star.
2. **Rotation and Symmetry**:
    - The rotation of 30 degrees between each ray ensures that the rays are evenly spaced to form the star shape. Each ray is drawn with the given length, and the backward movement ensures that the turtle returns to the center before drawing the next ray.

## Output 📜

The program will display the rays of a star, with each ray having the specified length. The rays will be evenly spaced, creating a symmetric star-like shape.

### Example:

For the input:

```
length = 100
```

The output will be a star with rays, each having a length of 100 pixels.

## Usage 📦

1. Save the code in a file, e.g., `star_rays.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python star_rays.py`
5. The program will open a Turtle graphics window and draw the rays of the star.

## Conclusion 🚀

This program demonstrates how to use Turtle graphics to draw a star with symmetrical rays. It provides a simple approach to creating geometric patterns with repeated line drawing and rotation.
