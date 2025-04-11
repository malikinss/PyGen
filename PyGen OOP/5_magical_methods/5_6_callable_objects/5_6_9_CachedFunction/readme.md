# CachedFunction Decorator Result Storer

## Description 📝

The `CachedFunction` class is a Python decorator designed to enhance the efficiency of function calls by caching their return values based on the input arguments.
It maintains a persistent `cache` attribute, implemented as a dictionary where each key is a tuple of positional arguments passed to the function, and the corresponding value is the result returned by the function for those arguments.
This caching mechanism ensures that subsequent calls with the same arguments retrieve the precomputed result instead of recalculating it, making it particularly useful for functions with computationally expensive operations or frequent repeated invocations.
The decorator is tailored to work seamlessly with functions that accept only positional arguments, ensuring unambiguous caching as specified.

## Purpose 🎯

The primary purpose of the `CachedFunction` decorator is to optimize performance by memoizing function results, thereby reducing redundant computations.
It is an excellent tool for scenarios such as recursive algorithms (e.g., Fibonacci calculations), data processing tasks with repetitive inputs, or any application where the same function calls occur multiple times with identical arguments.
Beyond practical use, it serves as an educational resource for demonstrating the power of decorators and caching strategies in Python, offering a clear example of how to implement stateful behavior in a functional context.
Its design balances simplicity with utility, making it accessible to both novice and experienced developers.

## How It Works 🔍

-   **Class Structure**: The decorator is implemented as a class, `CachedFunction`, which allows it to maintain state (the cache) across multiple calls to the decorated function. This stateful approach is key to its functionality, as it needs to remember previous results.
-   **Initialization (`__init__`)**: When the decorator is applied to a function, the `__init__` method is called with the function (`func`) as an argument. It initializes two instance attributes:
    -   `self.func`: Stores the original function to be called when needed.
    -   `self.cache`: An empty dictionary that will hold the cached results, with keys as tuples of arguments and values as the function’s return values.
-   **Call Execution (`__call__`)**: This method makes the decorator instance callable, allowing it to act as a proxy for the original function. It works as follows:
    -   Takes all positional arguments (`*args`) passed to the function call.
    -   Converts these arguments into a tuple (`key = tuple(args)`), which serves as a hashable key for the cache dictionary (since lists are unhashable, but tuples are not).
    -   Checks if `key` exists in `self.cache`. If not, it calls the original function with the arguments (`self.func(*args)`), stores the result in `self.cache[key]`, and then returns it.
    -   If `key` is already in the cache, it skips computation and directly returns the cached value (`self.cache[key]`).
-   **Cache Accessibility**: The `cache` attribute is publicly accessible on the decorated function, allowing users to inspect or manipulate the stored results if needed.

## Usage 📦

1. **Save the Code**: Place the `CachedFunction` class in a Python file, such as `cached_function.py`, ensuring it’s the only code submitted per the task requirements.
2. **Apply the Decorator**: Use the `@CachedFunction` syntax above any function definition that takes positional arguments to enable caching. For example:
    ```python
    @CachedFunction
    def add(a, b):
        return a + b
    ```
3. **Call the Function**: Invoke the decorated function as usual; the decorator handles caching automatically. For instance:
    ```python
    print(add(2, 3))  # Computes and caches: 5
    print(add(2, 3))  # Retrieves from cache: 5
    print(add.cache)  # {(2, 3): 5}
    ```
4. **Inspect the Cache**: Access the `cache` attribute on the function object (e.g., `add.cache`) to view the dictionary of cached argument-result pairs.
5. **Testing Environment**: Since the task specifies submission without calling code, the testing system will verify functionality by applying the decorator to its own test functions and checking the `cache` and return values.

## Conclusion 🚀

The `CachedFunction` decorator delivers a robust and efficient solution for caching function results in Python, leveraging a class-based approach to maintain a persistent cache across calls.
Its design ensures that the original function’s behavior remains intact while adding significant performance benefits for repeated invocations with the same arguments.
The exposed `cache` attribute provides transparency and flexibility, allowing users to inspect or potentially modify the cache if desired.
This implementation is both practical and educational, serving as a foundational example of memoization that could be extended with features like cache size limits, expiration policies, or support for keyword arguments (though not required here due to the positional-only constraint).
Its simplicity and effectiveness make it a valuable addition to any Python developer’s toolkit, particularly in performance-critical applications or learning environments focused on advanced programming techniques.
