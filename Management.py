from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_details(self):
        pass


class GradeCalculatorMixin:
    def calculate_average(self, grades: dict):
        keys = list(grades.keys())
        total = 0
        index = 0
        while index < len(keys):
            total += grades[keys[index]]
            index += 1
        if index == 0:
            return 0.0
        return total / index


class Student(Person, GradeCalculatorMixin):
    def __init__(self, student_id: int, name: str):
        super().__init__(name)
        self.__student_id = student_id
        self.__grades = {}

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        raise AttributeError("Use add_grade() method to set grades")

    def add_grade(self, subject: str, grade: float):
        if not 0 <= grade <= 100:
            raise ValueError("grade must be above 0 and under 100")
        self.__grades[subject] = grade

    def average_grade(self):
        return self.calculate_average(self.__grades)

    def display_details(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.average_grade()}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        if student.student_id in self.students:
            print("Student with given ID already exist")
        else:
            self.students[student.student_id] = student

    def show_student_details(self, student_id: int):
        student = self.students.get(student_id)
        if student:
            student.display_details()
        else:
            print("Student not found.")

    def show_student_average_grade(self, student_id: int):
        student = self.students.get(student_id)
        if student:
            avg = student.average_grade()
            print(f"Student {student.name}'s average grade is: {avg}")
        else:
            print("Student not found.")

