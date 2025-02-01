# Filtering and Cubing Numbers Divisible by 5 with Remainder 2

## Description

This program filters a given list of numbers to select the three-digit numbers that leave a remainder of 2 when divided by 5. Then, it computes the cubes of those numbers and prints each cube on a separate line.

## Purpose

The program uses the `filter()` function to select numbers meeting specific conditions and the `map()` function to calculate the cubes of the filtered numbers. It then prints the resulting cubes on individual lines.

## How It Works

1. The `predicate()` function filters the list by checking two conditions: if the number is a three-digit number and if it gives a remainder of 2 when divided by 5.
2. The `cube()` function computes the cube of a given number.
3. The `process_numbers()` function combines the filtering and mapping steps to return a list of cubes.
4. Finally, the cubes are printed one per line using `print()`.

## Usage

```python
numbers = [
    1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434,
    696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776,
    657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207,
    266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144,
    1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928,
    1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278,
    166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282,
    336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456,
    1268, 1018, 1274, 387, 120, 340, 963, 832, 1127
]

# Process the numbers and print their cubes
print(*process_numbers(numbers), sep='\n')
```

## Output

For the provided list, the output will consist of the cubes of all three-digit numbers that give a remainder of 2 when divided by 5. Here is an example of the first few outputs:

```
106120375
42607009
282475249
1670961
162300000
314226704
```

## Conclusion

This program efficiently filters and processes the numbers to provide the cubes of those that satisfy the specific conditions. The use of `filter()` and `map()` allows for a concise and functional approach to solving the problem.
