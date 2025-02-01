# Drawing a Clock Face

## Description 📝

This Python program uses the Turtle graphics module to draw a clock face with a specified number of hour marks (ticks) around the edge. The function `draw_clock_face(num_marks)` draws the clock face with the desired number of marks and places a turtle stamp at each mark's position.

## Purpose 🎯

The goal of this program is to demonstrate how to draw a clock face with a given number of hour marks, using Turtle graphics. It also introduces the concepts of positioning and rotating the turtle to create circular patterns.

## How It Works 🔍

1. **Initial Setup**:
    - The turtle's pen is lifted, and its size is set to `3` to make the marks visible.
    - The turtle shape is set to `'turtle'` to use the stamp as an hour mark.
2. **Clock Face Drawing**:
    - A loop runs for the number of marks (`num_marks`), and for each iteration:
        - The turtle moves forward to position itself at the correct place for the tick.
        - The pen is lowered to draw the tick.
        - The pen is lifted, and the turtle moves forward again, stamping a turtle to mark the hour tick's position.
        - After the tick is placed, the turtle moves back to the center.
        - The turtle turns by an angle of `360 / num_marks` to position itself for the next tick.
3. **Center Stamp**:
    - After completing the loop, a final stamp is placed at the center of the clock face to represent the center of the clock.

## Output 📜

The program will display a window with a clock face, where the number of hour ticks is determined by the user input.

### Example:

For the input:

```
Enter the number of marks for the clock face: 12
```

The output will be a clock face with 12 ticks, arranged around the circle, representing the hours.

## Usage 📦

1. Save the code in a file, e.g., `clock_face.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python clock_face.py`
5. Enter the number of marks when prompted.
6. The program will open a Turtle graphics window and draw the clock face with the specified number of marks.

## Conclusion 🚀

This program demonstrates how to draw a clock face using Turtle graphics. You can experiment with different numbers of ticks to create clocks for various time intervals or design needs.
