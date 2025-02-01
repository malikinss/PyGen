# Heart Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a filled heart shape based on a parametric equation. The heart is drawn by calculating the coordinates using the equation:

-   \(x = 128 \sin(t)^3\)
-   \(y = 8 (13 \cos(t) - 5 \cos(2t) - 2 \cos(3t) - \cos(4t) - 5)\)
    where \( t \) ranges from \( 0 \) to \( 2\pi \).

Additionally, the program draws an arrow at the bottom of the heart using simple turtle commands.

## Purpose 🎯

The purpose of this program is to demonstrate how to use parametric equations for drawing shapes with the Turtle graphics library. It showcases the drawing of a heart shape, allowing the user to see the transformation of mathematical equations into a visual representation.

## How It Works 🔍

1. **Parametric Equation**:
    - The program uses parametric equations to define the coordinates for drawing the heart. For each value of \( t \) in the range \( [0, 2\pi] \), the `calculate_heart_coordinates()` function computes the corresponding \(x\) and \(y\) values.
2. **Drawing the Heart**:

    - The heart shape is drawn in red using the `draw_heart()` function, which uses the parametric coordinates to position the turtle at the right spots and create a filled heart shape.

3. **Arrow Drawing**:

    - The `draw_arrow()` function creates an arrow shape at the bottom of the heart. The arrow is drawn using turtle commands, and its shape is modified for visual effect.

4. **Turtle Graphics**:
    - Turtle graphics are used to render both the heart and the arrow. The `setup_turtle()` function configures the turtle with specific pen sizes and colors.

## Output 📜

The output consists of a graphical representation of a red heart shape created using a parametric equation and an arrow positioned below the heart.

### Example:

-   **Heart**: A filled red heart shape drawn using the parametric equation.
-   **Arrow**: An arrow pointing upwards, placed below the heart.

## Usage 📦

1. Save the code in a file, e.g., `heart_shape.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python heart_shape.py`
5. The program will open a Turtle graphics window displaying the heart shape with the arrow.

## Conclusion 🚀

This program showcases how to use parametric equations to create a visually appealing shape (heart) using the Turtle graphics library. It also demonstrates how to work with simple turtle commands to create an arrow shape. The program can be further enhanced by adding animations or other graphical elements.
