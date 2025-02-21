# Lesson 4.6: Working with `pickle` Files 🐍

## Description 📝

In this lesson, I will explore the `pickle` module, which is used for serializing and deserializing Python objects.
The lesson covers how to store and retrieve Python objects in a binary format, making it easier to save the state of objects between program executions.
I will also work with real-world examples and practical tasks that demonstrate how to serialize dictionaries, functions, and filter data before serialization.

## Purpose 🎯

The goal of this lesson is to help me:

-   Understand the `pickle` module and its use cases for serialization.
-   Learn how to store and retrieve data using `pickle`.
-   Apply `pickle` for more advanced tasks such as deserializing functions and verifying data integrity.

## How It Works 🔍

This lesson is divided into 10 theoretical questions and 4 practical tasks.
The theoretical part explains the `pickle` data format and the workings of the `pickle` module.
The practical tasks guide me through applying `pickle` for serialization and deserialization of Python objects, including dictionaries, functions, and custom objects.

## Output 📜

Upon completing this lesson, I will be able to:

-   Serialize Python objects using `pickle`.
-   Deserialize and execute functions stored in `pickle` files.
-   Filter objects based on type and serialize the filtered data.
-   Calculate and compare checksums for serialized objects to verify data integrity.

## Usage 📦

Follow these steps to complete the tasks:

1. **Task 1: Create Pickle**  
   Write a script that serializes a dictionary containing dog names and ages to a `.pkl` file.  
   Goal: Serialize the `dogs` dictionary and save it as `dogs.pkl` for later use.

2. **Task 2: Call Function from Pickle**  
   Create a script that reads a function from a pickle file, deserializes it, and calls it with arguments provided by the user.  
   Goal: Dynamically execute a function stored in a pickle file and print the result.

3. **Task 3: Filter and Dump**  
   Implement a function `filter_dump()` that filters objects based on their type and serializes the filtered result.  
   Goal: Serialize only objects that match a specified type to a pickle file.

4. **Task 4: Compare and Print Checksum**  
   Write a script that reads an object from a pickle file, calculates its checksum, and compares it with a provided checksum.  
   Goal: Ensure data integrity by verifying the checksum of deserialized objects.

## Conclusion 🚀

By completing this lesson, I will be proficient in using the `pickle` module for serializing and deserializing Python objects.
I will also understand how to dynamically load and execute functions stored in pickle files, filter data before serialization, and verify the integrity of serialized objects through checksum comparisons.
