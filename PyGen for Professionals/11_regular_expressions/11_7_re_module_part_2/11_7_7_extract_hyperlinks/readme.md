# HTML Hyperlink Extractor

## Description 📝

This program extracts all hyperlinks (address parts and pointers) from an HTML page fragment.
It looks for `<a>` tags and extracts the URL (address part) specified in the `href` attribute and the text (pointer) inside the `<a></a>` tag.
The program then outputs each hyperlink's components in a specified format: `<address part>, <pointer>`.

## Purpose 🎯

The program is useful for parsing HTML fragments to extract URLs and the visible text associated with them.
This can be helpful for tasks like web scraping or analyzing HTML documents to gather all the links on a page.

## How It Works 🔍

1. **Input**: The program takes an arbitrary number of input lines representing an HTML fragment.
2. **Regular Expression**: The function uses a regular expression (`<a\s+href="([^"]+)">(.+?)</a>`) to:
    - Extract the URL (`href` attribute) from each `<a>` tag.
    - Extract the text (pointer) between the opening and closing `<a>` tags.
3. **Output**: It prints each hyperlink's address part and pointer, formatted as `<address part>, <pointer>`.

## Output 📜

### Example Input:

```html
<a href="https://stepik.org">Stepik</a>
<a href="https://www.example.com">Example</a>
<a href="https://github.com">GitHub</a>
```

### Example Output:

```text
https://stepik.org, Stepik
https://www.example.com, Example
https://github.com, GitHub
```

## Usage 📦

1. Call the `extract_hyperlinks()` function, passing a list of HTML code lines as input.
2. The function processes the input, finds all `<a>` tags, and extracts the URL and text (pointer) for each hyperlink.
3. The result is printed in the format `<address part>, <pointer>`.

### Example Usage:

```python
html_lines = [
    '<a href="https://stepik.org">Stepik</a>',
    '<a href="https://www.example.com">Example</a>',
    '<a href="https://github.com">GitHub</a>'
]
extract_hyperlinks(html_lines)
```

## Conclusion 🚀

The `extract_hyperlinks()` function is a simple and effective tool for extracting hyperlinks from HTML fragments, making it ideal for web scraping, analyzing HTML content, or extracting all links from a web page.
