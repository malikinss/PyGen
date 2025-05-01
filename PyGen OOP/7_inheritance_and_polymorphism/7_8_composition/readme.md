# Lesson 7.8: Composition 🛠️

## Description 📝

This lesson covers:

-   The concept of composition in class design
-   Composition versus inheritance

This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 7 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand composition and its role in object-oriented design  
✅ Compare composition with inheritance for class relationships  
✅ Implement classes using composition for practical scenarios  
✅ Design flexible, modular systems with composed objects

## Concepts & Theory 🔍

### 🔹 Composition

-   **Purpose**: Builds complex objects by combining simpler ones as attributes.
-   **How It Works**: Objects contain instances of other classes to delegate functionality.

### 🔹 Composition and Inheritance

-   **Composition**: "Has-a" relationship, promoting flexibility and loose coupling.
-   **Inheritance**: "Is-a" relationship, useful for shared behavior but tighter coupling.
-   **When to Use**: Composition for modular design; inheritance for hierarchical specialization.

## Practical Task 🧪

### 1️⃣ **Composition-Based Class Design**

The lesson includes 5 practical tasks, each implementing classes using composition:

1. **`Point` and `Circle` Classes**: Geometric objects.

    - `Point`: x, y coordinates; `Circle`: radius and `Point` center.

2. **`Item` and `ShoppingCart` Classes**: E-commerce model.

    - `Item`: name, price; `ShoppingCart`: manages list of `Item` instances.

3. **`Card` and `Deck` Classes**: Card game components.

    - `Card`: suit, rank; `Deck`: manages 52 `Card` instances.

4. **`Queue` Class**: Key-value queue.

    - Uses `deque` to manage key:value pairs with updates and pops.

5. **`Lecture` and `Conference` Classes**: Event scheduling.
    - `Lecture`: topic, time, duration; `Conference`: manages non-overlapping `Lecture` instances.

💡 These tasks showcase composition for building modular, real-world systems.

## Benefits ✅

-   Composition promotes flexible, loosely coupled designs.
-   Modular classes are easier to test and maintain.
-   Composition avoids the complexity of deep inheritance hierarchies.
-   Delegating functionality to composed objects enhances code reuse.

## Output 📜

After completing this lesson, I now:  
✅ Design classes using composition for modular systems  
✅ Compare composition and inheritance for appropriate use cases  
✅ Implement practical examples like shopping carts and conference schedules

## Conclusion 🚀

Mastering composition enables me to create modular, maintainable Python code.  
From geometric circles to conference schedules, composition fosters flexible designs, making complex systems easier to build and extend. 🧑‍💻✨
