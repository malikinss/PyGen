# Likes System

## Description 📝

The `likes()` function generates a string that represents the number of people who liked a post, following a specific format based on the number of names provided.

## Purpose 🎯

This function is designed to mimic the like system commonly found in social networks.
It ensures that the output is readable and adjusts dynamically depending on how many people liked the post.

## How It Works 🔍

1. The function takes a list of names as input.
2. Based on the length of the list, it returns a message:
    - **0 names:** `"Никто не оценил данную запись"`
    - **1 name:** `"<name> оценил(а) данную запись"`
    - **2 names:** `"<name1> и <name2> оценили данную запись"`
    - **3 names:** `"<name1>, <name2> и <name3> оценили данную запись"`
    - **More than 3 names:** `"<name1>, <name2> и <n других> оценили данную запись"`
3. The names are kept in their original order.
4. If more than three people like the post, only the first two names are explicitly mentioned, with the rest being counted.

## Output 📜

The function returns a string message depending on the number of names provided.

Example outputs:

```python
likes([])
# "Никто не оценил данную запись"

likes(["Алекс"])
# "Алекс оценил(а) данную запись"

likes(["Алекс", "Борис"])
# "Алекс и Борис оценили данную запись"

likes(["Алекс", "Борис", "Виктор"])
# "Алекс, Борис и Виктор оценили данную запись"

likes(["Алекс", "Борис", "Виктор", "Георгий"])
# "Алекс, Борис и 2 других оценили данную запись"
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Call the `likes()` function in your script or interactive Python shell.

Example:

```python
from likes_system import likes

print(likes(["Алекс", "Борис", "Виктор", "Георгий"]))
```

## Conclusion 🚀

The `likes()` function provides a structured way to display social media-style like messages.
It ensures readability while dynamically handling various cases efficiently.
