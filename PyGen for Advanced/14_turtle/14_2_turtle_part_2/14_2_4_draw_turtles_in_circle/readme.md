# Drawing Turtles in a Circular Pattern

## Description 📝

This Python program uses the Turtle graphics module to draw turtles arranged in a circular pattern. The function `draw_turtles_in_circle(num_turtles)` allows the user to specify how many turtles will be drawn. Each turtle is stamped on the screen in a circular arrangement.

## Purpose 🎯

The goal of this program is to demonstrate how to arrange multiple objects (in this case, turtles) in a circular pattern using Turtle graphics. This program also introduces the use of shapes and the `stamp()` function in Turtle.

## How It Works 🔍

1. **Initial Setup**:
    - The program sets up the turtle to stamp turtles on the screen. The turtle's shape is changed to `'turtle'` to make the stamps look like turtles.
2. **Turtle Stamping**:
    - Initially, a turtle is stamped at the center of the screen.
3. **Circular Arrangement**:
    - The program uses a loop to stamp additional turtles in a circular arrangement.
    - After each turtle is stamped, the turtle moves forward by a fixed distance, stamps, and then moves back to the center.
    - The turtle then turns by `360 / num_turtles` degrees to position itself for the next stamp.

## Output 📜

The program will display a window where the turtles are arranged in a circle. The number of turtles is based on the user input.

### Example:

For the input:

```
Enter the number of turtles: 8
```

The output will be a circular pattern with 8 turtles, each stamped at an equal distance from each other around the circle.

## Usage 📦

1. Save the code in a file, e.g., `turtles_in_circle.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python turtles_in_circle.py`
5. Enter the number of turtles when prompted.
6. The program will open a Turtle graphics window and draw the turtles in a circular pattern.

## Conclusion 🚀

This program demonstrates how to arrange objects in a circular pattern using Turtle graphics. You can experiment with different numbers of turtles to create various circular patterns.
