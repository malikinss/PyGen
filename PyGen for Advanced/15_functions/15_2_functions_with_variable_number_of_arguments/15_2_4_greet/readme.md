# greet() Function

## Description

The `greet()` function generates a greeting message for one or more names. It takes at least one mandatory name and can accept additional names, returning a personalized greeting for all.

## Purpose

This function creates a customized greeting message based on the names provided, accommodating an arbitrary number of names.

## How It Works

-   The function takes a mandatory first name and any number of additional names.
-   It constructs a greeting string, listing the names separated by "and", and formats it as "Hello, name1 and name2 and ...!"

## Usage

Example calls:

```python
print(greet('Timur'))             # Output: "Hello, Timur!"
print(greet('Timur', 'Roman'))    # Output: "Hello, Timur and Roman!"
print(greet('Timur', 'Roman', 'Ruslan'))  # Output: "Hello, Timur and Roman and Ruslan!"
```

## Conclusion

The `greet()` function offers a flexible way to greet multiple people by taking any number of name arguments and returning a formatted message.
