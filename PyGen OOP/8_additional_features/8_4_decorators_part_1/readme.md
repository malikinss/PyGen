Lesson 8.4: Decorators (part 1)

Decorators
Decorating Methods
Decorator Classes
Abstract: This lesson covers different types of decorators in Python.

https://stepik.org/lesson/808351/step/1?unit=811596

This lesson has good theory explonation, has 7 programing practical tasks and 8 theoretical questions presented on the website.

1.

```
# reverse_args Decorator Class Implementation

## Description 📝

The provided code implements the `reverse_args` decorator as a class that reverses the order of positional arguments passed to a decorated function.
The decorator uses `functools.update_wrapper` to preserve the metadata of the decorated function and supports functions with any number of positional and keyword arguments, ensuring the function’s return value is passed through unchanged.

## Purpose 🎯

Intended for scenarios requiring argument order manipulation, such as testing, debugging, or educational examples of Python decorators, callable classes, and metadata preservation.
```

2. 8_4_2_limited_calls

```
# limited_calls Decorator Class Implementation

## Description 📝

The provided code implements the `limited_calls` decorator as a class that restricts a decorated function to a maximum of `n` calls.
It uses `functools.wraps` to preserve the decorated function's metadata and raises a `MaxCallsException` with the specified message if the call limit is exceeded.
The decorator supports functions with any number of positional and keyword arguments and passes the function’s return value unchanged.

## Purpose 🎯

Intended for scenarios requiring call restrictions, such as rate limiting, resource management, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.
```

3. 8_4_3_takes_numbers

```
# takes_numbers Decorator Class Implementation

## Description 📝

The provided code implements the `takes_numbers` decorator as a class that ensures all positional and keyword arguments passed to a decorated function are of type `int` or `float`.
If any argument is of a different type, it raises a `TypeError` with the message "Arguments must be of type int or float".
The decorator uses `functools.update_wrapper` to preserve the decorated function's metadata, supports arbitrary numbers of positional and keyword arguments, and passes the function’s return value unchanged.

## Purpose 🎯

Intended for scenarios requiring type checking of numeric arguments, such as mathematical functions, data processing, or educational examples of Python decorators, callable classes, type checking, and metadata preservation.
```

4. 8_4_4_returns

```
# returns Decorator Class Implementation

## Description 📝

The provided code implements the `returns` decorator as a class that ensures the return value of a decorated function matches a specified `datatype`.
If the return value is not an instance of `datatype`, it raises a `TypeError`.
The decorator uses `functools.wraps` to preserve the decorated function's metadata, supports arbitrary positional and keyword arguments, and passes the return value unchanged when valid.

## Purpose 🎯

Intended for scenarios requiring return type validation, such as API development, type-safe programming, or educational examples of Python decorators, callable classes, type checking, and metadata preservation.
```

5. 8_4_5_exception_decorator

```
# exception_decorator Class Implementation

## Description 📝

The provided code implements the `exception_decorator` as a class that wraps a function to capture its execution outcome.
It returns a tuple: `(value, None)` if the function executes without raising an exception, where `value` is the function’s return value, or `(None, errortype)` if an exception occurs, where `errortype` is the type of the raised exception.
The decorator uses `functools.update_wrapper` to preserve the decorated function's metadata and supports arbitrary positional and keyword arguments.

## Purpose 🎯

Intended for scenarios requiring exception handling and result reporting, such as logging, debugging, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.
```

6. 8_4_6_ignore_exception

```
# ignore_exception Decorator Class Implementation

## Description 📝

The provided code implements the `ignore_exception` decorator as a class that catches specified exception types, prints "Exception <exception type> handled", and returns `None`.
If an exception is not one of the specified types, it is re-raised.
The decorator uses `functools.wraps` to preserve the decorated function's metadata, supports arbitrary positional and keyword arguments, and does not consume the function’s return value when no exception occurs.

## Purpose 🎯

Intended for scenarios requiring selective exception handling, such as logging, error suppression, or educational examples of Python decorators, callable classes, exception handling, and metadata preservation.
```

7. 8_4_7_type_check

```
# type_check Decorator Class Implementation

## Description 📝

The provided code implements the `type_check` decorator as a class that ensures the types of positional arguments passed to a decorated function match the types specified in a provided list.
It checks that the type of each positional argument corresponds to the respective type in the `types` list, raising a `TypeError` if any mismatch occurs.
The decorator handles cases where the number of arguments is less than or greater than the number of types, uses `functools.wraps` to preserve metadata, supports arbitrary positional and keyword arguments, and passes the function’s return value unchanged.

## Purpose 🎯

Intended for scenarios requiring strict type checking of positional arguments, such as API validation, type-safe programming, or educational examples of Python decorators, callable classes, type checking, and metadata preservation.
```
