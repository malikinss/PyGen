Lesson 5.6: callable objects

Callable Objects
Magic Method **call**()
Abstract. The lesson is devoted to callable objects.

https://stepik.org/lesson/805787/step/1?unit=808914

This lesson has good theory explonation, 10 programing practical tasks and 7 theoretical questions presented on the website.

1. 5_6_1_Calculator

```
# Calculator Class Arithmetic Engine
The `Calculator` class creates callable instances for performing basic arithmetic operations (`+`, `-`, `*`, `/`) on two numbers, requiring no initialization arguments.
It uses a dictionary of operator functions and handles division by zero with a `ValueError`.
This class is designed for simple arithmetic tasks, suitable for educational examples of callable objects, basic computation utilities, or applications needing flexible operation execution.
```

2. 5_6_2_RaiseTo

```
# RaiseTo Class Power Function
The `RaiseTo` class creates callable instances that raise a number to a fixed exponent specified during instantiation.
It takes one argument (`degree`) at creation and one argument (`x`) when called, returning `x` raised to `degree`.
This class is designed for exponentiation tasks, suitable for mathematical utilities, educational examples of callable objects, or applications needing repeated power operations.
```

3. 5_6_3_Dice

```
# Dice Class Random Roller
The `Dice` class models a die with a specified number of sides, set during instantiation.
It’s a callable object that, when invoked with no arguments, returns a random integer from 1 to the number of sides, simulating a dice roll using `random.randint`.
This class is designed for random number generation within a range, ideal for games, simulations, educational examples of callable objects, or applications needing dice-like randomness.
```

4. 5_6_4_QuadraticPolynomial

```
# QuadraticPolynomial Class Function Evaluator
The `QuadraticPolynomial` class represents a quadratic trinomial `ax^2 + bx + c`, initialized with coefficients `a`, `b`, and `c`.
It’s a callable object that takes a number `x` and returns the polynomial’s value at that point, computed as `ax^2 + bx + c`.
This class is designed for evaluating quadratic expressions, suitable for mathematical modeling, educational examples of callable objects, or applications needing polynomial calculations.
```

5. 5_6_5_Strip

```
# Strip Class String Trimmer
The `Strip` class creates callable instances that remove specified characters from both ends of a string.
It takes a string `chars` during instantiation, defining the characters to strip, and when called with a string, returns the result using Python’s `strip()` method.
This class is designed for string cleaning, suitable for text preprocessing, educational examples of callable objects, or applications needing custom trimming logic.
```

6. 5_6_6_Filter

```
# Filter Class Iterable Sifter
The `Filter` class creates callable instances that filter elements from an iterable based on a predicate function, defaulting to `bool()` if no predicate is provided.
When called with an iterable, it returns a list of elements where the predicate evaluates to `True`.
This class is designed for data filtering, suitable for list processing, educational examples of callable objects, or applications needing custom iterable refinement.
```

7. 5_6_7_DateFormatter

```
# DateFormatter Class Regional Converter
The `DateFormatter` class creates callable instances that format `date` objects into strings based on a country-specific format, determined by a `country_code` provided during instantiation.
It supports formats for countries like `ru` (DD.MM.YYYY), `us` (MM-DD-YYYY), and others from a predefined table.
This class is designed for date localization, suitable for internationalization, educational examples of callable objects, or applications needing region-specific date displays.
```

8.

```
# CountCalls Decorator Call Counter
The `CountCalls` class is a Python decorator that wraps a function to count how many times it is invoked.
The call count is stored in an accessible `calls` attribute on the decorator instance.
It is designed to be non-intrusive, preserving the original function’s return value and supporting any number of positional and keyword arguments, making it versatile for a wide range of use cases.
This decorator serves as a utility for tracking function call frequency, making it ideal for debugging, performance monitoring, logging function usage in applications, or teaching the concept of decorators in Python.
Its simplicity and flexibility make it a valuable tool in both development and educational contexts.
```

9.

```

```

10.

```

```
