# Pickle Checksum Verifier 📝

## Description 📝

This program reads a serialized object (either a dictionary or list) from a pickle file, calculates its checksum according to specified rules, and compares it with a provided checksum. The checksum is calculated as:

1. For a dictionary: the sum of all integer keys.
2. For a list: the product of the minimum and maximum integer elements.

## Purpose 🎯

The purpose of this program is to verify the integrity of data received over a communication channel by comparing the checksum of the deserialized object with a provided value. This ensures that the object has not been altered during transmission.

## How It Works 🔍

1. The program receives the path to a pickle file and an expected checksum value.
2. The object in the pickle file (either a dictionary or a list) is deserialized.
3. Depending on the type of the object (dictionary or list), the checksum is calculated:
    - For a dictionary: the sum of all integer keys is computed.
    - For a list: the product of the minimum and maximum integer elements is calculated.
4. The program compares the calculated checksum with the expected checksum.
5. If they match, it prints "Checksums match", otherwise, it prints "Checksums do not match".

## Output 📜

The output is either "Checksums match" or "Checksums do not match", based on whether the calculated checksum matches the provided expected checksum.

### Example:

**Input:**

```text
Enter pickle file path: data.pkl
Enter expected checksum: 15
```

**Output:**

```text
Checksums match
```

If the checksums do not match:

```text
Checksums do not match
```

## Usage 📦

1. The program reads the path of the pickle file and the expected checksum from the user input.
2. The pickle file should contain a dictionary or list with integer keys or elements.
3. The checksum is calculated and compared to the expected checksum, and the result is printed.

## Conclusion 🚀

This program helps ensure that transmitted data has not been tampered with by calculating and comparing checksums, making it ideal for verifying the integrity of serialized data.
