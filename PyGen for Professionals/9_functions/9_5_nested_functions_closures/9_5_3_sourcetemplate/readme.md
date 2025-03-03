# URL Query String Generator

## Description 📝

This function, `sourcetemplate(url)`, generates a URL with query parameters dynamically.
It returns a function that accepts an arbitrary number of named arguments (representing key-value pairs for the query string) and returns the original URL concatenated with the formatted query string.
If called without arguments, it simply returns the original URL.

## Purpose 🎯

The purpose is to generate a URL with a properly formatted query string.
This is useful in web development or any context where URLs need to be dynamically constructed with query parameters, sorted lexicographically by their keys.

## How It Works 🔍

1. **Base Function (`sourcetemplate`)**:
    - The function accepts a URL string and returns an inner function, which will handle the creation of query strings.
2. **Query String Generation**:
    - The inner function accepts arbitrary named arguments (as keyword arguments) and forms a query string by sorting the keys lexicographically.
    - If arguments are passed, it appends the query string to the URL.
3. **Example Usage**:

    - Calling `sourcetemplate('https://example.com')` and passing arguments `name='timur'` and `color='green'` will return:
        ```python
        'https://example.com?color=green&name=timur'
        ```

4. **Edge Case**:
    - If no arguments are passed, the function returns the original URL unchanged.

## Output 📜

Example usage:

```python
# Create a function to generate the URL with query parameters
url_gen = sourcetemplate('https://example.com')

# Calling the function with parameters
print(url_gen(name='timur', color='green'))
# Output: 'https://example.com?color=green&name=timur'

# Calling the function without parameters returns the original URL
print(url_gen())
# Output: 'https://example.com'
```

## Usage 📦

1. Save the code to a file named `url_template.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using Python:

    ```python
    from url_template import sourcetemplate

    url_gen = sourcetemplate('https://example.com')
    print(url_gen(name='timur', color='green'))  # 'https://example.com?color=green&name=timur'
    print(url_gen())  # 'https://example.com'
    ```

## Conclusion 🚀

This function provides a flexible way to generate URLs with query parameters, ensuring that the parameters are correctly sorted and appended to the base URL.
It's particularly useful in web development when constructing URLs dynamically.
