"""
TODO:
    You have access to the films dictionary, the key of which is the name of
    a certain film, and the value is a dictionary with ratings of this film
    from imdb and kinopoisk.

    Complete the code below so that it displays the name of the film with the
    lowest average rating.

NOTE:
    It is guaranteed that the desired film is unique.

    The average rating is the ratio of the sum of all ratings to their number.

    It is convenient to use the min() function in the problem.
"""

film_ratings = {
    'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
    'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
    'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
    'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
    'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
    'Harry Potter 20th Anniversary: Return to Hogwarts': {
        'imdb': 8.1, 'kinopoisk': 8.2
    },
    'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
    'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
    'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
    'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
    'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}
}


def calculate_average_ratings(
    films: dict[str, dict[str, float]]
) -> dict[str, float]:
    """
    Calculate the average ratings for each film.

    Args:
        films (dict): A dictionary where the key is the name of the film and
        the value is a dictionary containing ratings from imdb and kinopoisk.

    Returns:
        dict: A dictionary where the key is the name of the film and
              the value is the average rating of the film.
    """
    return {
        film: sum(rates.values()) / len(rates)
        for film, rates in films.items()
    }


def get_film_with_lowest_rating(films: dict[str, dict[str, float]]) -> str:
    """
    Get the name of the film with the lowest average rating.

    Args:
        films (dict): A dictionary where the key is the name of the film and
        the value is a dictionary containing ratings from imdb and kinopoisk.

    Returns:
        str: The name of the film with the lowest average rating.
    """
    if not films:
        raise ValueError("The films dictionary is empty.")

    # Calculate average ratings and find the film with the lowest average
    average_ratings = calculate_average_ratings(films)
    return min(average_ratings, key=average_ratings.get)


# Output the film with the lowest average rating
print(get_film_with_lowest_rating(film_ratings))
