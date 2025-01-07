# Total Students Calculation Program 🎓

## Description 📝

This program calculates the total number of students in the school based on the number of students who visited different places (the seaside, village, and mountains) and those who stayed home to study.

## Purpose 🎯

-   To calculate the total number of students in a school given some specific data about where students went during their holiday break.
-   The calculation ensures that no one visited all three places and that some students stayed at home.

## How It Works 🔍

1. **Inputs**:

    - The number of students who went to the seaside, village, mountains, and the combinations of places (seaside and village, village and mountains).
    - The number of students who stayed home to study.

2. **Function `calculate_total_students`**:

    - It computes the number of students who visited only one of the locations (seaside, village, or mountains).
    - It then adds the students who stayed at home and those who visited two locations.
    - Finally, it calculates the total number of students in the school by summing these values.

3. **Output**:
    - The program outputs the total number of students in the school.

### Example:

```
Input:
Enter the number of students who went to the seaside: 10
Enter the number of students who went to the village: 15
Enter the number of students who went to the mountains: 20
Enter the number of students who went to both the village and seaside: 5
Enter the number of students who went to both the village and mountains: 3
Enter the number of students who stayed at home to study: 7

Output:
45
```

## Output 📜

The program prints the total number of students in the school based on the given inputs. For the example provided, the output is:

```
45
```

## Conclusion 🚀

This program successfully calculates the total number of students in a school, taking into account the students who visited various places during their holidays and those who stayed home to study.
The solution ensures that no one visited all three places and provides an accurate count based on the input data.
