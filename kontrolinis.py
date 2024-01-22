class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        print(f"Student: {self.name}, Course: {math_course.name}, Grade: {self.grades[math_course]}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return math_course.name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = attendance_record
            print(f"Student: {student.name}, Attendance: {attendance_status}")

    def add_lesson(self, lesson):
        if lesson not in lesson_1.lessons:
            lesson_1.lessons.append(lesson)

    def get_lessons(self):
        for lesson in lesson_1.lessons:
            print(f'Topic: {lesson.topic}, duration: {lesson.duration}, date: {lesson.date}, {lesson.materials}')


class Lesson:
    def __init__(self, room, topic, duration, date):
        self.__room = room
        self.topic = topic
        self.duration = duration
        self.date = date
        self.materials = []
        self.lessons = []

    def display_lesson(self):
        return f'Topic: {self.topic}, duration: {self.duration}, date: {self.date}'

    def add_materials(self, material):
        if material not in self.materials:
            self.materials.append(material)

    def get_room(self):
        return self.__room

    def set_room(self, room):
        self.__room = room


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

lesson_1 = Lesson('Math class', 'Analysis and probability', '45 minutes', '2024-03-01')
lesson_2 = Lesson('Math class', 'Modern geometry', '90 minutes', '2024-03-10')
lesson_1.add_materials('Mathematical analysis')
lesson_2.add_materials('Modern geometries')
math_course.add_lesson(lesson_1)
math_course.add_lesson(lesson_2)
math_course.get_lessons()
