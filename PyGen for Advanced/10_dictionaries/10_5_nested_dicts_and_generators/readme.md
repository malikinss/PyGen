# Lesson 10.5: Nested Dicts and Dictionary Comprehensions

## Description 📝

This section covers nested dictionaries and dictionary comprehensions (generators). It provides practical exercises for manipulating dictionaries by filtering, transforming, and generating new dictionary structures using various Python techniques. The examples range from basic dictionary manipulations to more complex use cases involving filtering, key-value swaps, and tuple transformations.

## Purpose 🎯

-   Learn how to manipulate nested dictionaries.
-   Understand how to filter dictionary items based on specific conditions.
-   Master the use of dictionary comprehensions and generator expressions.

---

### 1. 10_5_1_get_squared_numbers

```
This program generates a dictionary where the key is the position (index) of a number in the input list, and the value is the square of that number. The dictionary is created using a generator expression, which efficiently iterates through the list of numbers.The purpose of this program is to demonstrate how to use a generator expression to build a dictionary from a list of numbers. It helps understand how to map list indices to corresponding squared values.
```

---

### 2. 10_5_2_filter_colors

```
This program filters out the key-value pairs from a dictionary where the value is `None`.
It produces a new dictionary that only contains the entries where the value is a valid color name.
The purpose of this program is to demonstrate how to filter a dictionary using a generator expression, removing entries with a `None` value.
This is useful in cases where you need to clean up data by eliminating invalid or missing values.
```

---

### 3. 10_5_3_filter_favorite_numbers

```
This program filters out entries from a dictionary of favorite numbers, keeping only the ones where the values are two-digit numbers (between 10 and 99 inclusive).
The purpose of this program is to demonstrate how to filter a dictionary based on a condition (two-digit numbers) using a generator expression inside a dictionary comprehension.
```

---

### 4. 10_5_4_swap_months

```
This program swaps the keys and values of a dictionary where the keys are integers representing the months (1 to 12), and the values are the corresponding month names.
The output is a new dictionary where the month names become the keys and their respective numbers become the values.
The goal of this program is to demonstrate how to manipulate a dictionary by swapping its keys and values using a dictionary comprehension.
```

---

### 5. 10_5_5_parse_string_to_dict

```
This program takes a string of space-separated `number:word` pairs and converts it into a dictionary. The numbers from the string become the dictionary keys (as integers), and the corresponding words become the values (as strings).
The purpose of this program is to demonstrate how to parse and process a string of number:word pairs and convert it into a dictionary format suitable for further usage.
```

---

### 6. 10_5_6_find_divisors

```
This program takes a list of integers and returns a dictionary where each integer is a key, and the value is a sorted list of its divisors in ascending order, starting with 1.
The purpose of this program is to generate a dictionary where each number from a list is associated with its divisors. The divisors are listed in ascending order, which can be useful in a variety of mathematical and computational problems.
```

---

### 7. 10_5_7_get_ascii_codes

```
This program takes a list of words and returns a dictionary where each word is associated with a list of ASCII codes corresponding to the characters of that word.
The purpose of this program is to provide a simple way to convert words into their ASCII code representations. This can be useful in encoding, encryption, or various text processing tasks.
```

---

### 8. 10_5_8_filter_letters

```
This program takes a dictionary of letter mappings and a list of keys to be removed.
It then returns a new dictionary with the entries whose keys are not in the list of keys to be excluded.
The purpose of this program is to provide an easy way to filter out specific key-value pairs from a dictionary.
It can be useful for tasks that require removing unwanted entries from a dictionary based on certain conditions.
```

---

### 9. 10_5_9_filter_students_by_height_and_weight

```
This program filters a dictionary of students based on specific criteria: students whose height is greater than 167 cm and whose weight is less than 75 kg.
It returns a new dictionary containing only the students who meet these conditions.
The purpose of this program is to help filter out students from a dataset based on given physical criteria (height and weight).
This functionality can be useful for scenarios that require filtering based on physical attributes.
```

---

### 10. 10_5_10_generate_tuple_dict

```
This program takes a list of tuples where each tuple contains three integers.
It generates a dictionary where the key is the first element of each tuple, and the value is a tuple of the remaining two elements.
The purpose of this program is to demonstrate how to transform a list of tuples into a dictionary, where the first element of each tuple becomes the key, and the remaining two elements form the value.
```

---

### 11. 10_5_11_generate_student_info

```
This program takes three lists — `student_ids`, `student_names`, and `student_grades` — containing information about students.
It generates a list of nested dictionaries where each dictionary contains the student ID as the key and another dictionary containing the student's name and grade as the value.
The purpose of this program is to convert three parallel lists into a structured list of dictionaries, making it easier to look up student information by ID.
```

---

**Usage 📦**

1. Run the programs in a Python environment.
2. Follow the prompts to input data as required by each program.
3. Observe the results and explore how dictionaries are transformed based on the operations described.

**Conclusion 🚀**  
By the end of this section, you'll have learned how to manipulate dictionaries with advanced techniques, including filtering, swapping keys and values, and applying generator expressions.
