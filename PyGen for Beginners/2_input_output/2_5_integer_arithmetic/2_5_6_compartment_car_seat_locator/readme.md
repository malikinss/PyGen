# Compartment Car Seat Locator

## Description 📝
This Python script determines the compartment number in a compartment car where a given seat number is located.
Each compartment has four passenger seats, and the seat numbering starts from 1.

## Purpose 🎯
The goal of this program is to calculate the compartment number based on a given seat number in a car with a fixed seating arrangement.
This exercise demonstrates the use of integer division and modulo operations for categorizing continuous seat numbers.

## How It Works 🔍
1. **`input()` Function**: Reads the seat number from the user.
2. **Compartment Calculation**:
   - **Determine Compartment**: Calculates the compartment number by using integer division. Since each compartment has 4 seats, the formula `(seat_number - 1) // 4 + 1` is used to find the compartment number.
3. **`print()` Function**: Outputs the compartment number where the seat is located.

## Output 📜
When the script is executed and the user inputs a seat number, the output will display the compartment number.
For example, if the user inputs:
    `10`

The output will be:
    `3`
This means that seat number 10 is in compartment number 3.

## Usage 📦
1. Save the code to a file named `2_5_6_compartment_car_seat_locator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
   `python 2_5_6_compartment_car_seat_locator.py`
5. Enter the seat number when prompted and press Enter.
6. The program will display the compartment number where the seat is located.

## Conclusion 🚀
This exercise helps in understanding how to categorize sequential items into groups using integer arithmetic.
It reinforces the concept of grouping and indexing in a fixed arrangement.
Happy coding! 😊