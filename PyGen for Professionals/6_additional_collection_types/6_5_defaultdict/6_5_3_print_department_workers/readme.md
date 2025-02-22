# Group and Display Workers by Department 👥💼

## Description 📝

This program processes employee data from a company, where each tuple contains the department name and the employee's name.
The program groups employees by department, removes duplicates, and displays the departments and their employees in lexicographical order.

## Purpose 🎯

✔ Groups employees by department and removes duplicates.  
✔ Sorts departments and employee names lexicographically.  
✔ Displays the results in the desired format.

## Example Input

```python
staff = [
    ('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'),
    ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'),
    ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
    ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'),
    ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'),
    ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
    ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'),
    ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'),
    ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
    ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'),
    ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'),
    ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
    ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'),
    ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'),
    ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
    ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'),
    ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'),
    ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
    ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'),
    ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'),
    ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
    ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'),
    ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'),
    ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
    ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'),
    ('Sales', 'John White'), ('Sales', 'Marie Cooper'),
    ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
    ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'),
    ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'),
    ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
    ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'),
    ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'),
    ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
    ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'),
    ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'),
    ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
    ('Accounting', 'Dale Houston')
]
```

## Example Output 📜

```
Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, Dale Houston, Edna Cunningham, Gloria Higgins, James Wilkins, Jane Jackson, John Watts, Kay Scott, Kimberly Reynolds, Linda Hudson, Michelle Wright, Rosemary Garcia, Steven Diaz
Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, Thomas Porter, Wilma Woods
Marketing: Andrew Clark, Bernice Ramos, Billy Lloyd, Carol Peters, Charles Bailey, Gail Hill, Helen Taylor, John Gonzalez, Joy Lawrence, Mario Reynolds, Mary King, Ralph Morgan, Sam Davis
Sales: Alicia Mendoza, Chester Fernandez, Charlotte Cox, Connie Reid, Evelyn Martin, Gladys Taylor, John White, Joseph Lee, Jose Taylor, Katie Warner, Marie Cooper, Robert Barnes
```

## Output Format

Departments are displayed first, followed by the names of their employees in lexicographical order, separated by commas.  
Each department is displayed on a new line.

## Usage 📦

To use the program:  
1️⃣ Ensure that the `staff` list contains valid department-employee pairs.  
2️⃣ Run the script to group employees by department and print the results.

### Run the script:

```bash
$ python group_by_department.py
```

## Conclusion 🚀

This program efficiently groups employees by department, removes duplicates, and displays the results sorted lexicographically.
It is a useful tool for organizing and displaying employee data in a structured manner.
