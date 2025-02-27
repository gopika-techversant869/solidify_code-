from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeDatabase:
    def save(self, employee: Employee):
        print(f"Saving {employee.name}'s data to the database...")


class ReportFormat(ABC):  # Base class for all reports
    @abstractmethod
    def generate(self, employee):
        pass

class TextReport(ReportFormat): 
    def generate(self, employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"

class PDFReport(ReportFormat): 
    def generate(self, employee):
        return f"[PDF] Employee Report: {employee.name}, Salary: {employee.salary}"

class CSVReport(ReportFormat):  
    def generate(self, employee):
        return f"CSV Format: {employee.name}, {employee.salary}"

emp = Employee("Alice", 50000)
report = TextReport()  
print(report.generate(emp))

report = PDFReport()
print(report.generate(emp))

report = CSVReport()
print(report.generate(emp))
