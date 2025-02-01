# Drawing a Dotted Line

## Description 📝

This Python program uses the Turtle graphics module to draw a dotted line by placing dots at regular intervals. The function `draw_dotted_line(dot_distance, num_dots, dot_size)` draws a series of dots with customizable distance between them, number of dots, and size of each dot.

## Purpose 🎯

The purpose of this program is to demonstrate how to create a dotted line pattern using Turtle graphics. The program shows how to control the movement of the turtle and place dots at specific intervals to form a line.

## How It Works 🔍

1. **Turtle Setup**:
    - The program begins by lifting the pen using `turtle.penup()`, so the turtle can move without drawing a line.
2. **Drawing Dots**:

    - The turtle then moves forward by a specified distance (`dot_distance`), and places a dot using `turtle.dot(dot_size)` at each step.

3. **Movement and Dot Placement**:
    - The loop iterates `num_dots` times, drawing a dot and moving forward by the set distance after each one.

## Output 📜

The program will display a dotted line on the Turtle graphics window. The number of dots, the distance between them, and the size of each dot can be customized using the parameters.

### Example:

For the input:

```
dot_distance = 20
num_dots = 10
dot_size = 10
```

The output will be a dotted line consisting of 10 dots, each spaced 20 pixels apart, and each dot having a size of 10 pixels.

## Usage 📦

1. Save the code in a file, e.g., `dotted_line.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python dotted_line.py`
5. The program will open a Turtle graphics window and draw the dotted line.

## Conclusion 🚀

This program demonstrates how to create simple graphical patterns using Turtle graphics. By adjusting the distance, number of dots, and dot size, you can customize the dotted line to your liking.
