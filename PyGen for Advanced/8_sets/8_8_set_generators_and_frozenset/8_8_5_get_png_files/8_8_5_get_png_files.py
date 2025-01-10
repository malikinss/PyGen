'''
TODO:
    Using the set generator, complete the code below so that it selects unique
    file names with the .png extension from the files list, regardless of the
    case of the names and extensions.

    Output the file names together with the extension, all on one line,
    in lower case, in alphabetical order, separated by a space.
'''
from typing import List, Set


def get_png_files(files: List[str]) -> Set[str]:
    """
    Generates a set of unique .png file names (case-insensitive).

    Args:
    - files: A list of file names (strings).

    Returns:
    - A set containing file names with the '.png' extension, in lowercase.
    """
    return {file.lower() for file in files if file.lower().endswith('.png')}


def print_sorted_files(png_files: Set[str]) -> None:
    """
    Prints the sorted .png file names in lowercase, space-separated.

    Args:
    - png_files: A set of file names with the .png extension.
    """
    print(*sorted(png_files))


# List of files to check for .png extensions
files = [
    'python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp',
    'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg',
    'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop',
    'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git'
]

# Get the .png files and print them sorted
png_files = get_png_files(files)
print_sorted_files(png_files)
