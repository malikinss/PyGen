# Correcting Poet Data 🎭

## Description 📝

This program is designed to correct the place of birth in a tuple containing biographical data about a Russian poet. The tuple consists of the poet's surname, year of birth, and city of birth. In the example, the city of birth for Alexander Pushkin was incorrectly listed, and the program corrects it.

## Purpose 🎯

-   To demonstrate how to correct a specific element in a tuple by converting it to a list, modifying the list, and then converting it back to a tuple.
-   To provide a corrected version of biographical data for Russian poets.

## How It Works 🔍

1. **Function `correct_poet_data(poet_data: Tuple)`**:

    - Takes a tuple with the poet's surname, year of birth, and city of birth as input.
    - Converts the tuple into a list to allow modification of the city of birth.
    - Corrects the city of birth by replacing the incorrect value with 'Москва'.
    - Returns the corrected data as a new tuple.

2. **Example Input**:
    - The initial poet data: `('Пушкин', 1799, 'Санкт-Петербург')`
    - The city of birth is corrected to 'Москва'.

### Example:

```
Input: ('Пушкин', 1799, 'Санкт-Петербург')
Output: ('Пушкин', 1799, 'Москва')
```

## Output 📜

The output will be:

```
('Пушкин', 1799, 'Москва')
```

## Conclusion 🚀

The program successfully corrects the poet's place of birth and returns the updated tuple with the accurate data.
