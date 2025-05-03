# Lesson 8.5: Decorators (Part 2) 🎨

## Description 📝

This lesson covers:

-   Decorating classes in Python
-   Practical examples of class decorators

This lesson includes a detailed theoretical explanation, 7 programming practical tasks, and 8 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to decorate classes to modify their structure or behavior  
✅ Implement class decorators for instance tracking, attribute addition, and more  
✅ Apply class decorators to practical scenarios like singletons and naming conventions  
✅ Design flexible, reusable decorators for class customization

## Concepts & Theory 🔍

### 🔹 Decorating Classes

-   **Purpose**: Modify class definitions or behavior at creation time.
-   **How It Works**: Wrap or transform the class using callable objects or functions.

### 🔹 Examples of Class Decorating

-   **Purpose**: Demonstrate real-world applications of class decorators.
-   **Use Cases**: Instance tracking, attribute injection, and behavioral constraints.

## Practical Task 🧪

### 1️⃣ **Class Decorator Implementations**

The lesson includes 7 practical tasks, each implementing a class decorator:

1. **`track_instances` Decorator**: Tracks all class instances.

    - Stores instances in a class-level `instances` list.

2. **`add_attr_to_class` Decorator**: Adds attributes to a class.

    - Uses `setattr` to inject keyword arguments as attributes.

3. **`jsonattr` Decorator**: Adds JSON key-value pairs as class attributes.

    - Parses JSON file and uses `setattr` for attribute injection.

4. **`singleton` Decorator**: Enforces a single class instance.

    - Reuses instance with `object.__new__` for subsequent calls.

5. **`snake_case` Decorator**: Renames methods/attributes to snake case.

    - Converts Camel Case using regex, skips magic methods.

6. **`auto_repr` Decorator**: Adds custom `__repr__` to a class.

    - Formats attributes as values or `name=value` based on input lists.

7. **`limiter` Decorator**: Limits class instances by identifier.
    - Caps instances to `limit`, returns existing instance if exceeded.

💡 These tasks showcase class decorators for dynamic modification and constraint enforcement.

## Benefits ✅

-   Class decorators enable dynamic, reusable class modifications.
-   Simplifies tasks like instance tracking, singletons, and naming conventions.
-   Enhances code maintainability with standardized behaviors.
-   Flexible designs support diverse applications like configuration and debugging.

## Output 📜

After completing this lesson, I now:  
✅ Create class decorators to modify class structure and behavior  
✅ Implement decorators for instance limits, JSON attributes, and more  
✅ Apply class decorators to practical use cases like singletons and auto-repr

## Conclusion 🚀

Mastering class decorators empowers me to customize Python classes dynamically.  
From enforcing singletons to standardizing naming, these tools provide elegant solutions for enhancing class functionality in scalable applications. 🧑‍💻✨
