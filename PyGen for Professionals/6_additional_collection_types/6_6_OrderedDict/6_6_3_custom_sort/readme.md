# Custom Sorting of an OrderedDict 📑

## Description 📝

This project includes a function `custom_sort()` that modifies an `OrderedDict` by sorting its items either by keys or by values, based on the boolean argument `by_values`.
The dictionary is sorted **in place**, meaning no new dictionary is returned, and the original dictionary is directly modified.

## Purpose 🎯

The purpose of the `custom_sort()` function is to allow sorting of an `OrderedDict` either by its keys or by its values while preserving the original order of equal elements.

## How It Works 🔍

1. **Initialization:**  
   The function `custom_sort()` takes an `OrderedDict` and a boolean `by_values` as input. The `OrderedDict` is a special dictionary that maintains the order of the items as they are added.

2. **Clearing the Dictionary:**  
   Before sorting, the dictionary is cleared using `ordered_dict.clear()`. This removes all elements so that the dictionary can be refilled after sorting.

3. **Sorting Logic:**

    - If `by_values` is **`False`**, the dictionary is sorted by **keys**.

        - Sorting is done using `sorted(ordered_dict.items(), key=lambda item: item[0])`, where `item[0]` refers to the key.
        - The `OrderedDict` is updated with the sorted items.

    - If `by_values` is **`True`**, the dictionary is sorted by **values**.
        - Sorting is done using `sorted(ordered_dict.items(), key=lambda item: item[1])`, where `item[1]` refers to the value.
        - The `OrderedDict` is updated with the sorted items.

4. **Preserving Order for Equal Items:**  
   The function respects the original order of elements when their keys or values are equal. Python's `sorted()` function is stable, meaning it preserves the relative order of equal items.

## Output 📜

The function does not return anything. It modifies the `OrderedDict` passed to it **in place**.

## Usage 📦

1. Create an `OrderedDict`:

    ```python
    from collections import OrderedDict
    data = OrderedDict({
        'Dustin': 29,
        'Anabel': 17,
        'Brian': 40,
        'Carol': 16
    })
    ```

2. Call the `custom_sort()` function:
    - **Sort by Keys**:
        ```python
        custom_sort(data, by_values=False)
        print(data)
        ```
    - **Sort by Values**:
        ```python
        custom_sort(data, by_values=True)
        print(data)
        ```

## Conclusion 🚀

The `custom_sort()` function is an efficient tool for sorting `OrderedDict` objects by either keys or values, allowing for flexibility while ensuring the order of equal elements is preserved.
