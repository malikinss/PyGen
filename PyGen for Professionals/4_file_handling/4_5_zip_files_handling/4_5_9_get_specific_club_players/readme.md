# Extract and Sort Arsenal Players from a ZIP Archive ⚽📂

## Description 📝

This script extracts football player data from JSON files inside a ZIP archive and lists only Arsenal players, sorting them lexicographically by:

1. First name
2. Last name (if first names are identical)

## Purpose 🎯

-   Filter JSON files from the ZIP archive.
-   Validate JSON structure before processing.
-   Find players who play for Arsenal.
-   Sort and display names in lexicographical order.

## How It Works 🔍

1. Extracts JSON files from `data.zip`.
2. Validates JSON format (handles errors gracefully).
3. Filters players by `team == 'Arsenal'`.
4. Sorts players alphabetically.
5. Prints names, one per line.

## Usage 📦

### Run the script

```python
arsenal_players = get_players_from_club('data.zip', 'Arsenal')
display_players(arsenal_players)
```

✅ Outputs Arsenal players' names, sorted lexicographically:

```
Alex Iwobi
Alexis Sanchez
```

## Conclusion 🚀

This script efficiently processes ZIP archives, validates JSON data, and extracts sorted player lists—perfect for sports analytics!
