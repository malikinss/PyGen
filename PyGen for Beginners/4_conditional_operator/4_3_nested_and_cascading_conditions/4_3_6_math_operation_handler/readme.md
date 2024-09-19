# Mathematical Operation Handler

## Description 📝
This Python program performs basic mathematical operations (+, -, *, /) based on user input.
It takes two integers and a string representing an operation, then applies the chosen operation to the two integers.

## Purpose 🎯
The purpose of this program is to apply one of the four basic mathematical operations to two integers.
It also handles cases where invalid operations are input or division by zero is attempted.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to enter two integers.
   - The user is then asked to input a string representing a mathematical operation (`+`, `-`, `*`, `/`).
2. **Operation Execution**:
   - The program checks which operation was entered and performs the corresponding calculation:
     - **Addition (+)**: Adds the two numbers.
     - **Subtraction (-)**: Subtracts the second number from the first.
     - **Multiplication (*)**: Multiplies the two numbers.
     - **Division (/)**: Divides the first number by the second (with error handling for division by zero).
3. **Error Handling**:
   - If the operation is not one of the four valid operations, the program outputs `"Invalid operation"`.
   - If division by zero is attempted, the program outputs `"You can't divide by zero!"`.

## Output 📜
Depending on the input, the program will output the result of the operation or an error message:
- **Valid Operation**: Outputs the result of the calculation.
- **Invalid Operation**: Outputs `Invalid operation`.
- **Division by Zero**: Outputs `You can't divide by zero!`.

### Example:
For input: `10 5 +`
The output will be: `15`

## Usage 📦
1. Save the code in a file named `4_3_6_math_operation_handler.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_3_6_math_operation_handler.py`
5. Enter the two integers and the operation when prompted, and the program will display the result.

## Conclusion 🚀
This program provides a simple and efficient way to perform basic arithmetic operations and handle potential errors such as invalid input or division by zero.
It is a useful tool for beginners learning Python and practicing input validation.
✨