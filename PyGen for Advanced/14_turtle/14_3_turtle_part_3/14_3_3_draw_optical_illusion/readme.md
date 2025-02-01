# Optical Illusion Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw an optical illusion consisting of triangles and dots. It features an outer black equilateral triangle with an inner white shape containing black dots. The combination of these shapes creates an optical illusion effect.

## Purpose 🎯

The purpose of this program is to demonstrate how simple geometric shapes can be arranged to create an optical illusion. It also serves as an exercise in drawing equilateral triangles and using different colors in Turtle graphics.

## How It Works 🔍

1. **Drawing the Outer Triangle**:

    - The `draw_triangle` function is used to draw an equilateral triangle with a given side length and color. It repeats the forward movement and turns to create the triangle shape.

2. **Optical Illusion Creation**:

    - The `draw_optical_illusion` function first draws a large black triangle.
    - Then, it moves to a new position and draws a smaller white triangle inside the first one.
    - Within the smaller triangle, black dots are drawn at each corner, contributing to the illusion.

3. **Color and Positioning**:
    - The outer triangle is black, while the inner triangle is white.
    - Black dots are placed at the corners of the inner triangle to enhance the illusion.

## Output 📜

The output is a drawing of an optical illusion consisting of a large black equilateral triangle with a smaller white triangle inside it. At the corners of the inner triangle, black dots create an illusionary effect.

### Example:

A Turtle graphics window will appear displaying an optical illusion created with black and white triangles and dots. The illusion gives the impression of a changing or shifting pattern, depending on the viewer's perception.

## Usage 📦

1. Save the code in a file, e.g., `optical_illusion.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python optical_illusion.py`
5. The program will open a Turtle graphics window and draw the optical illusion.

## Conclusion 🚀

This program demonstrates how geometric shapes and strategic positioning can create visually intriguing optical illusions. By using simple shapes like triangles and dots, the program showcases how perception can be manipulated through art.
