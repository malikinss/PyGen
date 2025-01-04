# Get City Info and Return as Tuple 🏙️

## Description 📝

This program prompts the user to input the name of a city and the year of its foundation.
It then stores these values in a tuple, where the first element is the city name (a string), and the second element is the year of foundation (an integer).

## Purpose 🎯

-   To take user input for city name and foundation year.
-   To return the city name and foundation year as a tuple.

## How It Works 🔍

1. **Input Collection**:
    - The user is prompted to input the name of the city, which is stored in the `city_name` variable.
    - The user is then prompted to input the year of foundation, which is converted into an integer and stored in the `city_year` variable.
2. **Tuple Creation**:
    - A tuple named `city` is created using the values of `city_name` and `city_year`.
3. **Return the Tuple**:
    - The function `get_city_info()` returns the created tuple.

### Example:

```
Input:
Enter city name: Moscow
Enter city foundation year: 1147

Output:
('Moscow', 1147)
```

## Output 📜

The output will be a tuple with the city name and year of foundation:

```
('Moscow', 1147)
```

## Conclusion 🚀

The code successfully collects the name and foundation year of a city from the user, and returns this information as a tuple.
