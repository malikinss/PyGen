'''
TODO:
    Implement an immutable MusicAlbum class that describes a music album.

    When instantiated, the class must accept four arguments in the following
    order:
        title — album title (type str)
        artist — album author (type str)
        genre — album genre (type str)
        year — album release year (type int)

    An instance of the MusicAlbum class must have four attributes:
        title — album title
        artist — album author
        genre — album genre
        year — album release year

    Also, an instance of the MusicAlbum class must have the following formal
    string representation:
        MusicAlbum(title='<album title>', artist='<album author>')

    Finally, instances of the MusicAlbum class must support comparisons
    between themselves using the == and != operators.

    Two music albums are considered equal if their titles, authors,
    and release years match.

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the MusicAlbum
    class, it can be arbitrary.
'''
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    """
    A data class for an immutable music album with title, artist, genre,
    and year.
    """
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)
