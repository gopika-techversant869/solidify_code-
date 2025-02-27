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

