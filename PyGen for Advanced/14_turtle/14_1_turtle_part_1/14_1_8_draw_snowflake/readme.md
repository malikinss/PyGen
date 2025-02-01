# Drawing a Snowflake Made of Diamonds

## Description 📝

This Python program uses the Turtle graphics module to draw a snowflake composed of 10 diamond-shaped figures (rhombuses). The `draw_snowflake(diamonds, side)` function creates the snowflake by arranging multiple diamonds in a circular pattern.

## Purpose 🎯

The purpose of this program is to illustrate how to draw a snowflake pattern using the Turtle graphics library. It demonstrates the concept of arranging multiple shapes (diamonds) in a circular formation to create a complex figure.

## How It Works 🔍

1. **Diamond Drawing**:
    - The `draw_rhombus(side)` function draws a diamond shape (rhombus) with the given side length. It uses turns of 60 and 120 degrees to create the rhombus shape.
2. **Snowflake Formation**:
    - The `draw_snowflake(diamonds, side)` function calls `draw_rhombus(side)` multiple times to draw a series of diamonds. Each diamond is rotated by an angle of `360 / diamonds` to form a circular arrangement of diamonds.

## Output 📜

The program will display a snowflake composed of 10 diamonds, with each diamond having the specified side length. The diamonds are evenly spaced in a circular pattern.

### Example:

For the input:

```
diamonds = 10
side = 100
```

The output will be a snowflake shape made up of 10 diamonds, each with a side length of 100 pixels.

## Usage 📦

1. Save the code in a file, e.g., `snowflake.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python snowflake.py`
5. The program will open a Turtle graphics window and draw the snowflake.

## Conclusion 🚀

This program demonstrates how to use Turtle graphics to create a snowflake pattern composed of diamonds. It showcases geometric drawing techniques, including rotation and repetitive patterns.
