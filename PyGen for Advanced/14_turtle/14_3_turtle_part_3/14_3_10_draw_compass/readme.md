# Compass Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a simple compass with four main directions: North, South, East, and West. The compass is represented by a circle with directional labels written in both Russian and English. The program demonstrates how to draw a circle, position labels, and use turtle graphics for basic visual representation.

## Purpose 🎯

The purpose of this program is to show how to use Turtle graphics to draw a compass with labeled directions. It provides an example of using Turtle to draw shapes (a circle) and display text labels (for the cardinal directions). This program can be extended to create more complex navigational tools or to explore geometric drawing.

## How It Works 🔍

1. **Drawing the Compass Circle**:

    - A circle is drawn to represent the outer boundary of the compass. The radius of the circle is adjustable by passing different values to the `draw_circle` function.

2. **Positioning the Directions**:
    - The four cardinal directions ('Восток', 'Север', 'Запад', 'Юг') are drawn at fixed positions along the compass circle. Each direction is drawn relative to the center of the compass circle, and its label is placed using the `turtle.write()` method.
3. **Directional Labeling**:

    - Each direction is placed using a relative movement from the center. The labels are aligned using the specified alignment options (`'left'`, `'center'`, `'right'`), and the font style is defined.

4. **Drawing the Compass**:
    - The compass is drawn by first creating the circle, then placing each directional label correctly. The Turtle graphics window will display the compass after running the program.

## Output 📜

The output is a graphical compass drawn in the Turtle graphics window. The compass consists of a circle with directional labels (East, North, West, South) placed around it.

### Example:

A graphical compass showing the four main directions:

-   East (Восток)
-   North (Север)
-   West (Запад)
-   South (Юг)

## Usage 📦

1. Save the code in a file, e.g., `compass.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python compass.py`
5. The program will open a Turtle graphics window displaying the compass.

## Conclusion 🚀

This program demonstrates the basics of using Turtle graphics to draw geometric shapes and display text. It shows how to draw a circle and add directional labels at specific points on the circle. This program can be expanded to include more complex graphical elements, such as additional markers or a more detailed compass.
