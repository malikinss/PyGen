# Lesson 7.2: Inheritance (Part 2) 🧬

## Description 📝

This lesson covers:

-   Overriding methods in subclasses
-   Extending methods to enhance inherited behavior
-   The `super()` function for accessing parent class methods
-   Using descendant methods in a base class

This lesson includes a detailed theoretical explanation, 6 programming practical tasks, and 14 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Override and extend methods to customize subclass behavior  
✅ Use `super()` to leverage parent class functionality  
✅ Design base classes that utilize descendant methods  
✅ Apply advanced inheritance techniques to practical scenarios

## Concepts & Theory 🔍

### 🔹 Overriding Methods

-   **Purpose**: Redefines a parent class method in a subclass to alter behavior.
-   **When Used**: To specialize functionality for a specific subclass.

### 🔹 Extending Methods

-   **Purpose**: Enhances inherited methods by combining parent and subclass logic.
-   **How It Works**: Uses `super()` to call the parent method and add new behavior.

### 🔹 The `super()` Function

-   **Purpose**: Accesses parent class methods or constructors.
-   **When Used**: To reuse or extend parent class functionality in subclasses.

### 🔹 Using Descendant Methods in a Base Class

-   **Purpose**: Allows base classes to call methods defined in subclasses.
-   **When Used**: For flexible designs where base classes rely on subclass specialization.

## Practical Task 🧪

### 1️⃣ **Advanced Inheritance Techniques**

The lesson includes 6 practical tasks, each implementing inheritance with method overriding and extension:

1. **`BasicPlan` Hierarchy**: Models subscription plans.

    - `BasicPlan`, `SilverPlan`, `GoldPlan` with tiered attributes.

2. **`WeatherWarning` Hierarchy**: Weather alert system.

    - `WeatherWarning`: Basic alerts; `WeatherWarningWithDate`: Adds date to alerts.

3. **`Triangle` Hierarchy**: Geometric triangles.

    - `Triangle`: General triangle; `EquilateralTriangle`: Single-side initialization.

4. **`DoubledCounter` Class**: Extends `Counter`.

    - Doubles increment/decrement effects while maintaining non-negativity.

5. **`Summator` Hierarchy**: Mathematical summations.

    - `Summator`: Sum of numbers; Subclasses: Sums of squares, cubes, custom powers.

6. **`FieldTracker` Class**: Tracks attribute changes.
    - Methods: `base`, `has_changed`, `changed`, `save` for state tracking.

💡 These tasks demonstrate method overriding, extension, and base class flexibility.

## Benefits ✅

-   Method overriding enables tailored subclass behavior.
-   `super()` facilitates reuse of parent class logic.
-   Extending methods balances inheritance with specialization.
-   Base class use of descendant methods supports flexible designs.

## Output 📜

After completing this lesson, I now:  
✅ Override and extend methods using `super()`  
✅ Design base classes that leverage subclass methods  
✅ Apply advanced inheritance to practical examples like counters and trackers

## Conclusion 🚀

Mastering advanced inheritance techniques with `super()` and method overriding empowers me to create flexible, reusable class hierarchies.  
From subscription plans to attribute tracking, these tools enable sophisticated, extensible designs for complex Python applications. 🧑‍💻✨
