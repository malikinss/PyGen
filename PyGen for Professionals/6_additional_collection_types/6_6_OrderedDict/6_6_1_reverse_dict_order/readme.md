# Reversing the Order of an OrderedDict 🔄

## Description 📝

The code takes an `OrderedDict` and prints its content in reverse order.
This is particularly useful when you need to manipulate or display ordered data in reverse.

## Purpose 🎯

✔ Reverse the order of items in an `OrderedDict`.  
✔ Ensure that the dictionary maintains its structure, with the only change being the order of the items.

## Example Input

```python
OrderedDict({
    'Name': 'Брусника',
    'IsNetObject': 'да',
    'OperatingCompany': 'Брусника',
    'TypeObject': 'кафе',
    'AdmArea': 'Центральный административный округ',
    'District': 'район Арбат',
    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
    'SeatsCount': '10'
})
```

## Example Output 📜

```python
OrderedDict([('SeatsCount', '10'),
             ('Address', 'город Москва, переулок Сивцев Вражек, дом 6/2'),
             ('District', 'район Арбат'),
             ('AdmArea', 'Центральный административный округ'),
             ('TypeObject', 'кафе'),
             ('OperatingCompany', 'Брусника'),
             ('IsNetObject', 'да'),
             ('Name', 'Брусника')])
```

## Output Format

-   The output is an `OrderedDict` with the items reversed from the original dictionary.
-   The Python 3.12 version of `OrderedDict` will display the items in a set-like format.

## Usage 📦

To use the function:
1️⃣ Pass an `OrderedDict` to the `reverse_dict_order()` function.  
2️⃣ The function will return a new `OrderedDict` with the order of items reversed.  
3️⃣ Print the result to see the reversed dictionary.

## Conclusion 🚀

This code efficiently reverses the order of an `OrderedDict`, which is useful for various data processing tasks where the order of items matters.
