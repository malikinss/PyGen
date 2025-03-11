# Generator for Parsing Planet Data from a Text File

## Description 📝

The `txt_to_dict()` function is a generator that reads the `planets.txt` file containing information about various planets.
It returns a sequence of dictionaries, each of which contains the characteristics (name, diameter, mass, and orbital period) of a planet.
The function processes the file in a memory-efficient manner, yielding one planet's data at a time.

## Purpose 🎯

This function is useful for efficiently extracting planet information from a structured text file.
It returns each planet's data as a dictionary, making it easy to work with the information programmatically.

## How It Works 🔍

1. **Input Parameters**:

    - No parameters are required. The function reads from a predefined file, `planets.txt`.

2. **File Parsing**:
    - The `read_lines()` helper function reads the file line by line.
    - The `parse_line()` function processes each line, converting the key-value pairs into a dictionary format.
    - The `group_planet_data()` function groups the lines into planet data dictionaries. It checks for empty lines to identify when one planet's data ends and another begins.
3. **Generator**:

    - The `txt_to_dict()` function serves as the main generator, yielding a dictionary for each planet, containing the keys:
        - `Name`
        - `Diameter`
        - `Mass`
        - `OrbitalPeriod`

4. **Mass Parsing**:
    - The mass values are parsed using a specific function (`parse_mass()`) to convert scientific notation to floating-point numbers.

## Output 📜

The function yields a sequence of dictionaries:

```python
{
    'Name': 'Mercury',
    'Diameter': '4879.4',
    'Mass': '3.302*10^23',
    'OrbitalPeriod': '0.241'
}
```

### Example:

```python
>>> for planet in txt_to_dict():
>>>     print(planet)
{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302*10^23', 'OrbitalPeriod': '0.241'}
{'Name': 'Venus', 'Diameter': '12103.6', 'Mass': '4.869*10^24', 'OrbitalPeriod': '0.615'}
...
```

## Usage 📦

1. Save the code to a file, e.g., `planet_data.py`.
2. Call the `txt_to_dict()` function to iterate through the planet data:
    ```python
    for planet in txt_to_dict():
        print(planet)  # Outputs a dictionary for each planet
    ```

## Conclusion 🚀

The `txt_to_dict()` function efficiently processes planet data from a structured text file and returns the information in a format that's easy to work with.
By using a generator, it processes the data lazily, making it suitable for large files. 🌍✨
