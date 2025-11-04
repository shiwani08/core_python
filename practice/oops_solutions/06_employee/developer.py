from employee import Employee

class Developer(Employee):

    def __init__(self, basic, incentives):
        self.basic = basic
        self.incentives = incentives

    def calculate_salary(self):
        salary = self.basic + self.incentives
        return salary

developer = Developer(basic=100000, incentives=20000)
salary = developer.calculate_salary()

print(f"Salary of the Developer is: {salary}")