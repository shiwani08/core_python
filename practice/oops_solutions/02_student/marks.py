class Student:
    def __init__(self, name):
        self.name = name
        self.mark = {}

    def add_mark(self, subject, mark):
        self.mark[subject] = mark

    def total_marks(self):
        return sum(self.mark.values())

    def calculate_average(self):
        if not self.mark:
            return 0
        return self.total_marks() / len(self.mark)
    
    def check_grade(self, subject):
        if subject not in self.mark:
            return "No marks for this subject."
        mark = self.mark[subject]
        if mark >= 90:
            return 'A'
        elif mark >= 80:
            return 'B'
        elif mark >= 70:
            return 'C'
        elif mark >= 60:
            return 'D'
        else:
            return 'F'

student = Student("Alice")
student.add_mark("Math", 85)
student.add_mark("Science", 90)
print(f"Student Name: {student.name}")
print("Total subjects:", len(student.mark))
print(f"Total Marks: {student.total_marks()}")
print(f"Average Marks: {student.calculate_average()}")
print(f"Grade in Math: {student.check_grade('Math')}")
print(f"Grade in Science: {student.check_grade('Science')}")