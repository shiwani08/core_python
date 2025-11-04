from manager import Manager
from developer import Developer
from intern import Intern

class Salary:
    def __init__(self, employees):
        self.employees = employees

    def print_all_salaries(self):
        for emp in self.employees:
            salary = emp.calculate_salary()
            print(f"{emp.__class__.__name__} salary: {salary}")

manager = Manager(100000, 50000, 20000)
developer = Developer(80000, 10000)
intern = Intern(30000)

salary = Salary([manager, developer, intern])
salary.print_all_salaries()
