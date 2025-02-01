# Building Silhouette Program

## Description 📝

This Python program uses the Turtle graphics library to draw a cityscape with silhouettes of multi-story buildings, windows scattered in buildings, and stars in the night sky. The program draws several buildings in a random fashion, adds windows with a probability, and randomly scatters stars across the sky. The buildings are drawn in a simple silhouette style to simulate a city skyline at night.

## Purpose 🎯

The purpose of this program is to demonstrate how to use the Turtle graphics library to create a cityscape scene with multiple buildings, windows, and stars in the sky. It covers the use of randomness in graphical elements such as building heights, window placement, and star positions.

## How It Works 🔍

1. **Setup Screen**:

    - The `setup_screen()` function configures the Turtle graphics screen by setting its size and background color to represent the night sky.

2. **Create Turtle**:

    - The `create_turtle()` function creates and configures turtles with specified colors, speed, and visibility. Turtles are used for drawing buildings, windows, and stars.

3. **Draw Stars**:

    - The `draw_stars()` function randomly scatters stars (represented as dots) across the sky, ensuring they do not overlap with the buildings. The number of stars and their sizes are customizable.

4. **Draw Windows**:

    - The `draw_windows()` function places windows on buildings with a certain probability. The windows are drawn with random offsets to make the placement look more natural.

5. **Draw Buildings**:

    - The `draw_buildings()` function draws multiple buildings based on randomly generated heights and widths. Windows are added on these buildings according to the specified probability.

6. **Main Drawing Function**:

    - The `draw_scene()` function ties everything together: it initializes the screen, creates turtles, and calls the functions to draw stars, buildings, and windows.

7. **Random Elements**:
    - The randomness in this program is used for:
        - **Building shapes**: Random heights and roof placements.
        - **Windows**: Windows are placed with a given probability.
        - **Stars**: Stars are placed at random positions in the sky.

## Output 📜

The output is a graphical cityscape scene with:

-   **Night sky**: A dark blue background with randomly scattered stars.
-   **Buildings**: Randomly generated silhouettes of multi-story buildings with varying heights.
-   **Windows**: Random windows placed on the buildings with a probability of appearing.
-   **Stars**: Randomly placed stars that appear in the sky, not overlapping with the buildings.

### Example:

A graphical representation of the cityscape might look like:

-   **Buildings**: Dark blue silhouettes with varying heights.
-   **Windows**: Bright yellow windows scattered on buildings.
-   **Stars**: Small yellow dots scattered in the night sky.

## Usage 📦

1. Save the code in a file, e.g., `building_silhouette.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python building_silhouette.py`
5. The program will open a Turtle graphics window displaying the cityscape scene.

## Conclusion 🚀

This program demonstrates how to create a random cityscape with buildings, windows, and stars using the Turtle graphics library. It shows how to combine various graphical elements with randomness to create a dynamic scene. The program can be expanded to include more complex elements such as animated movement or interactive features.
