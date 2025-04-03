# Lesson 4.4: Access Modifiers and Accessors 🔐

## Description 📝

This lesson covers:

-   **Access Modifiers** (public, private, and protected)
-   **Accessor Methods** (Getters and Setters)
-   How to **encapsulate data** and enforce **data integrity** in object-oriented programming.

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand the role of access modifiers in controlling access to class attributes.  
✅ Learn how to use getters and setters to safely access and modify object data.  
✅ Implement access control in practical programming tasks.

## How It Works 🔍

### 🔹 Access Modifiers

Access modifiers determine the visibility of class attributes and methods:

1. **Public (`public`)**

    - Accessible from anywhere.
    - Example:
        ```python
        class Example:
            def __init__(self):
                self.value = 42  # Public attribute
        ```

2. **Protected (`_protected`)**

    - Intended for internal use but still accessible from outside (by convention, not enforced).
    - Example:
        ```python
        class Example:
            def __init__(self):
                self._protected_value = 99  # Conventionally protected attribute
        ```

3. **Private (`__private`)**
    - Not directly accessible from outside the class.
    - Example:
        ```python
        class Example:
            def __init__(self):
                self.__private_value = "secret"  # Private attribute
        ```

### 🔹 Accessor Methods (Getters & Setters)

-   **Getters**: Retrieve the value of a private attribute.
-   **Setters**: Modify the value with validation.

Example:

```python
class User:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):  # Getter
        return self.__name

    def set_name(self, new_name):  # Setter
        if isinstance(new_name, str) and new_name:
            self.__name = new_name
        else:
            raise ValueError("Invalid name!")
```

### 🔹 Practical Applications

-   **Encapsulation**: Protects data from direct modification.
-   **Validation**: Ensures only valid data is set.
-   **Code Maintainability**: Provides a controlled way to interact with data.

---

## Practical Tasks 🖥️

### 1️⃣ **Circle Class Geometry Tool**

📌 Implements a `Circle` class with a private radius attribute.  
🔹 Provides methods to get the radius, diameter, and area.  
🔹 Uses the `math` module for calculations.

### 2️⃣ **BankAccount Class Finance Manager**

📌 Simulates a bank account with deposit, withdraw, and transfer methods.  
🔹 Ensures balance cannot be overdrawn.  
🔹 Demonstrates encapsulation with private balance attribute.

### 3️⃣ **User Class Profile Manager**

📌 Manages user data with strict validation rules.  
🔹 Name must be a non-empty string of Latin or Russian letters.  
🔹 Age must be an integer between 0 and 110.  
🔹 Implements access control using getters and setters.

## Output 📜

By completing this lesson, I will:
✅ Understand access control using public, protected, and private modifiers.  
✅ Learn to implement and use getter and setter methods for safe data access.  
✅ Apply these concepts in real-world scenarios, such as geometry tools, financial applications, and user profile management.

## Conclusion 🚀

This lesson is essential for mastering **data encapsulation** and **object security** in programming.
By using access modifiers and accessor methods correctly, I can create more secure, maintainable, and error-resistant applications.
The provided exercises reinforce these concepts with practical coding tasks. 💡
