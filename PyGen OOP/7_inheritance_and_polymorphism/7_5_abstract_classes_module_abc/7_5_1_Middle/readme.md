# Middle and Inheritance Scheme Implementation

## Description 📝

The provided code implements the `Middle` abstract base class and establishes a correct inheritance scheme for the `Average`, `Median`, and `Harmonic` classes.
The `Middle` class serves as a common interface for calculating average ratings (arithmetic mean, median, or harmonic mean) from user and expert votes on a 100-point scale.
It avoids code duplication by centralizing shared functionality, such as vote filtering, while requiring subclasses to implement the specific average calculation via the abstract `get_average` method.

## Purpose 🎯

Intended to unify the interface and shared logic of the `Average`, `Median`, and `Harmonic` classes, which process user and expert ratings for media content.
This hierarchy promotes code reuse, maintainability, and extensibility, making it suitable for applications like rating systems or statistical analysis, as well as educational examples of abstract base classes and inheritance in Python.

## How It Works 🔍

-   **Abstract Base Class (`Middle`)**:
    -   Inherits from `ABC` (Abstract Base Class) to enforce abstraction.
    -   **Initialization (`__init__`)**:
        -   Accepts `user_votes` and `expert_votes` (lists of `int` or `float`).
        -   Stores them as instance attributes.
    -   **Helper Methods**:
        -   `_filter_votes(data, condition)`: Filters a list of votes based on a condition (e.g., range check).
        -   `get_correct_user_votes()`: Returns user votes between 10 and 90.
        -   `get_correct_expert_votes()`: Returns expert votes between 5 and 95.
        -   `_get_correct_votes(users=True)`: Returns filtered user or expert votes based on the `users` flag.
    -   **Abstract Method**:
        -   `get_average(users=True)`: Must be implemented by subclasses to return the average (specific to each class).
-   **Subclasses**:
    -   `Average`: Implements `get_average` to compute the arithmetic mean (`sum(votes) / len(votes)` or `0.0` if empty).
    -   `Median`: Implements `get_average` to compute the median (middle value of sorted votes or `0.0` if empty).
    -   `Harmonic`: Implements `get_average` to compute the harmonic mean (`len(votes) / sum(1/vote)` or `0.0` if empty).
-   **Behavior**:
    -   All classes share vote filtering logic via `Middle`.
    -   Each subclass provides a unique average calculation, maintaining original functionality.
    -   Methods handle edge cases (e.g., empty vote lists) consistently, returning `0.0`.

## Verification ✅

Implementation satisfies requirements:

-   **Inheritance Scheme**:
    -   `Average`, `Median`, and `Harmonic` inherit from `Middle`.
    -   `issubclass(Average, Middle)`, `issubclass(Median, Middle)`, `issubclass(Harmonic, Middle)` → `True`.
-   **Abstract Base Class**:
    -   `Middle` is abstract, with `get_average` as an abstract method.
    -   Cannot instantiate `Middle` directly due to `ABC`.
-   **Functionality Preservation**:
    -   `Average.get_average`: Returns arithmetic mean, e.g., `Average([20, 30], []).get_average()` → `25.0`.
    -   `Median.get_average`: Returns median, e.g., `Median([20, 30, 40], []).get_average()` → `30.0`.
    -   `Harmonic.get_average`: Returns harmonic mean, e.g., `Harmonic([20, 40], []).get_average()` → `26.666...`.
    -   Filtering:
        -   User votes: Only 10 < x < 90, e.g., `[5, 20, 95]` → `[20]`.
        -   Expert votes: Only 5 < x < 95, e.g., `[0, 10, 100]` → `[10]`.
    -   Empty votes: All return `0.0`, e.g., `Average([], []).get_average()` → `0.0`.
-   **Code Reuse**:
    -   Vote filtering (`get_correct_user_votes`, `get_correct_expert_votes`, `_filter_votes`) and vote selection (`_get_correct_votes`) are centralized in `Middle`.
    -   Subclasses only implement `get_average`, avoiding duplication.
-   **Interface**:
    -   Consistent interface: All classes accept `user_votes`, `expert_votes`, and provide `get_average(users=True)`.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**: `Middle` centralizes filtering logic, ensuring consistent vote validation across subclasses. Each subclass implements `get_average` as originally specified. No validation beyond filtering is needed per requirements.
-   **Performance**:
    -   Filtering: O(n) for vote lists of length n.
    -   `Average`: O(n) for sum and length.
    -   `Median`: O(n log n) for sorting.
    -   `Harmonic`: O(n) for sum of reciprocals.
    -   All are efficient for typical rating datasets.
-   **Design**:
    -   `Middle` abstracts shared functionality, reducing duplication.
    -   `_filter_votes` is reusable for any condition, enhancing flexibility.
    -   `_get_correct_votes` simplifies `get_average` implementations.
    -   Type hints and docstrings improve clarity.
    -   Using `ABC` ensures subclasses implement `get_average`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
avg = Average([5, 20, 30, 95], [0, 10, 100])
med = Median([5, 20, 30, 95], [0, 10, 100])
harm = Harmonic([5, 20, 30, 95], [0, 10, 100])

# Test user votes (10 < x < 90 → [20, 30])
print(avg.get_average())  # 25.0
print(med.get_average())  # 30.0
print(harm.get_average())  # 24.0

# Test expert votes (5 < x < 95 → [10])
print(avg.get_average(users=False))  # 10.0
print(med.get_average(users=False))  # 10.0
print(harm.get_average(users=False))  # 10.0

# Test empty votes
empty = Average([], [])
print(empty.get_average())  # 0.0

# Test inheritance
print(isinstance(avg, Middle))  # True
```

## Conclusion 🚀

The `Middle` abstract base class and inheritance scheme are precise, unifying the `Average`, `Median`, and `Harmonic` classes with shared vote-filtering logic while preserving their unique average calculations.
The implementation minimizes code duplication and maintains functionality, making it ideal for rating systems or inheritance education, fully compliant with the task’s requirements.
