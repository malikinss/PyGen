# JSON File Reader

## Description 📝

This program reads and deserializes a JSON file provided by the user.
If the file is found and contains valid JSON data, the program prints its contents.
Otherwise, it handles errors gracefully and provides appropriate messages.

## Purpose 🎯

The function `load_json_file()` is designed to:

-   Read the contents of a JSON file.
-   Deserialize the JSON data.
-   Handle errors related to file existence and data validity.

## How It Works 🔍

1. The program prompts the user to enter the name of a JSON file.
2. The function `load_json_file()` attempts to:
    - Open and read the file.
    - Deserialize its contents using `json.load()`.
    - Print the deserialized data.
3. If an error occurs, the function prints:
    - `"File not found"` if the file does not exist.
    - `"Deserialization error"` if the file contains invalid JSON.

## Output 📜

-   If the file is valid, the function prints the deserialized JSON object.
-   If the file does not exist:
    ```text
    File not found
    ```
-   If the file contains invalid JSON:
    ```text
    Deserialization error
    ```

## Usage 📦

1. Run the program.
2. Enter the name of the JSON file.
3. The program will print the file's contents or an appropriate error message.

Example:

```json
{
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

Running:

```text
Enter file name: data.json
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

Example with a missing file:

```text
Enter file name: missing.json
File not found
```

Example with an invalid JSON file:

```text
Enter file name: invalid.json
Deserialization error
```

## Conclusion 🚀

This program provides a simple and efficient way to read and validate JSON files while ensuring proper error handling for missing files or incorrect JSON formatting.
