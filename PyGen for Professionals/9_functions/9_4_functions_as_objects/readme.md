# Lesson 9.4: Functions as Objects 🏗️

## Description 📝

This lesson explores **functions as objects** in Python, demonstrating that functions can have attributes and be manipulated just like any other object.
Python functions are first-class citizens, meaning they can be assigned to variables, passed as arguments, and modified dynamically.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand that **functions are objects** and can have attributes.  
✅ Learn how to access function attributes like **`__name__`**, **`__doc__`**, and **`__defaults__`**.  
✅ Modify function behavior dynamically by assigning attributes or overriding built-in functions.

## How It Works 🔍

This lesson covers the following concepts:

1. **Functions as First-Class Objects**: Functions can be stored in variables, passed as arguments, and manipulated like any other object.
2. **Function Attributes**: Functions have built-in attributes such as:
    - **`__name__`** – Stores the function’s name.
    - **`__doc__`** – Stores the function’s documentation string.
    - **`__defaults__`** – Stores default values for parameters.
3. **Adding Custom Attributes**: Functions can have their own attributes to store additional information, like counting calls or tracking results.

This lesson includes 4 programming tasks:

1.  **9_4_1_numbers_sum**  
    **Goal**: Implement `numbers_sum()`, a function that sums all numeric elements (integers and floats) from a list while ignoring non-numeric values.

-   This task demonstrates **type filtering** and working with **lists of mixed data types**.

2.  **9_4_2_print**  
    **Goal**: Override the built-in `print()` function to convert all string arguments, as well as `sep` and `end`, to uppercase before printing.

-   This task illustrates **function overriding** and how to **wrap built-in functions** to modify behavior.

3.  **9_4_3_polynom**  
    **Goal**: Define a function `polynom(x)` that computes the polynomial expression \( x^2 + 1 \), while storing previously computed results in a `values` attribute.

-   This task demonstrates **function attributes** and **tracking computed values dynamically**.

4.  **9_4_4_remove_marks**  
    **Goal**: Implement `remove_marks(text, marks)`, which removes specified characters from a string while tracking how many times it has been called using a `count` attribute.

-   This task showcases **function attributes** and **tracking function usage** dynamically.

## Output 📜

After completing this lesson, I will be able to:  
✅ Treat **functions as objects**, assigning them attributes and modifying their behavior.  
✅ Access built-in function attributes like **`__name__`**, **`__doc__`**, and **`__defaults__`**.  
✅ Implement **custom function attributes** to store and track additional information.

## Conclusion 🚀

Understanding **functions as objects** is a key aspect of Python’s flexibility.
By treating functions as first-class citizens, I can dynamically modify their behavior, track data, and extend built-in capabilities.
This knowledge is essential for advanced Python programming, including decorators, metaprogramming, and functional programming techniques.
