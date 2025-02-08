'''
TODO:
    Write a program that reads a line of text and writes it to a text file
    output.txt.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def write_data_to_file(file_name: str, data: str) -> None:
    """
    Writes the given data to a file with the specified file name.

    Parameters:
    - file_name (str): The name of the file to write to.
    - data (str): The data to be written to the file.

    Returns:
    - None: This function doesn't return anything; it only writes data
            to a file.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


given_data: str = input("Enter some text: ")
write_data_to_file('output.txt', given_data)
