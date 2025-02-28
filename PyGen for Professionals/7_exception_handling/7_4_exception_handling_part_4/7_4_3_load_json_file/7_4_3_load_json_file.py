'''
TODO:
    Write a program that takes the name of a JSON file as input, deserializes
    the object contained in this file, and outputs it.

    If a file with this name is not in the program folder, the program should
    output the text:
        File not found

    If a file with this name contains incorrect data (i.e., does not comply
    with the JSON format), the program should output the text:
        Deserialization error

    The program receives the name of a JSON file as input.

    The program should deserialize the object contained in the file with the
    entered name and output it.

    If an error occurred while searching for a file or deserializing its
    contents, the program should output the corresponding text.

NOTE:
    The name of the file being submitted already contains an extension.
'''
import json


def load_json_file(file_path: str) -> None:
    """
    Reads and prints the contents of a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    If the file is not found, prints "File not found".
    If the file contains invalid JSON, prints "Deserialization error".
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(json.load(file))
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Deserialization error")


# Prompt user for input and call the function
file_name = input()
load_json_file(file_name)
