# Sorting Athletes by Various Attributes

## Description

This program sorts a list of athletes, where each athlete is represented by a tuple containing their name, age, height, and weight. The sorting is done based on the user's choice of attribute: name, age, height, or weight.

## Purpose

The program demonstrates how to sort a list of tuples based on a user-selected attribute using a function mapping approach.

## How It Works

1. The `sort_by_*` functions extract the relevant attribute (name, age, height, or weight) from each athlete's tuple to be used as the sorting key.
2. The user is prompted to input a number corresponding to the sorting criterion (1: Name, 2: Age, 3: Height, 4: Weight).
3. The dictionary `my_sort_funcs` maps the user's input to the respective sorting function.
4. The `sort_athletes()` function uses the chosen sorting function to sort the athletes' list and then prints the sorted athletes.

## Usage

Example:

```python
athletes = [
    ('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
    ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
    ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)
]

chosen_sort = input(
    "Enter the number to sort by (1: Name, 2: Age, 3: Height, 4: Weight): "
)

sort_athletes(athletes, my_sort_funcs[chosen_sort])
```

## Output

For example, if the user chooses to sort by `Name` (input `1`):

```
Enter the number to sort by (1: Name, 2: Age, 3: Height, 4: Weight): 1
Матвей 17 168 68
Петя 15 190 90
Рома 16 188 100
Руслан 9 140 33
Рустам 10 128 30
Тимур 11 135 39
Дима 10 130 35
Амир 16 170 70
```

## Conclusion

This program effectively sorts athletes by various attributes. By using a dictionary that maps input to sorting functions, it allows flexible sorting without the need for conditional logic in the main function.
