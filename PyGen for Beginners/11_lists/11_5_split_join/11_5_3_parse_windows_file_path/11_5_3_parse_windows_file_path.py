'''
TODO:
    In the Windows operating system, the full file name consists of a drive
    letter followed by a colon and the "\" character, then the subdirectories
    (folders) in which the file is located are listed through the same
    character, and the file name is written at the end
    "(C:/Windows/System32/calc.exe)".

    The input to the program is one line with the correct file name
    in the Windows operating system.

    Write a program that parses a string into pieces separated
    by the "\" character.

    Print each part on a separate line.
'''


def parse_windows_file_path(file_path: str) -> None:
    """
    This function takes a file path in the Windows operating system format and
    splits it into parts separated by the backslash character ("\\").
    It then prints each part on a separate line.

    Args:
        file_path (str): The full file path in Windows format, which includes
        drive letter, subdirectories, and file name.

    Returns:
        None: The function prints each part of the path on a separate line.
    """
    parts = file_path.split("\\")
    print(*parts, sep="\n")


# Input the file path
file_path = input()

# Call the function with the input file path
parse_windows_file_path(file_path)
