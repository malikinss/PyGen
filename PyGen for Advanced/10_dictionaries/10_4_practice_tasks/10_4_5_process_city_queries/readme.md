# City-to-Country Finder 🗺️

## Description 📝

This program allows users to input a list of countries with their corresponding cities and then, for each queried city, outputs the country it belongs to. The program helps in quickly identifying the country of any given city from a predefined list.

## Purpose 🎯

The purpose of this program is to provide a quick and simple tool to map cities to their respective countries, which can be used for educational purposes, geography games, or other applications requiring such information.

## How It Works 🔍

1. **Input**:
    - The program first prompts the user to input a list of countries, each followed by one or more cities in that country.
2. **City-to-Country Mapping**:
    - The input data is processed into a dictionary where cities are mapped to their respective countries.
3. **City Queries**:
    - The program then asks for a series of city names and returns the country each city belongs to.
4. **Output**:
    - The country of each queried city is printed.

## Output 📜

The program prints:

-   The country the given city belongs to.

### Example Input/Output:

**Input**:

```text
Enter the number of countries: 2
Enter a country followed by its cities: USA NewYork LosAngeles
Enter a country followed by its cities: Japan Tokyo Osaka
Enter the number of cities to query: 2
Enter the name of the city: NewYork
Enter the name of the city: Osaka
```

**Output**:

```text
USA
Japan
```

## Usage 📦

1. Copy the code into a Python file, e.g., `city_to_country.py`.
2. Run the program.
3. Enter the number of countries when prompted.
4. Input each country followed by its cities.
5. Enter the number of cities you want to query.
6. Input the names of cities to find their countries.

### Example Run:

```python
# Sample run
Enter the number of countries: 3
Enter a country followed by its cities: USA NewYork LosAngeles
Enter a country followed by its cities: Japan Tokyo Osaka
Enter a country followed by its cities: France Paris Lyon
Enter the number of cities to query: 2
Enter the name of the city: LosAngeles
Enter the name of the city: Paris
Output:
USA
France
```

## Conclusion 🚀

This program simplifies finding the country a city belongs to, which could be useful in a variety of applications, from educational tools to travel apps.
