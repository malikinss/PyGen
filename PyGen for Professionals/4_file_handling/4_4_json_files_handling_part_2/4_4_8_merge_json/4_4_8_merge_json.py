'''
TODO:
        You have two files data1.json and data2.json, each containing a single
        JSON object:
        {
            "Holly-Anne": [
                33,
                "failed"
            ],
            "Caty": [
                36,
                "failed"
            ],
            ...
        }

        Write a program that merges two JSON objects into one JSON object, and
        if pairs from the first and second objects have matching keys, then
        the value should be taken from the second object.

        The program should write the resulting JSON object to the
        data_merge.json file.

NOTE:
        For example, if the files data1.json and data2.json were as follows:
        {
            "Timur": 99,
            "Anri": 97
        }
        {
            "Dima": 99,
            "Anri": 100
        }
        then the program would have to create a file data_merge.json with the
        following contents:
        {
            "Anri": 100,
            "Dima": 99,
            "Timur": 99
        }
        The elements in the resulting JSON object can be in any order.
'''
import json
from typing import Any, Dict


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Reads JSON data from a file and returns it as a dictionary.

    Args:
        file_path (str): The path to the JSON file to read.

    Returns:
        Dict[str, Any]: A dictionary containing the JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def write_json_file(data: Dict[str, Any], file_path: str):
    """
    Writes a dictionary as JSON data to a file.

    Args:
        data (Dict[str, Any]): The dictionary containing the data to write.
        file_path (str): The path to the output JSON file.

    Raises:
        IOError: If the file cannot be written.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def merge_data(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges two dictionaries, preferring values from the second dictionary in
    case of key conflicts.

    Args:
        data1 (Dict[str, Any]): The first dictionary to merge.
        data2 (Dict[str, Any]): The second dictionary to merge, which will
        override values from the first dictionary in case of key conflicts.

    Returns:
        Dict[str, Any]: A new dictionary containing the merged data.

    Example:
        data1 = {"a": 1, "b": 2}
        data2 = {"b": 3, "c": 4}
        result = merge_data(data1, data2)
        print(result)  # Output: {"a": 1, "b": 3, "c": 4}
    """
    # Create a copy of the first dictionary to avoid
    # modifying the original data1
    merged_data = data1.copy()
    # Update the merged data with values from the second dictionary,
    # overwriting existing values in case of key conflicts
    merged_data.update(data2)
    return merged_data


def merge_json_files(
    input_file_path1: str, input_file_path2: str, output_file_path: str
):
    """
    Merges two JSON files into one, with values from the second file
    overwriting values from the first file in case of key conflicts.
    The result is written to the specified output file.

    Args:
        input_file_path1 (str): Path to the first input JSON file.
        input_file_path2 (str): Path to the second input JSON file.
        output_file_path (str): Path to the output JSON file where merged data
        will be saved.

    Example:
        merge_json_files('data1.json', 'data2.json', 'data_merge.json')
    """
    try:
        # Read data from both JSON files
        data1 = read_json_file(input_file_path1)
        data2 = read_json_file(input_file_path2)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading the files: {e}")
        return

    # Merge the two datasets
    merged_data = merge_data(data1, data2)

    try:
        # Write the merged data to the output file
        write_json_file(merged_data, output_file_path)
    except IOError as e:
        print(f"Error writing to the file: {e}")
        return


# Example usage:
merge_json_files('data1.json', 'data2.json', 'data_merge.json')
