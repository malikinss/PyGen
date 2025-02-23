# Lesson 6.10: ChainMap Data Type (Part 2) 📚

## Description 📝

In this lesson, I will continue exploring the **ChainMap** data type from Python’s **collections module**.
This lesson delves into advanced features of **ChainMap**, including its **maps** and **parents** attributes, and the **new_child()** method.
I will learn how to update, retrieve, and manage data across multiple dictionaries grouped in a **ChainMap**.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand how to use the **maps** and **parents** attributes of a **ChainMap**.
-   Learn how to create a child **ChainMap** with the **new_child()** method.
-   Learn how to perform deep updates and retrieve values efficiently in a **ChainMap**.

## How It Works 🔍

This lesson includes 3 practical tasks that apply the concepts learned:

1. **ChainMap Value Retriever 📝**

    - **Objective:** This program defines a function `get_all_values()` that retrieves all values associated with a specific key from all the dictionaries in a **ChainMap**.
    - **Use:** The function returns a set of all values associated with a specific key across multiple dictionaries. If the key doesn’t exist, an empty set is returned.

2. **ChainMap Deep Update 📝**

    - **Objective:** This program defines a function `deep_update()` that updates all occurrences of a key across all dictionaries in the **ChainMap**. If the key doesn’t exist, it adds the key-value pair to the first dictionary.
    - **Use:** The function ensures consistency by updating the key-value pair across all dictionaries, and if missing, it adds the key-value pair to the first dictionary in the **ChainMap**.

3. **ChainMap Key Retrieval 📝**
    - **Objective:** This program defines a function `get_value()` that retrieves the value associated with a key from a **ChainMap**. The search direction can be controlled by the `from_left` argument, determining whether the search starts from the first or last dictionary.
    - **Use:** This function provides flexibility in searching for a key and returns `None` if the key is not found. The search can go in either direction based on the `from_left` parameter.

## Output 📜

After completing these tasks, I will be able to:  
✅ Retrieve all values for a specific key across multiple dictionaries in a **ChainMap**.  
✅ Perform deep updates to modify values across dictionaries within the **ChainMap**.  
✅ Efficiently search for a key in a **ChainMap** with flexible search directions.

## Conclusion 🚀

In this lesson, I have learned how to manage and manipulate data in a **ChainMap** using its advanced features.
By using the **maps** and **parents** attributes and the **new_child()** method, I can create more complex and flexible data structures.
These techniques allow me to efficiently retrieve and update values in a **ChainMap**, making it a valuable tool for managing multiple contexts in Python.
