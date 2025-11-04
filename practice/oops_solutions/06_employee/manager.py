from employee import Employee

class Manager(Employee):

    def __init__(self, basic, bonus, incentives):
        self.basic = basic
        self.bonus = bonus
        self.incentives = incentives

    def calculate_salary(self):
        salary = self.bonus + self.basic + self.incentives
        return salary

manager = Manager(basic=100000, bonus=50000, incentives=20000)
salary = manager.calculate_salary()

print(f"Salary of the Manager is: {salary}")