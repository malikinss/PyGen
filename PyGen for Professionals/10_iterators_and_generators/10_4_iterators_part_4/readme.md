# Lesson 10.4: Iterators (Part 4) 📝

## Description 📝

In this lesson, I dive into creating custom iterators in Python using **class definitions**.
This lesson introduces how to build iterators from scratch, adhering to the **iterator protocol**.
I learn to define the necessary methods to create my own iterator objects and customize them for various use cases.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Learn how to create my own iterators by writing custom iterator classes.  
✅ Understand the **iterator protocol** that requires the implementation of `__iter__()` and `__next__()` methods.  
✅ Gain the ability to use these custom iterators in real-world scenarios.  
✅ Explore common use cases like infinite loops, bounded repetitions, mathematical sequences, and more.

## How It Works 🔍

This lesson covers the following topics:

1. **Iterator and Iterable Object Protocol**: An iterator must implement `__iter__()` and `__next__()`. The `__iter__()` method returns the iterator object itself, and `__next__()` returns the next item. When the sequence is exhausted, `StopIteration` is raised.
2. **`__init__()` Magic Method**: This method is used to initialize the attributes of the custom iterator, such as the sequence to iterate over or the range for iteration.
3. **Creating Your Own Iterators**: I will define several iterators based on real-world needs, such as generating Fibonacci numbers, cycling through letters, or even simulating a deck of cards.

This lesson includes 11 practical tasks to build and understand different custom iterators. Here are some of them:

1.  **10_4_1_Repeater**  
    **Goal**: Create an iterator that endlessly returns the same object.

-   This is useful in testing, simulations, or when you need a constant value to repeat indefinitely.

2.  **10_4_2_BoundedRepeater**  
    **Goal**: Create an iterator that repeats an object a limited number of times and then stops.

-   This is helpful in scenarios like generating test data or limited loops.

3.  **10_4_3_Square**  
    **Goal**: Create an iterator that generates the squares of the first `n` natural numbers.

-   This is useful for mathematical operations or generating a sequence of squares for data processing.

4.  **10_4_4_Fibonacci**  
    **Goal**: Create an infinite Fibonacci sequence iterator.

-   Ideal for situations where Fibonacci numbers are needed but storing the entire sequence is not efficient.

5.  **10_4_5_PowerOf**  
    **Goal**: Create an iterator that generates infinite powers of a number.

-   This is useful when needing an ongoing sequence of powers without precomputing them.

6.  **10_4_6_DictItemsIterator**  
    **Goal**: Create an iterator that iterates over a dictionary’s key-value pairs without using `items()`, `keys()`, or `values()`.

-   This teaches me how to manually iterate through a dictionary while keeping the original order.

7.  **10_4_7_CardDeck**  
    **Goal**: Create an iterator that generates a sequence of 52 playing cards in a specific order.

-   This is helpful for card games or simulations where I need to work with a deck of cards.

8.  **10_4_8_Cycle**  
    **Goal**: Create an iterator that cycles through the elements of a sequence indefinitely.

-   This can be useful for looping over a fixed set of values repeatedly.

9.  **10_4_9_RandomNumbers**  
    **Goal**: Create an iterator that generates a sequence of random numbers within a given range.

-   This is essential for applications like simulations, random sampling, or games.

10. **10_4_10_Alphabet**  
    **Goal**: Create an iterator that generates a cyclic sequence of letters from the English or Russian alphabet.

-   This is useful in educational applications, games, or any scenario where letters need to be generated cyclically.

11. **10_4_11_Xrange**  
    **Goal**: Create an iterator that generates a sequence of numbers with a specific interval, either positive or negative.

-   This is similar to Python's built-in `range()`, but it also supports floating-point numbers.

## Output 📜

After completing this lesson, I will:  
✅ Be able to create my own custom iterators using class definitions.  
✅ Understand and implement the **iterator protocol**.  
✅ Solve various problems using custom iterators like repeating values, generating sequences, and simulating complex data structures.

## Conclusion 🚀

Custom iterators give me full control over how sequences are generated and iterated in Python.
By mastering how to create them, I gain a powerful tool for efficient data processing, mathematical operations, and simulation tasks.
This knowledge is essential for tasks requiring infinite sequences, cyclic behaviors, and controlled iteration, making me more proficient in writing Python code.
