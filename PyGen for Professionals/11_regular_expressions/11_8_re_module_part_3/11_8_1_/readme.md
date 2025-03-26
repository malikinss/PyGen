# Normalize JPEG Filename Extension 🖼️

## Description 📝

This program normalizes the extension of JPEG or JPG files to `.jpg`.
It handles both `.jpeg` and `.jpg` extensions in any case (e.g., `.JPEG`, `.JPG`).

## Purpose 🎯

The purpose of this function is to standardize the file extension of image files by converting them to `.jpg` regardless of whether the input file has a `.jpeg` or `.jpg` extension.

## How It Works 🔍

1. **Takes Input**:

    - Accepts a filename as a string, which can have either `.jpeg` or `.jpg` extension in any case.

2. **Normalizes the Extension**:

    - Uses a regular expression to match both `.jpeg` and `.jpg` extensions (case-insensitive) and replaces them with `.jpg`.

3. **Returns Normalized Filename**:
    - Outputs the filename with `.jpg` extension.

## Output 📜

### Example Input:

```python
filename = "photo.JPEG"
```

### Example Output:

```python
"photo.jpg"
```

## Usage 📦

1. Call the function with the filename:

    ```python
    normalized_filename = normalize_jpeg("image.jpeg")
    print(normalized_filename)  # Output: image.jpg
    ```

2. The program will return the normalized filename with the `.jpg` extension.

## Conclusion 🚀

This function ensures consistency in filenames by standardizing JPEG file extensions to `.jpg`.
