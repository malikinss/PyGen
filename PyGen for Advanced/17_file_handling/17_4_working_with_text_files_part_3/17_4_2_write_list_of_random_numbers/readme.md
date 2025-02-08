# Writing Random Numbers to a File

## Description 📝

This Python program generates 25 random numbers within the range of 111 to 777 (inclusive) and writes each number on a new line in a file named `random.txt`. The program uses the `random.sample()` function to generate the random numbers and then writes them to the file using the `write_data_to_file()` function.

## Purpose 🎯

The purpose of this program is to demonstrate how to generate random numbers in Python and write them to a file. It specifically shows how to work with ranges, lists, and file handling to store data.

## How It Works 🔍

1. **Random Number Generation**:
    - The `get_list_of_random_numbers()` function generates 25 random numbers in the range from 111 to 777 (inclusive).
2. **Formatting**:
    - The `convert_list_to_write_format()` function converts the list of numbers into a list of strings, each followed by a newline character.
3. **File Writing**:
    - The `write_data_to_file()` function writes the list of numbers into `random.txt`, each number on a new line.

## Output 📜

The program creates (or overwrites) the `random.txt` file and writes 25 random numbers to it. Each number will appear on a new line.

### Example:

After running the program, the `random.txt` file will contain something like:

```
423
196
342
514
763
...
```

## Usage 📦

1. Save the code in a file, e.g., `write_random_numbers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python write_random_numbers.py`
5. The program will generate the random numbers and write them to `random.txt`.

## Conclusion 🚀

This program demonstrates how to generate random numbers in a specified range and write them to a file in Python. It showcases list manipulation, random number generation, and file handling.
