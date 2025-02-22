# File Extension Counter 📝

## Description 📝

This program analyzes a list of file names, extracts their extensions, and counts how many times each extension appears.
The results are displayed in lexicographic order, with each extension followed by its count.

## Purpose 🎯

-   Identify different file extensions in a given list of files.
-   Count occurrences of each file extension.
-   Display the results in a sorted format.

## Output 📜

The output is structured as:

```
<extension>: <number of files>
```

For example:

```
csv: 4
exe: 10
jpeg: 5
json: 4
mp3: 5
mp4: 5
...
```

## Usage 📦

1. Ensure that the list `files` contains the file names to be processed.
2. Run the script, and it will print the count of each file extension.

### Example Run

```bash
$ python file_extension_counter.py
```

### Expected Output (partial):

```
csv: 4
exe: 10
jpeg: 5
json: 4
mp3: 5
mp4: 5
...
```

## Conclusion 🚀

This script efficiently extracts and counts file extensions, presenting the data in a structured and readable format.
It is useful for file management and quick analysis of file types in a directory.
