class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        
    def enroll(self, course):
        self.courses.append(course)
    
    def show_courses(self):
        return [ course.course_name for course in self.courses]
    
    def __str__(self):
        return f"Student[ID={self.student_id}, Name={self.name}, Age={self.age}]"