# License Plate Validator 🚗

## Description 📝

This program validates license plates based on a specific format used by the traffic police. It checks if the given string matches the valid patterns for license plates that consist of Cyrillic letters and digits.

## Purpose 🎯

To ensure that the artificial intelligence used for generating license plates is accurately following the defined pattern.

## How It Works 🔍

1. The program accepts a license plate string.
2. It verifies if the string matches one of the two valid formats:
    - `<LETTER><DIGIT><DIGIT><LETTER><LETTER>_<DIGIT><DIGIT>`
    - `<LETTER><DIGIT><DIGIT><LETTER><LETTER>_<DIGIT><DIGIT><DIGIT>`
3. The valid characters are restricted to certain Cyrillic letters (`АВЭКМНОРСТУХ`) and digits.
4. If the string adheres to the format, the program outputs "YES", otherwise "NO".

## Output 📜

-   "YES" if the input string matches the correct license plate format.
-   "NO" if the input string does not match the format.

## Usage 📦

1. Input a license plate string in the format described above.
2. The program will check if the license plate is valid according to the rules.

### Example 1:

**Input:**  
`А12ВГ_34`

**Output:**  
`YES`

### Example 2:

**Input:**  
`А12БГ_345`

**Output:**  
`YES`

### Example 3:

**Input:**  
`А12ВГ_34А`

**Output:**  
`NO`

## Conclusion 🚀

This program helps verify whether a license plate meets the required format, ensuring consistency and correctness in license plate generation.
