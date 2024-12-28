# Body Mass Index (BMI) Calculator ⚖️

## Description 📝

This Python program calculates a person's Body Mass Index (BMI) based on their weight and height, and classifies it into one of three categories: underweight, optimal weight, or overweight.
The BMI is a useful measure to estimate whether a person’s weight is in a healthy range relative to their height.

## Purpose 🎯

The program helps individuals assess their body weight in relation to their height, providing a simple and quick way to understand their health status based on BMI.

## How It Works 🔍

1. **Input Format**:
    - The user is asked to input their weight in kilograms and height in meters.
2. **Function Logic**:
    - The program calculates BMI using the formula:
      \[
      BMI = \frac{\text{weight}}{\text{height}^2}
      \]
    - The BMI value is then classified:
        - "Underweight" if BMI < 18.5
        - "Optimal weight" if 18.5 ≤ BMI ≤ 25
        - "Overweight" if BMI > 25
3. **Example**:

    ```
    Enter your weight (kg): 70
    Enter your height (m): 1.75
    Output:
    Optimal weight
    ```

4. **Edge Cases**:
    - Ensure both weight and height inputs are positive.
    - BMI classification is based on standard ranges, so ensure accuracy in the input to prevent misleading results.

## Usage 📦

1. Copy the code into a Python file, e.g., `bmi_calculator.py`.
2. Run the script in the terminal:
    ```bash
    python bmi_calculator.py
    ```
3. Enter your weight and height when prompted.
4. The program will output your BMI classification.

## Conclusion 🚀

This BMI calculator provides a straightforward method to evaluate weight relative to height.
By classifying BMI into three categories, it helps users understand if they need to adjust their lifestyle choices based on their health status.
