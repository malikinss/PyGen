Chapter 5: Magical methods

This chapter separated on 11 lessons that have good theory explonation, 46 practical programming tasks and 131 theoretical questions presented on the course website.

5_magical_methods
├───5_1_objects_creation_initialization_clearing
├───5_2_objects_string_representation
├───5_3_objects_comparison
├───5_4_unary_operators_anf_functions
├───5_5_arithmetic_operations
├───5_6_callable_objects
├───5_7_type_conversion
├───5_8_working_with_object_attributes
├───5_9_object_hashing_part_1
├───5_10_object_hashing_part_2
└───5_11_dicr_and_set_features_of_work

1. 5_1_objects_creation_initialization_clearing

```
# Lesson 5.1: Creation, Initialization, and Clearing of Objects 🛠️
This lesson covers:
-   Magic methods in Python
-   The **`new()`** and **`init()`** magic methods
-   Singleton design pattern implementation
-   The **`del()`** magic method for object deletion
By the end of this lesson, I will:
✅ Understand how Python creates and initializes objects using `new()` and `init()`
✅ Implement the **Singleton** pattern to ensure a class has only one instance
✅ Learn how to manage object lifecycle using `del()`
✅ Be able to apply these concepts to optimize code for object creation and clearing
```

2. 5_2_objects_string_representation

```
# Lesson 5.2: String Representation of Objects 📜
This lesson covers:
-   Functions **`str()`** and **`repr()`** in Python
-   Magic methods **`__str__()`** and **`__repr__()`**
-   Formal and informal string representations of objects
-   Practical implementation across various classes
This lesson includes a detailed theoretical explanation, 6 programming practical tasks, and 11 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand the difference between **`str()`** and **`repr()`** functions
✅ Implement **`__str__()`** and **`__repr__()`** magic methods for custom string representations
✅ Learn to create formal (developer-friendly) and informal (user-friendly) object descriptions
✅ Apply these concepts to real-world class examples for better object management
```

3. 5_3_objects_comparison

```
# Lesson 5.3: Comparison of Objects ⚖️
This lesson covers:
-   Magic methods **`__eq__()`** and **`__ne__()`** for equality and inequality
-   The **`NotImplemented`** constant for unsupported comparisons
-   Magic methods **`__lt__()`** and **`__gt__()`** for less than and greater than
-   Magic methods **`__le__()`** and **`__ge__()`** for less than or equal and greater than or equal
-   The **`@total_ordering`** decorator for complete comparison support
-   Practical implementation of object comparison
This lesson includes a detailed theoretical explanation, 4 programming practical tasks, and 14 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to implement object comparison using magic methods
✅ Use **`NotImplemented`** to handle invalid comparison cases
✅ Apply **`@total_ordering`** to simplify comparison logic
✅ Be able to compare objects in practical scenarios like vectors, words, dates, and versions
```

4. 5_4_unary_operators_anf_functions

```
# Lesson 5.4: Unary Operators and Functions ➕➖
This lesson covers:
-   Magic methods **`__pos__()`**, **`__neg__()`**, and **`__invert__()`** for unary operators
-   Magic methods **`__abs__()`**, **`__round__()`**, and similar functions
-   Practical implementation of unary operations on objects
This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 8 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to implement unary operators using magic methods
✅ Use **`__abs__()`** and **`__round__()`** to extend object functionality
✅ Apply unary operations to manipulate objects in practical scenarios
✅ Be able to overload operators for custom behavior in classes
```

5. 5_5_arithmetic_operations

```
# Lesson 5.5: Arithmetic Operations 🧮
This lesson covers:
-   Magic methods **`__add__()`**, **`__sub__()`**, and **`__mul__()`** for basic arithmetic
-   Magic methods **`__truediv__()`**, **`__floordiv__()`**, and **`__mod__()`** for division and modulo
-   Reflected arithmetic operations (e.g., handling `scalar * obj`)
-   In-place magic methods **`__iadd__()`**, **`__isub__()`**, **`__imul__()`**, **`__itruediv__()`**, **`__ifloordiv__()`**, and **`__imod__()`**
-   Practical implementation of arithmetic operations on objects
This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 14 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to implement arithmetic operations using magic methods
✅ Handle reflected arithmetic for flexible operand ordering
✅ Use in-place operations for efficient object updates
✅ Apply arithmetic operations to practical scenarios like nutrition, vectors, and queues
```

