# Reordering an OrderedDict Based on a Custom Rule 🔄

## Description 📝

The goal of this code is to reorder the elements of an `OrderedDict` in a pattern where elements are arranged as: first, last, second, second-to-last, third, and so on.
The provided solution iterates through the dictionary and reorders it to follow this pattern.

## Purpose 🎯

✔ Reorganize the elements of an `OrderedDict` following a custom pattern.  
✔ This is useful in situations where alternating access to the first and last items of a collection is required.

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
OrderedDict([('Name', 'Брусника'),
             ('SeatsCount', '10'),
             ('IsNetObject', 'да'),
             ('Address', 'город Москва, переулок Сивцев Вражек, дом 6/2'),
             ('OperatingCompany', 'Брусника'),
             ('District', 'район Арбат'),
             ('TypeObject', 'кафе'),
             ('AdmArea', 'Центральный административный округ')])
```

## Output Format

-   The output is an `OrderedDict` where the items are rearranged in an alternating pattern starting from the first and last, then second and second-to-last, and so on.

## Usage 📦

To use the function:
1️⃣ Pass an `OrderedDict` to the `change_dict_order()` function.  
2️⃣ The function will return a new `OrderedDict` with the order of elements rearranged as per the specified rule.  
3️⃣ Print the result to see the modified dictionary.

### Example Usage:

```python
data = OrderedDict({
    'Name': 'Брусника', 'IsNetObject': 'да',
    'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
    'SeatsCount': '10'
})
print(change_dict_order(data))
```

## Conclusion 🚀

This code effectively reorders the items of an `OrderedDict` in an alternating pattern, which can be helpful for specific data display or manipulation tasks.
