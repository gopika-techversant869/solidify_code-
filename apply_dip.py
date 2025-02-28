
"""
------------------Dependency Inversion Principle (DIP)---------------------------------------
High-level modules should not depend on low-level modules. Both should depend on abstractions"""

from abc import ABC, abstractmethod

# Step 1: Create an abstraction for storage
class EmployeeStorage(ABC):  # Interface
    @abstractmethod
    def save(self, employee):
        pass

# Step 2: Implement storage options
class DatabaseStorage(EmployeeStorage):  
    def save(self, employee):
        print(f"Saving {employee.name}'s data to the database...")

class FileStorage(EmployeeStorage):  
    def save(self, employee):
        print(f"Saving {employee.name}'s data to a file...")

# Step 3: Create an abstraction for report generation
class ReportGenerator(ABC):  # Interface
    @abstractmethod
    def generate(self, employee):
        pass

# Step 4: Implement different report formats
class TextReport(ReportGenerator): 
    def generate(self, employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"

class PDFReport(ReportGenerator): 
    def generate(self, employee):
        return f"[PDF] Employee Report: {employee.name}, Salary: {employee.salary}"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Step 6: EmployeeService uses abstractions instead of concrete classes
class EmployeeService:
    def __init__(self, storage, report):
        self.storage = storage
        self.report = report

    def save_employee(self, employee):
        self.storage.save(employee)

    def generate_report(self, employee):
        return self.report.generate(employee)

# Step 7: Use abstractions instead of concrete implementations
emp = Employee("Alice", 50000)

storage = DatabaseStorage()  
report = TextReport() 

service = EmployeeService(storage, report)

# Now we can save employee and generate report without modifying main classes
service.save_employee(emp)
print(service.generate_report(emp))
