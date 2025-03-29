# recviz Decorator for Visualizing Function Execution 🔍

## Description 📝

The `recviz` decorator is designed to visualize the execution of a function, including recursive calls.
It logs the function call with its arguments and the result when the function returns.
This can be especially useful for debugging or understanding how a function operates with various inputs.

## Purpose 🎯

The purpose of the `recviz` decorator is to provide a detailed log of a function's execution process.
It allows me to:

-   View the function call with arguments and keyword arguments.
-   See the result after the function execution.
-   Track recursive function calls and their results.

## How It Works 🔍

1. **Decorator Setup**:

    - `recviz(func)` accepts a function as its argument and returns a wrapper function.
    - The wrapper function handles the printing of the function name, arguments, and result.

2. **Logging Execution**:

    - When the decorated function is called, the wrapper logs:
        - The function name and its arguments.
        - The result when the function returns.
    - The function's indentation increases for recursive calls to visualize the nesting of recursive function executions.

3. **Arguments and Results**:

    - The wrapper uses `repr()` to represent the function arguments and the result for human-readable output.
    - It handles an arbitrary number of positional and keyword arguments.

4. **Handling Recursion**:
    - The `indent` attribute of the wrapper function tracks the current depth of recursion. This helps in visualizing how deep the recursion goes.

### Example Usage:

```python
@recviz
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example call
factorial(3)
```

### Output:

```
-> factorial(3)
    -> factorial(2)
        -> factorial(1)
            -> factorial(0)
            <- 1
        <- 1
    <- 2
<- 6
```

## Output 📜

The decorator will print:

-   The function name and the arguments passed to it.
-   The result of the function's execution.

## Usage 📦

1. Apply the `@recviz` decorator to any function you want to visualize.
2. The function execution, including recursion, will be logged automatically.

## Conclusion 🚀

The `recviz` decorator is an effective tool for tracking and visualizing the execution of functions, especially those involving recursion.
By displaying the function name, arguments, and results, it provides valuable insights into the inner workings of your code.
