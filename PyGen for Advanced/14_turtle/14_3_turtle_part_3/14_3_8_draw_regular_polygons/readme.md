# Regular Polygons with Same Area Program

## Description 📝

This Python program uses the Turtle graphics library to draw a grid of regular polygons (triangle, square, pentagon, hexagon, and heptagon) with the same area. Each polygon is filled with a random color, and their side lengths are calculated to ensure that the area of all polygons is equal, using a mathematical formula for the area of a regular polygon.

## Purpose 🎯

The purpose of this program is to demonstrate how to calculate the side lengths of regular polygons with varying numbers of sides to achieve the same area. It also showcases how to use the Turtle graphics library to draw shapes and apply random colors.

## How It Works 🔍

1. **Setting Up the Turtle**:
    - The turtle is set to the fastest drawing speed, and its visibility is turned off to optimize drawing speed.
2. **Calculating Side Length**:

    - The area \( S \) of a regular polygon with \( n \) sides and side length \( a \) is given by:
      \[
      S = \frac{n \cdot a^2}{4 \cdot \tan\left(\frac{180^\circ}{n}\right)}
      \]
        - The side length \( a \) is calculated to achieve a target area (e.g., 200 square units) for each polygon.

3. **Grid and Positioning**:

    - The program calculates the appropriate grid size to fit the polygons and ensures they are placed in a grid format, with each polygon spaced evenly.

4. **Drawing the Polygons**:

    - The program draws polygons with 3 to 7 sides, each with a calculated side length to ensure they all have the same area. The polygons are randomly colored and drawn in a grid layout.

5. **Randomization**:

    - The colors of the polygons are randomly generated using RGB values.

6. **Final Output**:
    - The output is a grid of regular polygons, each with the same area, drawn on the Turtle graphics window.

## Output 📜

The output is a visual representation of a grid of polygons, with each polygon having the same area but varying numbers of sides (from 3 to 7). Each polygon is filled with a random color.

### Example:

The Turtle graphics window will show a grid of polygons (triangles, squares, pentagons, hexagons, and heptagons) of the same area, each filled with a different random color.

## Usage 📦

1. Save the code in a file, e.g., `regular_polygons.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python regular_polygons.py`
5. The program will open a Turtle graphics window displaying the grid of polygons.

## Conclusion 🚀

This program demonstrates how to use mathematical formulas to create visually appealing shapes while maintaining consistent areas. It is a great example of how to combine geometry and randomization in programming to produce creative results using the Turtle graphics library.
