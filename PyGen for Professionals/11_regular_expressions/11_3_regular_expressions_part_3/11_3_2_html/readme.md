# Regular Expression for Matching HTML Comments

## Description 📝

In **HTML**, comments are enclosed within **`<!-- ... -->`** and are **not displayed** in the browser.
This regular expression is designed to **match and extract** **HTML comments** from a given text.

## Purpose 🎯

The **regex** ensures that:

1. The **comment starts with** `<!--`.
2. The **comment ends with** `-->`.
3. It **captures everything in between**, including spaces, letters, digits, and symbols.

## How It Works 🔍

The regex:

```regex
r'<!--.*?-->'
```

**Explanation:**

-   **`<!--`** → Matches the **opening comment tag**.
-   **`.*?`** → Matches **any characters (non-greedy)** inside the comment.
-   **`-->`** → Matches the **closing comment tag**.

## Output 📜

**Example Usage:**

```python
import re

regex = r'<!--.*?-->'

html_text = """
<p>This is a paragraph.</p>
<!-- This is a comment -->
<div>Content</div>
<!-- Another comment with special chars !@#$%^&*() -->
"""

matches = re.findall(regex, html_text)

for match in matches:
    print(match)
```

**Expected Output:**

```
<!-- This is a comment -->
<!-- Another comment with special chars !@#$%^&*() -->
```

## Usage 📦

-   **HTML Parsing**: Extract **comments** from an **HTML document**.
-   **Web Scraping**: Ignore **comments** when processing HTML **data**.
-   **Code Analysis**: Find and **remove or modify comments** in HTML files.
-   **Debugging**: Identify **unwanted comments** in web pages.

## Conclusion 🚀

This **regular expression** accurately detects **HTML comments**, making it useful for **HTML processing, web scraping, and code analysis**.
