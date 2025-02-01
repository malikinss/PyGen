# Animated Moon Phases Program

## Description 📝

This Python program uses the Turtle graphics library to animate the phases of the moon. The moon goes through two primary phases: waxing and waning. A shadow is animated over the moon to simulate the movement of the shadow, giving the effect of changing phases.

## Purpose 🎯

The purpose of this program is to visually simulate the moon's phases using Turtle graphics. It demonstrates how to animate the moon phases by moving a shadow over a circular shape, simulating the waxing and waning of the moon.

## How It Works 🔍

1. **Setting Up the Screen**:

    - The screen is set up with a `DarkBlue` background to simulate the night sky. The window dimensions are 600x600 pixels.

2. **Creating the Moon**:

    - The moon is represented by an orange circle, which is centered on the screen. Its size is 200 units.

3. **Creating the Shadow**:

    - A shadow, represented by a circle with the color `DarkBlue`, is created. This shadow will move across the moon to simulate the changing phases.

4. **Animating the Phases**:

    - The moon goes through two phases:
        - **Waxing Phase**: The shadow moves from left to right, gradually covering the moon.
        - **Waning Phase**: The shadow moves from right to left, gradually uncovering the moon.
    - The movement is achieved by updating the position of the shadow turtle in small increments and refreshing the screen to display the changes.

5. **Animation Loop**:
    - The program continuously loops through the waxing and waning phases, creating a seamless animation of the moon's phases.

## Output 📜

The output is an animated representation of the moon going through its phases. The moon starts with a fully illuminated appearance and gradually changes as the shadow moves across it.

### Example:

A Turtle graphics window will appear, showing the moon with an animated shadow passing across it, creating the effect of waxing and waning moon phases.

## Usage 📦

1. Save the code in a file, e.g., `moon_phases.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python moon_phases.py`
5. The program will open a Turtle graphics window and animate the moon phases.

## Conclusion 🚀

This program demonstrates how to use basic animation techniques in Turtle graphics to simulate the phases of the moon. It's an interactive and visually appealing way to understand the moon's cycle.
