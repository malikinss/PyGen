# HTML Tag Attribute Extractor 🏷️

## Description 📝

This program extracts all HTML tags and their attributes from a given HTML page fragment.
It identifies the tags, extracts their attributes, and presents them in a structured format.

## Purpose 🎯

The purpose of this script is to analyze an HTML fragment and list all its tags along with their respective attributes in lexicographic order.

## How It Works 🔍

1. **Reads Input**:

    - Accepts multiple lines of HTML code as input.

2. **Extracts Tags and Attributes**:

    - Uses regular expressions to identify HTML tags and extract attribute names.

3. **Processes Data**:

    - Organizes tags and their attributes in a dictionary.

4. **Sorts and Displays Results**:
    - Outputs tags and their attributes in lexicographic order.

## Output 📜

### Example Input:

```html
<a href="https://example.com" class="link"></a>
<b></b>
<div id="main" data-value="123"></div>
```

### Example Output:

```text
a: class, href
b:
div: data-value, id
```

## Usage 📦

1. Run the script and provide HTML input.
2. The program processes the input and outputs the tags with their attributes.

## Conclusion 🚀

This script is a useful tool for analyzing HTML structure and extracting relevant information efficiently.
