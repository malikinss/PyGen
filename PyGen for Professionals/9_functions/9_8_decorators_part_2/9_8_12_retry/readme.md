# `retry` Decorator

## Description 📝

The `retry` decorator attempts to re-execute a function if it raises an exception.
The function will be retried up to a specified number of times. If the function continues to fail after the given number of retries, a `MaxRetriesException` is raised.

## Purpose 🎯

This decorator is useful when you want to handle transient errors (e.g., network failures) by retrying a function multiple times before giving up.
It helps make your code more resilient to temporary failures without requiring manual intervention.

## How It Works 🔍

1. **Input**:
    - The decorator takes an integer `times`, which specifies how many times the function should be retried after an exception occurs.
2. **Processing**:
    - The decorated function is called inside a `try-except` block. If an exception occurs, the function will be retried.
    - The function will be retried until the specified number of retries (`times`) is exhausted. If the function still fails, a `MaxRetriesException` is raised.
3. **Output**:
    - If the function succeeds within the retry attempts, the result is returned.
    - If the function fails after all retries, a `MaxRetriesException` is raised.

## Example 📜

```python
# Define the retry decorator
@retry(times=3)
def unstable_function():
    import random
    if random.choice([True, False]):
        raise ValueError("Random failure")
    return "Success!"

# Call the function
try:
    print(unstable_function())
except MaxRetriesException as e:
    print(f"Function failed after retries: {e}")
```

### Output:

```text
Attempt 1 failed with exception: Random failure
Attempt 2 failed with exception: Random failure
Success!
```

### Output when all retries fail:

```text
Attempt 1 failed with exception: Random failure
Attempt 2 failed with exception: Random failure
Attempt 3 failed with exception: Random failure
Function failed after 3 retries: Function failed after 3 retries.
```

In this example, the `unstable_function` is decorated with the `@retry` decorator and will be retried up to 3 times if it raises a `ValueError`. If it still fails after 3 attempts, a `MaxRetriesException` will be raised.

## Usage 📦

1. Define the `retry` decorator in your script.
2. Apply it to any function by using the `@retry(times=number)` syntax, where `number` is the maximum number of retry attempts.
3. Inside the decorated function, raise exceptions as needed. The decorator will handle retrying the function call.

## Conclusion 🚀

The `retry` decorator enhances the reliability of your code by automatically retrying a function if it fails due to exceptions.
This is especially useful when dealing with unreliable resources like network services or APIs.
By using the `retry` decorator, you can improve the robustness of your functions without excessive error handling logic.
