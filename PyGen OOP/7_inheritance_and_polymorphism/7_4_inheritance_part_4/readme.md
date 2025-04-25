Lesson 7.4: inheritance (part 4)

Inheritance from the dict type
Inheritance from the list type
UserDict and UserList types from the collections module
Abstract. The lesson is devoted to inheritance from the dict and list types.

https://stepik.org/lesson/860444/step/1?unit=864459

This lesson has good theory explonation, has 8 programing practical tasks and 14 theoretical questions presented on the website.

1. 7_4_1_DefaultList

```
# DefaultList Class Implementation

## Description 📝

The provided code implements the `DefaultList` class, a subclass of `collections.UserList`.
It represents a list that returns a specified default value when attempting to access an element at a non-existent index.
The class is initialized with two arguments: `iterable` (defining the initial elements, defaulting to an empty tuple) and `default` (the value returned for out-of-bounds indices, defaulting to `None`).
The list is independent of the input iterable, ensuring that changes to the original iterable do not affect the `DefaultList` instance.

## Purpose 🎯

Intended for scenarios where safe index access is needed, such as data processing, user input handling, or dynamic list manipulation, avoiding `IndexError` exceptions.
It’s also suitable for educational examples of list subclassing and custom indexing behavior in Python.
```

2.

```

```

3.

```

```

4.

```

```

5.

```

```

6.

```

```

7.

```

```

8.

```

```
