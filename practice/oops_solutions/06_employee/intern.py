from employee import Employee

class Intern(Employee):

    def __init__(self, incentives):
        self.incentives = incentives

    def calculate_salary(self):
        salary = self.incentives
        return salary

intern = Intern(incentives=2000)
salary = intern.calculate_salary()

print(f"Salary of the intern is: {salary}")