6. 5_6_callable_objects

```
# Lesson 5.6: Callable Objects 📞
This lesson covers:
-   Callable objects in Python
-   Magic method **`__call__()`** for enabling object invocation
-   Practical implementation of callable objects and decorators
This lesson includes a detailed theoretical explanation, 10 programming practical tasks, and 7 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to make objects callable using **`__call__()`**
✅ Create callable objects for diverse tasks like arithmetic, formatting, and sorting
✅ Use callable objects as decorators for function enhancement
✅ Apply these concepts to simplify code and improve functionality
```

7. 5_7_type_conversion

```
# Lesson 5.7: Type Conversion 🔄
This lesson covers:
-   Magic method **`__bool__()`** for boolean conversion
-   Magic methods **`__int__()`**, **`__float__()`**, and **`__complex__()`** for numeric conversions
-   Practical implementation of type conversion for objects
This lesson includes a detailed theoretical explanation, 3 programming practical tasks, and 8 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to implement type conversion using magic methods
✅ Enable objects to behave like booleans and numbers in different contexts
✅ Apply type conversion to practical scenarios like vectors, temperatures, and Roman numerals
```

8. 5_8_working_with_object_attributes

```
# Lesson 5.8: Working with Object Attributes 🔧
This lesson covers:
-   Attribute operations in Python
-   Magic methods **`__getattribute__()`** and **`__getattr__()`** for attribute access
-   Magic method **`__setattr__()`** for attribute modification
-   Magic method **`__delattr__()`** for attribute deletion
This lesson includes a detailed theoretical explanation, 8 programming practical tasks, and 6 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand how to control attribute access, modification, and deletion
✅ Implement custom attribute behavior using magic methods
✅ Apply attribute operations to create flexible, secure, and dynamic objects
✅ Use these techniques in practical scenarios like logging, immutability, and access control
```

9. 5_9_object_hashing_part_1

```
# Lesson 5.9: Object Hashing (Part 1) 🔢
This lesson covers:
-   Hashing and its role in Python
-   Applications of hashing in data structures
-   Built-in function **`hash()`**
-   Narrowing the range of hash values
-   Characteristics of a good hash function
-   Creating custom hash functions
This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and 21 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand the concept of hashing and its applications
✅ Use the built-in **`hash()`** function effectively
✅ Create custom hash functions with specific properties
✅ Apply hashing techniques to constrain hash values within a range
```

10. 5_10_object_hashing_part_2

```
# Lesson 5.10: Object Hashing (Part 2) 🔢
This lesson covers:
-   Hashability and immutability in Python
-   Hashing custom classes
-   Magic method **`__hash__()`** for custom hash values
-   The hash-equal contract for consistent object behavior
This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and 11 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand the relationship between hashability and immutability
✅ Implement custom hashing for classes using **`__hash__()`**
✅ Ensure the hash-equal contract for consistent object behavior
✅ Apply hashing to create hashable objects for sets and dictionaries
```

11. 5_11_dicr_and_set_features_of_work

```
# Lesson 5.11: Features of Dictionaries and Sets 📚
This lesson covers:
-   Features of dictionaries and sets in Python
-   Performance characteristics and memory consumption
-   Handling mutable keys and their implications
-   Pitfalls and downsides of dictionary and set implementations
This lesson includes a detailed theoretical explanation and 10 theoretical questions available on the Stepik platform.
By the end of this lesson, I will:
✅ Understand the internal workings of dictionaries and sets
✅ Recognize factors affecting their performance and memory usage
✅ Identify risks associated with mutable keys
✅ Be aware of common pitfalls and implementation limitations
```
