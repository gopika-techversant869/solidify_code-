"""multiple responsibilities implemented in one class.such as salary calculation,data storing and repoprt generation.
if any of the method is to be changed, it affect the other things in the class. 

-> The Employee object holds methods that may not be used, wasting memory.
-> If many employees exist, each will carry redundant methods in memory.
-> Large objects stay in heap memory longer, increasing garbage collection time.

"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        print(f"Salary of {self.name} is {self.salary}")

    def save_to_database(self):
        print(f"Saving {self.name}'s data to the database...")

    def generate_report(self):
        return print(f"Employee Report: {self.name}, Salary: {self.salary}")


emp_obj_1 = Employee("gopika","10000")
emp_obj_1.calculate_salary()
emp_obj_1.save_to_database()
emp_obj_1.generate_report()

"""
-> When you create an object (emp_obj_1) of the Employee class, it loads all instance attributes and methods defined in that class.
-> If the Employee class directly contained methods like save_to_db() and generate_report(), then even if you don't use them, they are still part of the object, increasing memory usage.
-> This would impact memory efficiency and potentially make garbage collection slower if large objects persist in memory.
"""
