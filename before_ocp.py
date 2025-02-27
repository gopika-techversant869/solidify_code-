
 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDatabase:
    def save(self, employee: Employee):
        print(f"Saving {employee.name}'s data to the database...")

class EmployeeReport:
    def generate(self, employee, report_type):
        if report_type == "text":
            return f"Employee Report: {employee.name}, Salary: {employee.salary}"
        elif report_type == "pdf":
            return f"[PDF] Employee Report: {employee.name}, Salary: {employee.salary}"
        elif report_type == "csv":
            return f"CSV Format: {employee.name}, {employee.salary}"
        else:
            raise ValueError("Invalid report type")


emp = Employee("Alice", 50000)


emp_report = EmployeeReport()
print(emp_report.generate(emp,"text"))





