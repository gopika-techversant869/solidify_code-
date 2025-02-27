#Single Responsibility Principle
"""A class should have only one responsibility.
If a class handles multiple tasks, it increases coupling and wastes memory by loading unnecessary methods.

After applying SRP, we split it into:

    Employee → Holds only instance data (lightweight).
    EmployeeDatabase → Manages saving to the database.
    EmployeeReport → Generates reports separately.

Memory Benefit: Since only relevant objects are created at runtime, unused functionalities don’t consume memory, making garbage collection more efficient. """


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDatabase:
    def save(self, employee):
        print(f"Saving {employee.name}'s data to the database...")

class EmployeeReport:
    def generate(self, employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"

# Creating an Employee object
emp = Employee("Alice", 50000)

# Using EmployeeDatabase to save the employee
db = EmployeeDatabase()
db.save(emp)  

# Using EmployeeReport to generate a report
report = EmployeeReport()
print(report.generate(emp)) 
