# Filter Students by Height and Weight 🧑‍🎓

## Description 📝

This program filters a dictionary of students based on specific criteria: students whose height is greater than 167 cm and whose weight is less than 75 kg.
It returns a new dictionary containing only the students who meet these conditions.

## Purpose 🎯

The purpose of this program is to help filter out students from a dataset based on given physical criteria (height and weight).
This functionality can be useful for scenarios that require filtering based on physical attributes.

## How It Works 🔍

1. **Input**:
    - A dictionary `students` where keys are student names (strings), and values are tuples containing their height (in cm) and weight (in kg).
2. **Processing**:
    - The program iterates over the dictionary and selects only those students whose height is greater than 167 cm and whose weight is less than 75 kg.
3. **Output**:
    - A new dictionary containing only the students who meet the height and weight conditions.

## Output 📜

The program outputs a filtered dictionary with students whose height is greater than 167 cm and weight is less than 75 kg.

### Example Input/Output:

**Input**:

```python
students = {
    'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68),
    'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70),
    'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67),
    'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
    'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
    'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80),
    'Mary': (175, 69), 'Jane': (190, 80)
}
```

**Output**:

```python
{
    'Soltan': (192, 68), 'Roman': (175, 70), 'Anna': (172, 67),
    'Mary': (175, 69)
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `filter_students.py`).
2. Call the `filter_students_by_height_and_weight()` function, passing a dictionary of students and their height and weight.
3. The function will return a new dictionary containing only the students who meet the criteria.

### Example Run:

```python
# Sample run
students = {
    'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68),
    'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70),
    'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67),
    'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
    'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
    'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80),
    'Mary': (175, 69), 'Jane': (190, 80)
}
result = filter_students_by_height_and_weight(students)
print(result)
```

**Output**:

```python
{
    'Soltan': (192, 68), 'Roman': (175, 70), 'Anna': (172, 67),
    'Mary': (175, 69)
}
```

## Conclusion 🚀

This program efficiently filters a list of students based on their height and weight, helping you quickly identify those who meet specific physical criteria.
It can be easily adapted to filter other datasets with similar requirements.
