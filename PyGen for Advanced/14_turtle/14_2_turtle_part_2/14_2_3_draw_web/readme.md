# Drawing a Web with Rays

## Description 📝

This Python program uses the Turtle graphics module to draw a web with a specified number of rays. The function `draw_web(num_rays, radius)` creates a web where each ray is drawn from the center, and the number of rays is defined by the user. A dot is placed at the end of each ray and at the center of the web.

## Purpose 🎯

The purpose of this program is to create a simple web-like structure using Turtle graphics. The number of rays (lines radiating from the center) can be specified, and the web will be drawn accordingly. The program demonstrates drawing shapes with multiple lines and adding dots as visual markers.

## How It Works 🔍

1. **Drawing Rays**:
    - The program draws a total of `num_rays` rays emanating from the center. Each ray is a line of the given `radius`.
    - After drawing each ray, a dot is stamped at the end to represent the ray's tip.
2. **Rotation and Centering**:
    - After drawing a ray, the turtle rotates by an angle of `360 / num_rays` to position itself for the next ray.
3. **Dot at the Center**:
    - After all the rays are drawn, a larger dot is placed at the center of the web to mark the origin.

## Output 📜

The program will display a web with a central dot and `num_rays` rays radiating from the center. Each ray has a dot at the end, and the rays are evenly spaced, based on the number of rays entered.

### Example:

For the input:

```
Enter the number of rays: 8
```

The output will be a web with 8 rays, each with a dot at its tip and a larger central dot.

## Usage 📦

1. Save the code in a file, e.g., `web_with_rays.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python web_with_rays.py`
5. Enter the number of rays when prompted.
6. The program will open a Turtle graphics window and draw the web with the specified number of rays.

## Conclusion 🚀

This program demonstrates the creation of a web-like pattern using Turtle graphics, with the flexibility to change the number of rays and the radius of the web. You can experiment with different values to create unique web patterns.
