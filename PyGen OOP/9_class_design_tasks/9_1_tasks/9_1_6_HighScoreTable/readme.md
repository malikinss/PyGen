# HighScoreTable Class Implementation

## Description 📝

The provided code implements the `HighScoreTable` class, which manages a high score table for a game.
The table stores a limited number of top scores, specified at initialization, in descending order.
It supports adding new scores with the `update` method, which only retains scores that rank within the table’s capacity, and resetting all scores with the `reset` method.
The `scores` attribute provides access to the current list of scores.

## Purpose 🎯

Intended for game applications requiring a leaderboard or high score tracking, such as arcade games, or educational examples of Python classes, list management, and sorting.

## How It Works 🔍

-   **Class Definition**:
    -   `HighScoreTable` is a class with type hints for clarity (`List[int]`).
    -   Manages a list of scores with a maximum capacity.
-   **Initialization (`__init__`)**:
    -   Takes `max_len` (integer), the maximum number of scores to store.
    -   Initializes `self.max_len` and an empty `self.scores` list.
-   **update Method**:
    -   Takes a `score` (integer) to add.
    -   Creates a new list with existing scores and appends the new score.
    -   Sorts the combined list in descending order (`sorted(..., reverse=True)`).
    -   Limits the list to `max_len` elements, keeping only the top scores.
    -   Updates `self.scores` with the new sorted list.
-   **reset Method**:
    -   Clears all scores by setting `self.scores` to an empty list.
-   **Behavior**:
    -   Maintains scores in descending order.
    -   Only adds new scores if they rank within the top `max_len` scores.
    -   Allows viewing current scores via `self.scores`.
    -   Supports resetting to an empty state.
    -   No validation needed, as inputs are guaranteed correct.

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Creates an empty table with specified `max_len`.
    -   Example: `HighScoreTable(3)` initializes with `scores = []`.
-   **Viewing Scores**:
    -   `self.scores` provides the current list of scores.
    -   Example: Initially `[]`, after updates `[12, 10, 8]`.
-   **Updating Scores**:
    -   Adds new scores, keeping only the top `max_len` in descending order.
    -   Example: `update(10)`, `update(8)`, `update(12)` → `[12, 10, 8]`.
    -   Ignores scores lower than the current lowest when full.
        -   Example: `update(6)`, `update(7)` → `[12, 10, 8]` (no change).
    -   Replaces lowest score if new score is higher.
        -   Example: `update(9)` → `[12, 10, 9]`.
-   **Resetting Scores**:
    -   Clears all scores.
    -   Example: `reset()` → `scores = []`.
-   **Correctness**:
    -   Scores are always sorted in descending order.
    -   Table respects `max_len` limit.
    -   No validation needed, as inputs are guaranteed integers.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `sorted(..., reverse=True)[:length]` ensures descending order and limits to `max_len`.
    -   Copying scores (`new_scores.extend(self.scores)`) avoids modifying the original list during processing.
    -   `self.scores[:]` assignment updates the list in place, preserving the reference.
    -   Handles cases where the table is not yet full correctly.
-   **Performance**:
    -   Initialization: O(1) for setting `max_len` and empty list.
    -   `update`: O(n log n) for sorting n scores (n ≤ `max_len + 1`).
    -   `reset`: O(1) for clearing the list.
    -   Efficient for typical small `max_len` values (e.g., 3–10).
-   **Design**:
    -   Simple list-based storage is effective for small score tables.
    -   Type hints (`List[int]`) clarify the `scores` attribute.
    -   Methods are concise and focused on their specific tasks.
    -   No external dependencies, using only built-in Python features.
-   **Alternatives**:
    -   Heap/priority queue: More efficient for large `max_len` (O(log n) insertions), but overkill for small tables.
    -   Manual sorting: Less readable and error-prone than `sorted`.
    -   Separate sorting and trimming: Less concise than combined operation.
-   **Extensibility**:
    -   Easily extended to store additional data (e.g., player names with scores).
    -   Could add validation (e.g., positive scores) if needed.
-   **Edge Cases**:
    -   Empty table: `scores = []`, updates work correctly.
    -   `max_len = 0`: No scores are stored, updates have no effect.
    -   Duplicate scores: Kept as-is, sorted correctly.
    -   Table not full: Adds scores until `max_len` is reached.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create high score table
high_score_table = HighScoreTable(3)

# Test initial state
print(high_score_table.scores)  # []

# Add scores
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)  # [12, 10, 8]

# Test lower scores (no change)
high_score_table.update(6)
high_score_table.update(7)
print(high_score_table.scores)  # [12, 10, 8]

# Test score that replaces lowest
high_score_table.update(9)
print(high_score_table.scores)  # [12, 10, 9]

# Test reset
high_score_table.reset()
print(high_score_table.scores)  # []

# Test with different max_len
table = HighScoreTable(2)
table.update(5)
table.update(15)
table.update(10)
print(table.scores)  # [15, 10]
```

## Conclusion 🚀

The `HighScoreTable` class implementation is precise, correctly managing a limited-size high score table with scores in descending order.
The `update` method efficiently adds new scores, respecting the table’s capacity, and the `reset` method clears the table.
The implementation is efficient for typical use cases, extensible, and ideal for game leaderboards or teaching list management, fully compliant with the task’s requirements.
