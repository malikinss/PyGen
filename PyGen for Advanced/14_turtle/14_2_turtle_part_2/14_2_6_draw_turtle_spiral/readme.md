# Drawing a Turtle Spiral

## Description 📝

This Python program uses the Turtle graphics module to draw a turtle-shaped spiral. The spiral is drawn with a series of steps that increase in length after each iteration. The turtle shape is stamped at each step of the spiral to create the effect of a "turtle spiral."

## Purpose 🎯

The goal of this program is to demonstrate how to create a spiral pattern using Turtle graphics, while experimenting with different step increments and turtle stamps to visualize the growth of the spiral.

## How It Works 🔍

1. **Initial Setup**:

    - The background color of the screen is set to `lawngreen` for contrast.
    - The turtle's shape is set to `'turtle'` and initially stamps at the center.

2. **Drawing the Spiral**:
    - A loop runs for the specified number of steps (`num_steps`), and in each iteration:
        - The turtle moves forward by a specified step length (`step_length`).
        - The turtle turns 90 degrees to the right to change direction.
        - The turtle stamps its shape at the new position to mark its place in the spiral.
        - After each stamp, the turtle rotates back and moves backward to prepare for the next segment.
        - The step length is incremented by the `step_increment` after each iteration to gradually increase the size of the spiral.
3. **Spiral Growth**:
    - With each step, the spiral grows in size, creating an outward spiral effect due to the increasing step lengths.

## Output 📜

The program will display a spiral shape with the turtle's stamp at each step. The turtle moves forward in increasing steps, turning and stamping to create the spiral pattern.

### Example:

For the input:

```
Initial Step Length: 10
Step Increment: 3
Number of Steps: 50
```

The output will be a turtle-shaped spiral that starts small and grows larger with each step.

## Usage 📦

1. Save the code in a file, e.g., `turtle_spiral.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python turtle_spiral.py`
5. The program will open a Turtle graphics window and draw the turtle spiral.

## Conclusion 🚀

This program demonstrates how to use Turtle graphics to create a spiral effect, using increasing step lengths and turtle stamps. You can experiment with different initial step lengths, increments, and numbers of steps to create various spiral patterns.
