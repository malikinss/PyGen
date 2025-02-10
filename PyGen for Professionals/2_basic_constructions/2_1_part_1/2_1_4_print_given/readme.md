# Print Arguments and Their Types

## Description 📝

This program implements the `print_given()` function, which accepts an arbitrary number of positional and named arguments.
It prints the value and type of each argument. Positional arguments are printed first, followed by named arguments sorted lexicographically by their variable names.

## Purpose 🎯

The purpose of this function is to display both the values and types of the arguments passed to it.
This is useful for debugging and understanding the types of data being passed around in a program.

## How It Works 🔍

1. The function accepts any number of positional (`*args`) and named (`**kwargs`) arguments.
2. It first prints all positional arguments, followed by their types.
3. Then, it prints all named arguments in lexicographic order of the variable names, along with their values and types.
4. If no arguments are passed, the function doesn't print anything.

## Output 📜

The function outputs the following:

-   For positional arguments:
    -   `<argument value> <argument type>`
-   For named arguments:
    -   `<variable name> <argument value> <argument type>`
-   If no arguments are passed, nothing is printed.

## Usage 📦

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Call the `print_given()` function with positional and/or named arguments to print their values and types.

Example:

```python
print_given(42, "Hello", True)
# Output:
# 42 <class 'int'>
# Hello <class 'str'>
# True <class 'bool'>

print_given(name="Alice", age=25)
# Output:
# age 25 <class 'int'>
# name Alice <class 'str'>
```

## Conclusion 🚀

The `print_given()` function provides an efficient way to output both the values and types of arguments passed to it.
This is particularly useful for debugging and gaining insight into the types of variables in a program.
