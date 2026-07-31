class Student:
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

s1 = Student("Akash", "A")
s2 = Student("Anu", "B")
s3 = Student("Rahul", "A")

print("Total Students:", Student.total_students)