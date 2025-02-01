# Solar System Drawing Program

## Description 📝

This Python program uses the Turtle graphics library to draw a simplified version of the Solar System. It includes the Sun, planets, and an elliptical orbit around the Sun. The planets are scaled down based on their real sizes, and their names are displayed along with them. Additionally, stars are randomly placed in the background to simulate space.

## Purpose 🎯

The purpose of this program is to visualize the Solar System using Turtle graphics. It demonstrates how to draw planets, elliptical orbits, and a starry background. The program also shows how to scale objects and position them dynamically based on the size of the planets.

## How It Works 🔍

1. **Setting Up the Screen**:

    - The screen is configured with a black background to simulate space, and the Turtle graphics window is set to a width of 1000px and a height of 400px.

2. **Drawing Background Stars**:

    - A random field of stars is drawn using the `draw_starfield()` function. This function generates random positions and draws small white circles to represent stars in the background.

3. **Drawing Planets**:

    - The `draw_planets()` function iterates over the `PLANETS` list, which contains the name, size, and color of each planet. It places each planet in the solar system based on its size and position.

4. **Drawing the Elliptical Orbit**:

    - The program uses the `draw_ellipse()` function to create an elliptical orbit around the Sun, starting with the position of the first planet.

5. **Displaying Planet Names**:

    - Each planet's name is written next to the planet using the `turtle.write()` method, with appropriate font and alignment settings.

6. **Final Output**:
    - The program creates a graphical representation of the Solar System with planets, their orbits, and stars in the background. The result is displayed in the Turtle graphics window.

## Output 📜

The output is a graphical Solar System representation:

-   The Sun is at the center.
-   Each planet is drawn as a circle with its color and name.
-   A randomly generated field of stars in the background.
-   An elliptical orbit surrounding the planets.

### Example:

A graphical depiction of the Solar System:

-   **Sun** (yellow circle in the center).
-   **Planets** (drawn around the Sun with their respective colors and sizes).
-   **Stars** scattered throughout the background.

## Usage 📦

1. Save the code in a file, e.g., `solar_system.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python solar_system.py`
5. The program will open a Turtle graphics window displaying the Solar System.

## Conclusion 🚀

This program provides a basic but visually appealing representation of the Solar System. It demonstrates how to draw planets, elliptical orbits, and add a starry background using Turtle graphics. The program can be further expanded to include more details such as planetary moons or orbits with different characteristics.
