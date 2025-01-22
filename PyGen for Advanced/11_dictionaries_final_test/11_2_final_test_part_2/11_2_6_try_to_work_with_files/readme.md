# File Access Rights Control 📝

## Description 📝

This program restores file access rights control after a virus has broken the system.
The program verifies user requests to perform actions (Read, Write, or Execute) on files, ensuring that only allowed actions are executed based on the file’s access rights. For each request, the program returns either `OK` if the action is allowed or `Access denied` if it is not.

## Purpose 🎯

The purpose of this program is to simulate file access rights control in a file system, allowing the verification of user actions (Read, Write, Execute) on files based on their assigned access rights.

## How It Works 🔍

1. **Input**:
    - The program first reads the number of files and their access rights from the user.
    - Then, it reads the number of user requests, each specifying an action and a filename.
2. **Processing**:
    - The program builds a dictionary to store the files and their access rights.
    - It then processes each user request by checking if the requested action is allowed for the specified file.
3. **Output**:
    - For each request, the program returns `OK` if the action is allowed, or `Access denied` if the action is not permitted.

## Output 📜

The output consists of the result for each request:

-   `OK`: The requested action is allowed for the file.
-   `Access denied`: The requested action is not allowed for the file.

### Example Input/Output:

**Input**:

```
3
file1 read write
file2 write execute
file3 read execute
4
read file1
write file2
execute file3
execute file1
```

**Output**:

```
OK
OK
OK
Access denied
```

### Explanation:

-   For `read file1`, file1 has `read` and `write` rights, so the action is allowed.
-   For `write file2`, file2 has `write` and `execute` rights, so the action is allowed.
-   For `execute file3`, file3 has `read` and `execute` rights, so the action is allowed.
-   For `execute file1`, file1 does not have `execute` rights, so the action is denied.

## Usage 📦

1. Copy the code into a Python file (e.g., `access_control.py`).
2. Input the number of files and their access rights.
3. Input the number of requests followed by the requested action and filename.
4. The program will output either `OK` or `Access denied` for each request.

### Example Run:

```python
# Input:
3
file1 read write
file2 write execute
file3 read execute
4
read file1
write file2
execute file3
execute file1

# Output:
OK
OK
OK
Access denied
```

## Conclusion 🚀

This program provides a simple way to simulate file access control, verifying whether specific actions are allowed based on the file's permissions. It can be useful for understanding file system security and simulating access rights management in various environments.
