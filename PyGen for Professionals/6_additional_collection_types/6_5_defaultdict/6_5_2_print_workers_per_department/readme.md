# Department Employee Count 📊

## Description 📝

This program processes employee data from a company and determines the number of employees in each department.
The data consists of tuples where the first element is the department name, and the second element is the employee’s full name.
The program counts the employees per department and presents the results in lexicographical order.

## Purpose 🎯

✔ Counts the number of employees in each department.  
✔ Sorts departments alphabetically.  
✔ Displays the results in a structured format.

## Example Input

```python
staff = [
    ('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'),
    ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'),
    ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
    ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'),
    ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'),
    ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
    ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'),
    ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'),
    ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
    ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'),
    ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'),
    ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
    ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'),
    ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'),
    ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
    ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'),
    ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'),
    ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
    ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'),
    ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'),
    ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
    ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'),
    ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'),
    ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
    ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')
]
```

## Example Output 📜

```
Accounting: 17
Developing: 7
Marketing: 13
Sales: 10
```

## Output Format

Each department and its employee count are displayed on a separate line in the format:

```
<Department>: <Number of Employees>
```

Departments are sorted in alphabetical order.

## Usage 📦

To use the program:  
1️⃣ Ensure the list `staff` contains valid department-employee pairs.  
2️⃣ Run the script to count employees per department.

### Run the script:

```bash
$ python department_employee_count.py
```

## Conclusion 🚀

This program provides a structured summary of the employee distribution across company departments, making it easy to analyze workforce distribution.
