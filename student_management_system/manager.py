from student import Student
from teacher import Teacher
from course import Course

class StudentManager:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        
    def add_student(self, student):
        self.students.append(student)
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None) 
        
        if student and course:
            student.enroll(course)
            print(f"{student.name} enrolled in {course.course_name}")
        else:
            print("Invalid student ID or course ID")    
    def show_all_students(self):
        for student in self.students:
            print (student)
            print("  Enrolled in:", student.show_courses())
    
    def show_all_teachers(self):
        for teacher in self.teachers:
            print(teacher)