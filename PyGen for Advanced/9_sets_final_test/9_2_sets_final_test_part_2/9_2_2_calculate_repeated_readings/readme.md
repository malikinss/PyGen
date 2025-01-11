# Voskhod Satellite Data Analyzer 📡

## Description 📝

The Voskhod satellite transmits solar radiation energy readings every minute to the observatory. To analyze these readings effectively, repeated data must be removed. This program calculates the maximum number of repeated readings in the dataset, helping scientists prepare clean and unique data for further analysis.

## Purpose 🎯

To determine how many redundant readings (repeated data) can be eliminated from the transmitted satellite data, ensuring accurate solar activity analysis.

## How It Works 🔍

1. **Inputs**:
    - A string of space-separated integers, where each integer represents a satellite reading of solar radiation energy.
2. **Logic**:
    - Convert the input list into a set to identify unique readings.
    - Calculate the difference between the total readings and the unique readings:
      \[
      \text{Repeated readings} = \text{Total readings} - \text{Unique readings}
      \]
3. **Output**:
    - The program outputs the maximum number of repeated readings that can be removed.

## Output 📜

The program will output the number of redundant readings that can be eliminated.

### Example:

**Input**:

```
12 15 12 17 15 15 20
```

**Output**:

```
3
```

### Explanation:

-   Total readings: `7`
-   Unique readings: `4` (`12, 15, 17, 20`)
-   Repeated readings: `7 - 4 = 3`

## Usage 📦

1. Copy the code into a Python file, e.g., `satellite_analyzer.py`.
2. Run the script.
3. Provide space-separated integers as input when prompted. Each integer represents a satellite reading.
4. The program will output the number of repeated readings.

### Example Run:

```plaintext
Input: 12 15 12 17 15 15 20
Output: 3
```

## Conclusion 🚀

This program helps scientists clean up redundant satellite readings, ensuring they work with accurate and unique data for analyzing solar activity.
