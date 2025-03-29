# JSONify Decorator 🛠️

## Description 📝

The `@jsonify` decorator transforms the return value of a decorated function into a JSON string.
It is useful when you need to return data from a function in JSON format, while ensuring the original function’s name and docstring are preserved.

## Purpose 🎯

This decorator takes the return value of a function, converts it into a JSON string using Python’s `json.dumps()` method, and returns that string.
It is particularly useful for functions that need to return structured data in JSON format.

## How It Works 🔍

1. The decorator `@jsonify` is applied to a function.
2. When the decorated function is called, the original return value is transformed into a JSON string using `json.dumps()`.
3. The decorator preserves the original function’s name and docstring using `@wraps`.

## Output 📜

### Example Input:

```python
@jsonify
def get_user_info():
    return {"name": "Alice", "age": 30}
```

### Example Output:

```python
'{"name": "Alice", "age": 30}'
```

## Usage 📦

1. Apply the `@jsonify` decorator to your function.
2. Call the function as usual, and it will return a JSON string.

## Conclusion 🚀

The `@jsonify` decorator simplifies the process of converting function return values into JSON strings, making it ideal for APIs and other applications where JSON is required.
