Lesson 10.11: `itertools` module (part 4)

https://stepik.org/lesson/674986/step/1?unit=673426

Lesson Topic: itertools module
The groupby() function
Examples of using the groupby() function
Abstract. The lesson is devoted to studying the groupby() function of the itertools module.

This lesson has good theory explonation, 6 programing practical tasks and 8 theoretical questions presented on the website.

10_11_itertools_module_part_4
├───10_11_1_group_by_height
├───10_11_2_most_popular_student_name
├───10_11_3_group_by_word_len
├───10_11_4_get_structured_tasks
├───10_11_5_group_anagrams
└───10_11_6_ranges

1. 10_11_1_group_by_height

```
# `group_by_height()`: Group People by Height
The `group_by_height()` function groups a list of `Person` named tuples by their height.
It then prints the names of individuals in each height group, **sorted alphabetically**, in the specified format.
✔ **Organizing data efficiently** by grouping people based on height.
✔ **Sorting results properly**:
-   **Ascending order** of height.
-   **Alphabetical order** of names within each height group.
    ✔ **Using `itertools.groupby`** to process sorted data efficiently.
```

2. 10_11_2_most_popular_student_name

```
# `most_popular_student_name()` - Find the Most Common First Name
The function `most_popular_student_name()` returns the most common first name among the students in the provided list of `Student` named tuples.
✔ **Find the most frequent first name** in a list of students.
✔ **Efficient grouping** of students based on first name.
✔ **Handles the case where the name is unique**.

```

3. 10_11_3_group_by_word_len

```
# `group_by_word_len()` - Group Words by Length
The function `group_by_word_len()` receives a sequence of lowercase Latin words, groups them by their length, and prints them in increasing order of length.
Each group contains words sorted alphabetically.
✔ **Groups words** based on their length.
✔ **Sorts words alphabetically** within each group.
✔ **Prints the groups** in order of increasing length.
```

4. 10_11_4_get_structured_tasks

```
# `get_structured_tasks()` - Display Tasks and Actions
The `get_structured_tasks()` function processes a list of tasks with their respective actions and orders, then displays them in alphabetical order of the task name.
Each task is listed with its corresponding actions, ordered by their respective sequence numbers.
✔ **Sorts tasks alphabetically** by name.
✔ **Groups actions** by task, sorting actions by their order.
✔ **Prints tasks and actions** in a formatted structure.
```

5. 10_11_5_group_anagrams

```
# `group_anagrams()` - Group Words that are Anagrams
The `group_anagrams()` function takes a list of words and groups the words that are anagrams into tuples.
It then returns a list of these tuples.
The order of the tuples and the order of the words within each tuple do not matter.
✔ **Groups anagram words** into tuples.
✔ **Returns a list** of tuples containing words that are anagrams of each other.
✔ **Handles any number of words** in the input list.
```

6. 10_11_6_ranges

```
# `ranges()` - Convert Numbers into Segments
The `ranges()` function takes a sorted list of distinct natural numbers and transforms consecutive numbers into segments.
Each segment is represented as a tuple, where the first element is the left border and the second is the right border.
✔ **Groups consecutive numbers** into segments.
✔ **Preserves the original order** of numbers in the input list.
✔ **Handles single numbers correctly** by treating them as segments with identical borders.
```
