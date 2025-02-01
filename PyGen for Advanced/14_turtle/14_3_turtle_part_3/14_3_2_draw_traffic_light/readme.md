# Traffic Light Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a simple traffic light consisting of a black rectangular body and three colored circles (representing the red, yellow, and green lights). The program defines a function to draw rectangles and dots, which are used to create the traffic light and its lights.

## Purpose 🎯

The goal of this program is to demonstrate basic Turtle graphics techniques, including drawing rectangles and circles, working with colors, and positioning shapes. It simulates a traffic light, which is a common visual used in many applications.

## How It Works 🔍

1. **Drawing Rectangles**:

    - The `draw_rectangle` function is used to draw a filled rectangle with a specified width, height, and starting position. It uses a loop to create the four sides of the rectangle.

2. **Drawing the Traffic Light**:

    - The `draw_traffic_light` function calls the `draw_rectangle` function to create the black body of the traffic light and uses `t.dot()` to draw three colored circles for the lights.

3. **Traffic Light Body**:

    - The body of the traffic light is a rectangle with dimensions 120x300 units, filled with black color.

4. **Traffic Light Colors**:

    - Three colored circles are drawn to represent the red, yellow, and green lights, each with a diameter of 80 units.

5. **Light Positioning**:
    - The lights are spaced vertically, starting from a Y-coordinate of 90 and adjusting by -90 units for each subsequent light.

## Output 📜

The output is a drawing of a traffic light consisting of a black rectangular body with three colored circles (red, yellow, and green) inside it. The drawing will be displayed in a Turtle graphics window.

### Example:

A window will appear with a simple traffic light illustration, consisting of a vertical black rectangle with red, yellow, and green circular lights.

## Usage 📦

1. Save the code in a file, e.g., `traffic_light.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python traffic_light.py`
5. The program will open a Turtle graphics window and draw the traffic light.

## Conclusion 🚀

This program demonstrates how to use basic Turtle graphics commands to create a simple illustration of a traffic light. It teaches essential concepts like drawing shapes, positioning, and filling with colors while creating a visually recognizable result.
