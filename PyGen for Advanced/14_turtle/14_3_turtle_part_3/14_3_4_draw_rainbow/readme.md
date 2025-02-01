# Rainbow Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a rainbow consisting of multiple colored arcs. Each arc represents a different color of the rainbow, and the arcs are drawn in sequence to form a full rainbow pattern.

## Purpose 🎯

The purpose of this program is to demonstrate the use of Turtle graphics to draw colorful patterns. By drawing multiple arcs with decreasing radii and different colors, it creates a visually appealing rainbow effect.

## How It Works 🔍

1. **Drawing the Rainbow Arcs**:

    - The program defines a function, `draw_rainbow_arc`, to draw a single arc of the rainbow with a given radius, color, and vertical offset.
    - The arc is drawn using a half-circle (180 degrees) with a specific radius and color.

2. **Generating the Rainbow**:

    - The `draw_rainbow` function calls `draw_rainbow_arc` multiple times with different colors and adjusted radii.
    - The radius decreases for each arc to create the layered effect of a rainbow.
    - The vertical offset increases to position each arc higher on the screen.

3. **Color Selection**:
    - The program uses a list of colors representing the rainbow (red, orange, yellow, green, blue, etc.), which are applied sequentially to the arcs.

## Output 📜

The output is a colorful rainbow with ten arcs, each representing a different color. The arcs are drawn with decreasing radii, resulting in a layered rainbow effect.

### Example:

A Turtle graphics window will appear displaying a rainbow consisting of ten arcs. Each arc is a different color, forming the shape of a rainbow with red at the top and pink at the bottom.

## Usage 📦

1. Save the code in a file, e.g., `rainbow.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python rainbow.py`
5. The program will open a Turtle graphics window and draw the rainbow.

## Conclusion 🚀

This program illustrates how Turtle graphics can be used to create colorful patterns, such as a rainbow, by using arcs and layering them with different colors. The result is a visually striking representation of a rainbow.
