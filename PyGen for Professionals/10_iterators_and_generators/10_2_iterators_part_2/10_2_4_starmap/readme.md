# `starmap()` Function 📝

## Description 📝

The `starmap()` function applies a function to each unpacked collection element within an iterable.
Unlike the standard `map()` function, where the function is applied to a single element, `starmap()` applies the function to each element of the iterable as separate arguments.

## Purpose 🎯

The goal of `starmap()` is to allow the application of a function that takes multiple arguments to elements of an iterable, where each element itself is a collection (such as a tuple or list).

## How It Works 🔍

1. **Unpacking the Collections**:

    - `zip(*collections)` is used to transpose the iterable of collections. This means it combines the corresponding elements from each collection into tuples. For example, if `collections` is a list of tuples, `zip(*collections)` will create tuples where the first tuple contains all the first elements from each collection, the second tuple contains all the second elements, and so on.

2. **Applying the Function**:
    - The `map()` function is used to apply the provided function (`function`) to each unpacked tuple of elements from the collections. Each tuple now represents the individual elements that were previously inside the collections.
3. **Return an Iterator**:
    - The result of `map()` is returned as an iterator, which can be converted to a list or used in a loop to retrieve the results.

## Example Usage 📦

In the example provided:

```python
persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
full_names = starmap(lambda name, surname: f'{name} {surname}', persons)

print(list(full_names))  # Output: ['Timur Guev', 'Arthur Kharisov']
```

-   `zip(*persons)` transposes the list of tuples `persons`, resulting in the following structure: `[('Timur', 'Arthur'), ('Guev', 'Kharisov')]`.
-   The lambda function is then applied to each pair of elements: `'Timur'` and `'Arthur'` for the first tuple, and `'Guev'` and `'Kharisov'` for the second tuple, resulting in `['Timur Guev', 'Arthur Kharisov']`.

## Output 📜

The output of the code is:

```
['Timur Guev', 'Arthur Kharisov']
```

This is the result of applying the lambda function `lambda name, surname: f'{name} {surname}'` to the corresponding elements in each tuple.

## Conclusion 🚀

The `starmap()` function is an efficient and elegant way to apply a function to the unpacked elements of collections inside an iterable.
It simplifies scenarios where a function requires multiple arguments, and each argument is contained within a collection.
