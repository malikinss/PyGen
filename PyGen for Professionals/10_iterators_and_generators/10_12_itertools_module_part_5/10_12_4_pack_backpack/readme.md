# `pack_backpack()`: Find the Optimal Items for a Backpack with Maximum Value

## Description 📝

The `pack_backpack()` function takes a set of items and a backpack's carrying capacity, then determines which items to select to maximize the value of the backpack while ensuring the total weight does not exceed the limit.
The selected items are returned in lexicographical order.

## Purpose 🎯

This function is useful for:  
✔️ **Maximizing the value** of items that can fit within a given weight limit.  
✔️ **Selecting the most valuable items** from a set, without exceeding the backpack's capacity.  
✔️ **Outputting the selected items** in a well-organized and easy-to-read manner.

## How It Works 🔍

1. It iterates through all possible combinations of items in the `items` list.
2. For each combination, it checks whether the total weight of the items exceeds the capacity of the backpack.
3. If the combination is valid, it calculates the total value and updates the best combination if the value is higher than the current maximum.
4. Finally, it returns the **names of the selected items** in lexicographical order or a message stating that the backpack cannot be assembled if no valid combination is found.

## Output 📜

### Example 1: Maximum Value Combination

```python
>>> pack_backpack(items, 3000)
['Гитара', 'Ноутбук', 'Золотая монета']
```

**Explanation**:

-   The function selects the combination of items with the highest value that fits within the weight limit of 3000 grams.
-   In this case, it selects the **Guitar**, **Laptop**, and **Golden Coin**, which have the highest combined value while respecting the weight limit.

### Example 2: No Valid Combination

```python
>>> pack_backpack(items, 10)
['Рюкзак собрать не удастся']
```

**Explanation**:

-   Since the backpack cannot carry any of the available items due to their weight exceeding the capacity, the function returns a message indicating that the backpack cannot be assembled.

### Example 3: Lexicographically Sorted Item Names

```python
>>> pack_backpack(items, 3000)
['Гитара', 'Золотая монета', 'Ноутбук']
```

**Explanation**:

-   The names of the selected items are returned in **lexicographical order** for easy reading and organization.

## Usage 📦

Use `pack_backpack()` when you need to select the **best combination of items** for a backpack without exceeding its weight capacity, and organize the output in lexicographical order.

```python
items = [
    Item('Обручальное кольцо', 7, 49_000),
    Item('Мобильный телефон', 200, 110_000),
    Item('Ноутбук', 2000, 150_000),
    Item('Ручка Паркер', 20, 37_000),
    Item('Статуэтка Оскар', 4000, 28_000),
    Item('Наушники', 150, 11_000),
    Item('Гитара', 1500, 32_000),
    Item('Золотая монета', 8, 140_000),
    Item('Фотоаппарат', 720, 79_000),
    Item('Лимитированные кроссовки', 300, 80_000)
]
result = pack_backpack(items, 3000)
print(result)
# Output: ['Гитара', 'Золотая монета', 'Ноутбук']
```

## Conclusion 🚀

The `pack_backpack()` function is an effective way to determine the optimal selection of items that fit into a backpack while maximizing their combined value.
It returns the names of the selected items in lexicographical order or a message indicating the impossibility of assembling the backpack if no suitable combination is found.
This function is useful for various real-life applications such as optimization problems and inventory management.
