# Function Min/Max on a Segment Program

## Description 📝

This Python script takes a valid mathematical function and a segment [a, b] as input and determines the minimum and maximum values of the function on that segment for integer points.
It evaluates the function at each integer in the range and prints the corresponding results.

## Purpose 🎯

The goal of this program is to demonstrate how to evaluate a mathematical function over a given segment and find its minimum and maximum values in a user-defined range.
It ensures that the function is properly evaluated at integer points within the segment.

## How It Works 🔍

1. **Input**:

    - The user inputs a mathematical function as a string (e.g., `x**2 - 4`).
    - The user inputs two integers `a` and `b`, representing the boundaries of the segment `[a; b]`.

2. **Evaluation**:

    - The program safely evaluates the function at each integer point in the range `[a; b]`.
    - It calculates the corresponding function values using Python's `eval()` function.

3. **Output**:

    - The program prints the minimum and maximum values of the function on the segment in the following format:
        - "The min value of the function <function> on the segment [a; b] is <min. value>"
        - "The max value of the function <function> on the segment [a; b] is <max. value>"

4. **Error Handling**:
    - The program catches and handles errors for invalid input, function evaluation errors, and segment boundary issues.

## Output 📜

### Input:

```
Enter the function: x**2 - 4
Enter the boundaries (a b): -3 3
```

### Output:

```
The min value of the function x**2 - 4 on the segment [-3; 3] is -4
The max value of the function x**2 - 4 on the segment [-3; 3] is 5
```

### Example with an Invalid Input:

```
Enter the function: x**2 - 4
Enter the boundaries (a b): 3 -3
```

### Output:

```
Invalid segment: 3 is greater than -3. Please ensure that the start is less than or equal to the end.
```

## Usage 📦

1. Save the code to a file named `min_max_function_segment.py`.
2. Open a terminal or command prompt.
3. Run the program:
    ```
    python min_max_function_segment.py
    ```
4. Enter a valid mathematical function (e.g., `x**2 - 4`).
5. Enter the segment boundaries (e.g., `-3 3`).
6. The program will output the minimum and maximum values of the function on the segment.

## Conclusion 🚀

This program demonstrates how to evaluate a mathematical function on a segment, determine its minimum and maximum values, and handle errors related to invalid input or function evaluation.
It is useful for applications requiring mathematical analysis over specific ranges.
