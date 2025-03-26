'''
TODO:
    Implement a normalize_jpeg() function that takes one argument:
        filename — the file name with the jpeg or jpg extension, which can be
        written in any uppercase letters

    The function should return a new file name with a normalized
    extension — jpg.
'''
import re


def normalize_jpeg(filename: str) -> str:
    """
    Normalize the extension of a JPEG or JPG file to .jpg.

    This function takes a filename with a .jpeg or .jpg extension
    (case-insensitive) and returns the filename with the extension normalized
    to .jpg.

    Args:
        filename (str): The filename to normalize.

    Returns:
        str: The normalized filename with .jpg extension.
    """
    return re.sub(r'\.jpe?g$', '.jpg', filename, flags=re.IGNORECASE)
