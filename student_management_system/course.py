class Course:
    def __init__(self, course_id, course_name, teacher):
        self.course_id = course_id
        self.course_name= course_name
        self.teacher = teacher
        
    def __str__(self):
        return f"Course[ID={self.course_id}, Name={self.course_name}, Taught by={self.teacher.name}]"