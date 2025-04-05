# Pet Class Tracker

## Description 📝

The `Pet` class represents a pet with a given name and tracks all instances using class-level attributes.
It provides class methods to access the first and last instantiated pets and the total number of pets created, maintaining this information across all instances.

## Purpose 🎯

This class is designed for tracking pet instances in scenarios like pet registries, educational examples of class methods and state management, or applications needing instance counting.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `name` attribute, updates the class-level `_counter`, and assigns `_first` (if first instance) and `_last` (always the current instance).
-   **first_pet() Method**: A `@classmethod` returning the first instantiated `Pet` or `None` if none exist.
-   **last_pet() Method**: A `@classmethod` returning the last instantiated `Pet` or `None` if none exist.
-   **num_of_pets() Method**: A `@classmethod` returning the total count of `Pet` instances.
-   **Class Attributes**: `_counter`, `_first`, and `_last` track instance data.

## Usage 📦

1. Save the class in a Python file, e.g., `pet.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from pet import Pet
print(f"Number of pets: {Pet.num_of_pets()}")
pet1 = Pet("Fluffy")
pet2 = Pet("Rex")
print(f"First pet: {Pet.first_pet().name}")
print(f"Last pet: {Pet.last_pet().name}")
print(f"Number of pets: {Pet.num_of_pets()}")
```

## Conclusion 🚀

The `Pet` class offers a simple yet effective way to manage and track pet instances in Python, using class methods to provide global insights.
Its design is flexible and can be extended with features like instance deletion tracking or additional pet attributes for more complex applications.
