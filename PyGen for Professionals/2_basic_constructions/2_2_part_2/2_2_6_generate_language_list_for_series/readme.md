# Language List Generator for TV Series

## Description 📝

The program generates a list of languages that can be used in a TV series.
The list is determined based on the languages that are known by everyone in a given group of people.
The languages are displayed in lexicographic order, and if no common languages are found, it indicates that the series will not be filmed.

## Purpose 🎯

This program helps in determining which languages are common among a group of people, which can be useful for ensuring that a TV series can be understood by all viewers.

## How It Works 🔍

1. The program first asks for the number of people in the group.
2. For each person, it takes input of the languages they know (separated by commas).
3. It then finds the intersection of all languages known by the group and displays them in lexicographic order.
4. If no common languages are found, the program will print "The series will not be filmed."

## Output 📜

Example usage and expected outputs:

```python
Enter the number of people: 3
English, French, Spanish
French, English
English, French
# Output: English, French
```

If no common languages are found:

```python
Enter the number of people: 3
English, French
Spanish, German
Italian, Russian
# Output: The series will not be filmed
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the program in your script or interactive Python shell.

Example:

```python
from language_generator import generate_language_list_for_series

number_of_people = 3
result = generate_language_list_for_series(number_of_people)
print(result)
```

## Conclusion 🚀

The program provides an efficient way to determine the common languages among a group of people and helps decide which languages to include in a TV series, ensuring it remains understandable for all viewers.
