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

3.

```

```

4.

```

```

5.

```

```

6.

```

```

7.

```

```
