# Time Interval Converter

## Description 📝
This Python script converts a time interval given in minutes into a more readable format expressed in hours and minutes.
It outputs the original number of minutes along with the converted hours and remaining minutes.

## Purpose 🎯
The goal of this program is to demonstrate how to convert a time interval from minutes to hours and minutes.
This exercise helps with understanding integer division and modulus operations to format time intervals.

## How It Works 🔍
1. **`input()` Function**: Reads the total number of minutes from the user.
2. **Conversion Calculation**: 
   - **Hours Calculation**: Computes the number of hours by performing integer division (`//`) with 60.
   - **Minutes Calculation**: Computes the remaining minutes by taking the modulus (`%`) of the total minutes with 60.
3. **`print()` Function**: Outputs the original number of minutes along with the calculated hours and remaining minutes in the specified format.

## Output 📜
When the script is executed and the user inputs the number of minutes, the output will display:
`<original number of minutes> min is <total number of hours> hour <remaining number of minutes> minutes.`

For example, if the user inputs:
    `135`

The output will be:
    `135 min is 2 hour 15 minutes.`

## Usage 📦
1. Save the code to a file named `2_5_5_time_interval_converter.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
   `python 2_5_5_time_interval_converter.py`
5. Enter the number of minutes when prompted and press Enter.
6. The program will display the time interval converted into hours and minutes.

## Conclusion 🚀
This exercise provides a practical application of basic arithmetic operations to convert and format time intervals. 
It reinforces understanding of integer division and modulus operations.
Happy coding! 😊