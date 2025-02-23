# Print Bar Chart

## Description 📝

This Python function generates a bar chart based on the frequency of elements in the given data.
The chart visually represents occurrences using a specified character as a bar marker.

## Purpose 🎯

The function is useful for quickly visualizing the frequency of characters in a string or occurrences of words in a list.

## How It Works 🔍

1. The function takes two parameters:

    - `data`: A string (characters will be counted) or a list of strings (words will be counted).
    - `mark`: A single character used to visually represent the count.

2. The function counts the occurrences of each unique character (for strings) or word (for lists).

3. It sorts the elements by decreasing count. If counts are equal, the original order is preserved.

4. It prints each element followed by a vertical bar (`|`) and its count represented using `mark` repeated accordingly.

5. The output is formatted for proper alignment, ensuring readability.

## Output 📜

Each unique character or string is displayed with its frequency, formatted as:

```
<character or string> |<repeated mark symbols>
```

### Example:

```python
print_bar_chart('beegeek', '+')
```

#### Output:

```
e |++++
b |+
g |+
k |+
```

```python
print_bar_chart(['apple', 'banana', 'apple', 'cherry'], '*')
```

#### Output:

```
apple  |**
banana |*
cherry |*
```

## Usage 📦

1. Import or define the `print_bar_chart()` function in your Python script.
2. Call the function with the desired data and marker character.
3. View the formatted output.

### Running the function:

```python
print_bar_chart("hello world", "#")
```

#### Output:

```
l |+++
o |++
h |+
e |+
  |+
w |+
r |+
d |+
```

## Conclusion 🚀

This function provides a simple and effective way to visualize data frequency in a text-based format.
It can be used for statistical analysis, debugging text data, or simply for fun visualizations.
