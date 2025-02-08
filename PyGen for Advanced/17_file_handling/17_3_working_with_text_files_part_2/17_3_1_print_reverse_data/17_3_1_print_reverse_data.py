'''
TODO:
    A text file is available to you "text.txt" with one line of text.

    Write a program that displays this line in reverse order.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def reverse(given_string: str) -> str:
    """
    Reverses a given string.

    Parameters:
    - given_string (str): The string to reverse.

    Returns:
    - str: The reversed string.
    """
    return given_string[::-1]


def get_data_from_file(file_name: str) -> str:
    """
    Reads the content of a text file and returns the text.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - str: The content of the file.
    """
    try:
        with open(file_name, 'rt', encoding='utf-8') as given_file:
            # Read and strip trailing newlines or spaces
            return given_file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return ""
    except IOError as e:
        print(f"Error reading the file: {e}")
        return ""


# Get the data and reverse it
data = get_data_from_file('text.txt')

# Print the reversed data if file read was successful
if data:
    print(reverse(data))
