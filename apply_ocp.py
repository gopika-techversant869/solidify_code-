"""
Open Closed Principle

A class should be open for extension but closed for modification.
"""

from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDatabase:
    def save(self, employee: Employee):
        print(f"Saving {employee.name}'s data to the database...")

# Base class for Report Formats (OCP applied)
class ReportFormat(ABC):  
    @abstractmethod
    def generate(self, employee: Employee):
        pass

# Different types of reports (extending without modifying base classes)
class TextReport(ReportFormat): 
    def generate(self, employee: Employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"

class PDFReport(ReportFormat):  
    def generate(self, employee: Employee):
        return f"[PDF] Employee Report: {employee.name}, Salary: {employee.salary}"

class CSVReport(ReportFormat):  
    def generate(self, employee: Employee):
        return f"CSV Format: {employee.name}, {employee.salary}"

# Creating an Employee instance
emp = Employee("Alice", 50000)

report = TextReport()  
print(report.generate(emp))  

report = PDFReport()
print(report.generate(emp))  

report = CSVReport()
print(report.generate(emp))  
