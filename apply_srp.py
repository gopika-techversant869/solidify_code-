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
