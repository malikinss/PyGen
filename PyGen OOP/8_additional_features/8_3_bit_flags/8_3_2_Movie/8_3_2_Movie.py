'''
TODO:
    Implement the MovieGenres class, which describes a flag with movie genres.

    The flag must have five elements:
        ACTION
        COMEDY
        DRAMA
        FANTASY
        HORROR

    Also implement the Movie class, which describes a movie.

    When instantiating the class, it must accept two arguments in
    the following order:
        name — the name of the movie
        genres — the genre of the movie (element of the MovieGenres flag)

    The Movie class must have one instance method:
        in_genre() — a method that takes a genre as an argument and returns
                     True if the movie belongs to this genre, or False
                     otherwise

    An instance of the Movie class must have the following informal string
    representation:
        <movie name>

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes, they
    can be arbitrary.
'''
from enum import Flag, auto


class MovieGenres(Flag):
    """
    Flag for movie genres.
    """
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()


class Movie:
    """
    Movie with name and genres.
    """
    def __init__(self, name: str, genres: MovieGenres) -> None:
        """Init movie.

        Args:
            name: Movie name.
            genres: Movie genres.
        """
        self.name = name
        self.genres = genres

    def in_genre(self, genre: MovieGenres) -> bool:
        """
        Check if movie belongs to genre.

        Args:
            genre: Genre to check.

        Returns:
            bool: True if movie has genre.
        """
        return genre in self.genres

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Movie name.
        """
        return self.name
