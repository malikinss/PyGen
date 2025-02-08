'''
TODO:
    The program is given a string with the name of a text file as input.

    Write a program that displays its contents on the screen.
'''


def display_file_contents(file_name: str) -> None:
    """
    Displays the contents of a text file on the screen.

    Parameters:
    - file_name (str): The name of the text file to be displayed.

    Returns:
    - None
    """
    try:
        with open(file_name, 'r') as file:
            # Directly read and print each line without storing in a list
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(
            f"Error: An error occurred while reading the file '{file_name}'."
        )


# Example usage
file_name = input("Enter the file name: ")
display_file_contents(file_name)
