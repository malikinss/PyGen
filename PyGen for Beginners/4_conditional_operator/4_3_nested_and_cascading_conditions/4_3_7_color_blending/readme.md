# Primary Color Blending

## Description 📝
This Python program reads the names of two primary colors and determines the resulting secondary color after blending them.
The program supports three primary colors: red, blue, and yellow.
It also handles cases where an invalid color is entered.

## Purpose 🎯
The purpose of this program is to simulate the blending of primary colors to form secondary colors.
The program ensures that only valid primary colors can be blended and provides the corresponding secondary color.

## How It Works 🔍
1. **User Input**:
   - The user is prompted to enter two primary colors from the options: `"red"`, `"blue"`, or `"yellow"`.
2. **Color Blending**:
   - The program checks the combination of primary colors:
     - **Red + Blue**: Produces **Purple**.
     - **Red + Yellow**: Produces **Orange**.
     - **Blue + Yellow**: Produces **Green**.
     - **Same Colors**: Produces the same primary color.
3. **Error Handling**:
   - If the user enters any color other than `"red"`, `"blue"`, or `"yellow"`, the program outputs `"color error"`.

## Output 📜
The program outputs either the resulting secondary color or an error message. Below are the possible combinations:
- **Red + Blue**: `purple`
- **Red + Yellow**: `orange`
- **Blue + Yellow**: `green`
- **Red + Red**: `red`
- **Blue + Blue**: `blue`
- **Yellow + Yellow**: `yellow`
- **Invalid Input**: `color error`

### Example:
For input: `red` `blue`
The output will be: `purple`

## Usage 📦
1. Save the code in a file named `4_3_7_color_blending.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_3_7_color_blending.py`
5. Enter two primary colors when prompted, and the program will display the result.

## Conclusion 🚀
This program provides a fun way to blend primary colors and see the resulting secondary colors.
It handles valid and invalid input efficiently, making it a great tool for beginners practicing conditionals and input validation in Python.
🎨✨