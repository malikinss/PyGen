# Function Execution Time Tracker ⏱️

## Description 📝

This program defines a function `calculate_it` that takes an arbitrary function and its arguments as input, executes the function, and returns the result along with the time it took to compute that result.
This can be useful for benchmarking the performance of various functions.

## Purpose 🎯

The purpose of this program is to measure the execution time of functions and return both their output and the time it took to execute them.
It can be useful for performance testing, optimization, or profiling code.

## How It Works 🔍

The function `calculate_it` works by:

1. Accepting a function `func` and a variable number of arguments `*args`.
2. Measuring the time before and after the function execution using `time.perf_counter()` for high-precision timing.
3. Returning a tuple containing the result of the function and the execution time in seconds.

### Example

```python
def example_function(a, b):
    return a + b

result, execution_time = calculate_it(example_function, 10, 20)

print(f"Result: {result}, Execution Time: {execution_time} seconds")
```

In this example:

-   The `example_function` will return the sum of `10` and `20`.
-   The time it takes to execute the function will be measured and returned along with the result.

## Output 📜

The function will output a tuple with two elements:

1. The result of the function.
2. The time it took to execute the function in seconds.

For example:

```
Result: 30, Execution Time: 0.000123456 seconds
```

## Usage 📦

1. Define a function that you want to measure.
2. Call `calculate_it()` with the function and its arguments as input.
3. The function will return the result and the execution time.

### Steps:

1. Define your function, for example:
    ```python
    def add(a, b):
        return a + b
    ```
2. Call `calculate_it()`:
    ```python
    result, execution_time = calculate_it(add, 5, 10)
    ```
3. Output will include the result and execution time.

## Conclusion 🚀

This program is a simple yet useful tool for profiling function performance.
It can be expanded to measure the time of multiple function executions or used in testing environments to monitor the efficiency of algorithms.
