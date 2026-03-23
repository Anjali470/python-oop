class Student:

    student_id_counter = 1
    def __init__(self, name, age, email, courses = None, grades = None):
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.name = name
        self.age = age
        self.email = email
        self.courses = list(courses) if courses is not None else []
        self.grades = grades if grades is not None else {}

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)

    def add_grade(self, course_name, grade):
        if course_name not in self.courses:
            self.courses.append(course_name)
        self.grades[course_name] = grade

    def calculate_gpa(self, course_name):
        if course_name not in self.courses:
            return f"{course_name} not found"
        if 90 < self.grades[course_name] <= 100:
            return 4.0
        elif 80 < self.grades[course_name] <= 90:
            return 3.0
        elif 70 < self.grades[course_name] <= 80:
            return 2.0
        elif 60 < self.grades[course_name] <= 70:
            return 1.0
        else:
            return 0.0

    def calculate_cgpa(self):
        if len(self.grades) == 0:
            return 0.0
        calculated_gpa = 0
        for course_name, grade in self.grades.items():
            calculated_gpa += self.calculate_gpa(course_name)
        return round(calculated_gpa / len(self.grades), 2)

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Courses:", self.courses)
        print("Grades:", self.grades)

    def get_transcript(self):
        return self.grades.copy()

student1 = Student("John Doe", 20, "john@email.com")
print(student1.courses)  # []

student1.enroll_course("Python Programming")
student1.add_grade("Python Programming", 85)

print(student1.courses)  # ['Python Programming']
print(student1.grades)   # {'Python Programming': 85}
print(student1.calculate_cgpa())  # 3.0

student1.display_info()
print("Transcript:", student1.get_transcript())
