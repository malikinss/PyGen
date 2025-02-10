# Choose Plural Function

## Description 📝

The `choose_plural()` function selects the correct noun declension based on a given quantity.
It follows grammatical rules to properly format the output in the form:

```
<quantity> <noun>
```

## Purpose 🎯

This function is useful for:

-   Handling correct noun declensions in Russian and similar languages.
-   Dynamically generating grammatically correct phrases for UI/UX, reports, and notifications.
-   Automating pluralization in text-based applications.

## How It Works 🔍

1. The function takes:
    - `amount` (int): A natural number representing quantity.
    - `declensions` (Tuple[str, str, str]): A tuple with three noun forms (singular, genitive singular, genitive plural).
2. It determines the correct declension based on:
    - If the last two digits are **11-19**, it uses the **genitive plural** (`declensions[2]`).
    - If the last digit is **1** (excluding cases from 11-19), it uses the **nominative singular** (`declensions[0]`).
    - If the last digit is **2, 3, or 4** (excluding cases from 11-19), it uses the **genitive singular** (`declensions[1]`).
    - Otherwise, it uses the **genitive plural** (`declensions[2]`).

## Output 📜

Example usage and expected outputs:

```python
choose_plural(1, ("яблоко", "яблока", "яблок"))
# "1 яблоко"

choose_plural(3, ("стул", "стула", "стульев"))
# "3 стула"

choose_plural(5, ("день", "дня", "дней"))
# "5 дней"

choose_plural(21, ("час", "часа", "часов"))
# "21 час"

choose_plural(102, ("год", "года", "лет"))
# "102 года"
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the function in your script or interactive Python shell.

Example:

```python
from pluralizer import choose_plural

print(choose_plural(47, ("рубль", "рубля", "рублей")))
```

## Conclusion 🚀

The `choose_plural()` function is a powerful tool for correctly handling noun declensions in numerical contexts.
It simplifies text formatting and ensures grammatical accuracy in various applications.
