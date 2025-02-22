# Chess Tournament Wins Tracking ♟️🏆

## Description 📝

This program tracks wins and losses from a series of chess games between students.
The `wins()` function computes the victories of each student, and the `print_results()` function displays the results in a sorted, readable format.

## Purpose 🎯

✔ Track wins in a chess tournament by mapping each student to the set of students they defeated.  
✔ Display the results of each student's victories in a sorted manner.  
✔ Ensure no draws are included in the data.

## Example Input

```python
games = [
    ('Артур', 'Дима'),
    ('Артур', 'Тимур'),
    ('Артур', 'Анри'),
    ('Дима', 'Артур')
]
```

## Example Output 📜

```
Дима -> Артур
Артур -> Анри, Дима, Тимур
```

## Output Format

-   Each student's name is followed by `->` and a comma-separated list of students they defeated.
-   Results are displayed in lexicographical order of the students' names.

## Usage 📦

To use the program:  
1️⃣ Pass a list of tuples containing the winners and losers of each chess game.  
2️⃣ Run the `wins()` function to compute the results.  
3️⃣ Call `print_results()` to display the formatted results.

### Run the script:

```bash
$ python chess_tournament.py
```

## Conclusion 🚀

This program provides a way to track the victories of students in a chess tournament, making it easy to view who each student has defeated.
The results are displayed in a clean, organized format for better clarity.
