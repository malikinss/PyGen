# Make HTML Decorator

## Description 📝

The `make_html()` decorator allows you to wrap the return value of a function in a specified HTML tag.
This can be useful for formatting the output of functions in a way that can be directly used in HTML content.
The decorator is flexible and preserves the original function's name and docstring.

## Purpose 🎯

The purpose of this decorator is to automatically format the return value of a function by wrapping it in a specified HTML tag.
This can be especially useful for rendering data or text dynamically in a web application or in situations where HTML formatting is needed.

## How It Works 🔍

1. **Input**:

    - The decorator takes one parameter:
        - `tag`: A string that represents the HTML tag to wrap the function's return value with (e.g., `<div>`, `<p>`, `<h1>`).

2. **Processing**:

    - The `make_html` decorator wraps the original function and calls it to get the result. Then, it formats the result by enclosing it in the specified HTML tag.

3. **Output**:
    - The output is the original function's result wrapped in the specified HTML tag.

## Example 📜

```python
# Define a function with the make_html decorator
@make_html('h1')
def welcome_message(name: str) -> str:
    """Returns a welcome message."""
    return f"Welcome, {name}!"

# Call the decorated function
print(welcome_message("Alice"))
```

### Output:

```html
<h1>Welcome, Alice!</h1>
```

```python
# Another example with a different tag
@make_html('p')
def description(text: str) -> str:
    """Returns a description in a paragraph."""
    return text

# Call the decorated function
print(description("This is a description of the project."))
```

### Output:

```html
<p>This is a description of the project.</p>
```

## Usage 📦

1. Define the `make_html` decorator in your script.
2. Apply the decorator to any function using the `@make_html` syntax.
3. Pass the desired HTML tag as the argument to the decorator.
4. Call the decorated function, and the returned value will be wrapped in the specified HTML tag.

## Conclusion 🚀

The `make_html` decorator offers a simple and efficient way to dynamically format the return values of functions by wrapping them in HTML tags.
This is particularly useful for generating HTML content on the fly without manually adding tags.
The decorator preserves function metadata such as the name and docstring, ensuring clarity and maintainability in your code.
