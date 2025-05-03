# MusicAlbum Data Class Implementation

## Description 📝

The provided code implements the `MusicAlbum` class as an immutable Python data class using the `@dataclass(frozen=True)` decorator.
It defines a music album with four attributes: `title` (string), `artist` (string), `genre` (string), and `year` (integer).
The data class automatically generates an `__init__` method to initialize these attributes, a `__repr__` method for a formal string representation, and an `__eq__` method for equality comparison based on `title`, `artist`, and `year`.
The `frozen=True` parameter ensures immutability, and `field` settings exclude `genre` and `year` from `__repr__` and `genre` from `__eq__` as required.

## Purpose 🎯

Intended for applications requiring structured, immutable representations of music albums, such as music libraries, catalog systems, or educational examples of Python data classes, immutability, and custom comparison logic.

## How It Works 🔍

-   **Class Definition**:
    -   Uses `@dataclass(frozen=True)` to define `MusicAlbum` as an immutable data class.
    -   Declares four fields with type hints:
        -   `title: str`
        -   `artist: str`
        -   `genre: str` with `field(repr=False, compare=False)` to exclude from `__repr__` and `__eq__`.
        -   `year: int` with `field(repr=False)` to exclude from `__repr__`.
-   **Generated Methods**:
    -   `__init__`: Automatically generated to accept `title`, `artist`, `genre`, and `year` in that order and initialize the attributes.
    -   `__repr__`: Automatically generated to produce `MusicAlbum(title='<title>', artist='<artist>')`, excluding `genre` and `year` due to `repr=False`.
    -   `__eq__`: Automatically generated to compare instances based on `title`, `artist`, and `year`, excluding `genre` due to `compare=False`.
    -   `__ne__`: Implicitly supported via `__eq__`, returning the opposite of equality.
    -   Immutability: `frozen=True` prevents attribute modification after initialization.
-   **Behavior**:
    -   Creates immutable instances with the specified attributes.
    -   Provides a formal string representation including only `title` and `artist`.
    -   Supports equality (`==`) and inequality (`!=`) comparisons based on `title`, `artist`, and `year`.
    -   No additional validation is performed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Class Initialization**:
    -   Accepts `title` (str), `artist` (str), `genre` (str), `year` (int) in that order.
    -   Example: `MusicAlbum("Abbey Road", "The Beatles", "Rock", 1969)` creates an instance with those values.
-   **Attributes**:
    -   `title`, `artist`, `genre`, `year` are instance attributes.
    -   Example: `album = MusicAlbum("Abbey Road", "The Beatles", "Rock", 1969)` has `album.title == "Abbey Road"`, etc.
-   **String Representation**:
    -   Produces `MusicAlbum(title='<title>', artist='<artist>')`.
    -   Example: `repr(MusicAlbum("Abbey Road", "The Beatles", "Rock", 1969))` → `MusicAlbum(title='Abbey Road', artist='The Beatles')`.
-   **Comparison Operations**:
    -   `==`: True if `title`, `artist`, and `year` are equal (ignores `genre`).
    -   `!=`: True if any of `title`, `artist`, or `year` differ.
    -   Example: `MusicAlbum("Abbey Road", "The Beatles", "Rock", 1969) == MusicAlbum("Abbey Road", "The Beatles", "Pop", 1969)` → `True`.
-   **Immutability**:
    -   `frozen=True` ensures attributes cannot be modified post-initialization.
    -   Example: Attempting `album.title = "New Title"` raises `dataclasses.FrozenInstanceError`.
-   **Correctness**:
    -   `@dataclass` with `field` settings correctly configures `__repr__` and `__eq__`.
    -   Type hints ensure clarity.
    -   No validation needed per requirements.
-   **Documentation**: Clear docstring.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `frozen=True` enforces immutability as required.
    -   `field(repr=False)` for `genre` and `year` ensures `__repr__` includes only `title` and `artist`.
    -   `field(compare=False)` for `genre` ensures `__eq__` ignores `genre`.
    -   Generated `__repr__` matches the exact format specified.
    -   Generated `__eq__` compares only `title`, `artist`, and `year`.
-   **Performance**:
    -   Initialization: O(1) for setting attributes.
    -   `__repr__`: O(1) for string formatting (two attributes).
    -   `__eq__`: O(1) for comparing three attributes.
    -   Highly efficient for all operations.
-   **Design**:
    -   Data class with `frozen=True` is the most concise and robust way to meet immutability and other requirements.
    -   Type hints (`str`, `int`) clarify attribute types.
    -   Minimal implementation leverages `@dataclass` defaults with custom `field` settings.
-   **Alternatives**:
    -   Manual class with `__init__`, `__repr__`, `__eq__`, and property setters: More verbose and error-prone.
    -   Named tuple: Immutable but less flexible for custom `__repr__` and `__eq__`.
    -   Custom decorator: Unnecessary, as `@dataclass` handles all requirements.
-   **Extensibility**:
    -   Easily extended with additional attributes or methods (e.g., `__str__`).
    -   Could add validation or custom comparison logic if needed.
-   **Edge Cases**:
    -   Empty strings or zero values: Handled correctly, as no validation is required.
    -   Same album with different genres: Considered equal, as `genre` is excluded from `__eq__`.
    -   Subclassing: Inherits data class behavior unless overridden.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create album instances
album1 = MusicAlbum("Abbey Road", "The Beatles", "Rock", 1969)
album2 = MusicAlbum("Abbey Road", "The Beatles", "Pop", 1969)
album3 = MusicAlbum("Let It Be", "The Beatles", "Rock", 1970)

# Test attributes
print(album1.title)    # Abbey Road
print(album1.artist)   # The Beatles
print(album1.genre)    # Rock
print(album1.year)     # 1969

# Test string representation
print(repr(album1))  # MusicAlbum(title='Abbey Road', artist='The Beatles')

# Test equality
print(album1 == album2)  # True (same title, artist, year; genre ignored)
print(album1 == album3)  # False (different title, year)
print(album1 != album3)  # True

# Test immutability
try:
    album1.title = "New Title"
except dataclasses.FrozenInstanceError:
    print("Cannot modify")  # Cannot modify
```

## Conclusion 🚀

The `MusicAlbum` data class implementation is precise, leveraging `@dataclass(frozen=True)` to create an immutable class with automatic `__init__`, `__repr__`, and `__eq__` methods that meet all requirements.
It correctly handles initialization, attributes, string representation, comparisons, and immutability, is efficient, and is extensible.
The design is ideal for structured, immutable data representation or teaching data class concepts, fully compliant with the task’s requirements.
