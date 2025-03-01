# Film Ratings Analysis 📝

## Description 🎯

This program processes a dictionary of film ratings from IMDb and Kinopoisk to calculate the average ratings of each film.
It then identifies and returns the name of the film with the lowest average rating.

## Purpose 🎯

The purpose of this program is to:

-   Calculate the average ratings of films based on ratings from different sources.
-   Identify and output the film with the lowest average rating.

## How It Works 🔍

1. The program takes a dictionary `film_ratings`, where the key is the film name, and the value is another dictionary containing ratings from IMDb and Kinopoisk.
2. The function `calculate_average_ratings()` calculates the average rating for each film.
3. The function `get_film_with_lowest_rating()` finds and returns the film with the lowest average rating.

## Output 📜

The output is the name of the film with the lowest average rating, based on the ratings from IMDb and Kinopoisk.

For example, the output for the given `film_ratings` dictionary is:

```
"Encanto"
```

## Usage 📦

1. Copy the provided code into a Python file.
2. Run the file to display the film with the lowest average rating.
3. The program will print the name of the film with the lowest average rating.

```python
film_ratings = {
    'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
    'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
    'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
    # Add more films here...
}

print(get_film_with_lowest_rating(film_ratings))
```

## Conclusion 🚀

This program efficiently calculates the average ratings of films and determines the one with the lowest rating, helping in comparing films from different sources.
