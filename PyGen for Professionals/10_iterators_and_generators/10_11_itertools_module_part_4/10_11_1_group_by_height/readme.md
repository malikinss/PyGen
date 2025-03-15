# `group_by_height()`: Group People by Height

## Description 📝

The `group_by_height()` function groups a list of `Person` named tuples by their height.  
It then prints the names of individuals in each height group, **sorted alphabetically**, in the specified format.

---

## Purpose 🎯

✔ **Organizing data efficiently** by grouping people based on height.  
✔ **Sorting results properly**:

-   **Ascending order** of height.
-   **Alphabetical order** of names within each height group.  
    ✔ **Using `itertools.groupby`** to process sorted data efficiently.

---

## How It Works 🔍

1. **Sort the list** by height.
2. **Use `groupby()`** to group elements with the same height.
3. **Extract names**, sort them alphabetically, and print the formatted output.

---

## Output 📜

### Example Input

```python
persons = [
    Person('Tim', 63, 193), Person('Eva', 47, 158),
    Person('Mark', 71, 172), Person('Alex', 45, 193),
    Person('Jeff', 63, 193), Person('Ryan', 41, 184),
    Person('Ariana', 28, 158), Person('Liam', 69, 193)
]

group_by_height(persons)
```

### Output

```plaintext
158: Ariana, Eva
172: Mark
184: Ryan
193: Alex, Jeff, Liam, Tim
```

---

## Breakdown 🛠

### Step 1: Sort by Height

```python
sorted(iterable, key=key_func)
```

-   Sorts the `persons` list **by height** in ascending order.

---

### Step 2: Group by Height

```python
grouped = groupby(sorted(iterable, key=key_func), key=key_func)
```

-   `groupby()` groups people with the same height.

---

### Step 3: Sort Names Alphabetically

```python
names = sorted(map(lambda p: p.name, group))
```

-   Extracts names and sorts them **alphabetically**.

---

### Step 4: Print the Results

```python
print(f'{height}: {", ".join(names)}')
```

-   Outputs the grouped and sorted names in the required format.

---

## Usage 📦

This function is useful for **data analysis**, **reporting**, and **categorization** tasks.

```python
people_data = [
    Person('Emma', 30, 165), Person('Noah', 28, 180),
    Person('Olivia', 32, 165), Person('Liam', 25, 180)
]

group_by_height(people_data)
```

**Output:**

```plaintext
165: Emma, Olivia
180: Liam, Noah
```

---

## Conclusion 🚀

The `group_by_height()` function effectively **sorts, groups, and formats** height-based data in a clean and readable way.  
It leverages `groupby()` for efficiency and ensures a well-structured output.
