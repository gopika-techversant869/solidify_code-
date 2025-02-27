class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDatabase:  # Directly depends on Employee 
    def save(self, employee):
        print(f"Saving {employee.name}'s data to the database...")

class EmployeeReport:  # Directly depends on Employee 
    def generate(self, employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"


emp = Employee("Alice", 50000)

db = EmployeeDatabase()
db.save(emp)

report = EmployeeReport()
print(report.generate(emp))
