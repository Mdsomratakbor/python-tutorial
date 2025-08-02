from manager import StudentManager
from student import Student
from teacher import Teacher
from course import Course

def main():
    manager = StudentManager()
    
    # Create Teachers
    t1 = Teacher(1, "Mr. Smith", "Mathematics")
    t2 = Teacher(2, "Ms. Johnson", "Physics")
    
    manager.add_teacher(t1)
    manager.add_teacher(t2)
    
    
    #Create Courses
    c1 = Course(101, "Algebra", t1)
    c2 = Course(102, "Mechanics", t2)
    
    manager.add_course(c1)
    manager.add_course(c2)
    
    # Create Students
    s1 = Student(201, "Alice", 18)
    s2 = Student(202, "Bob", 19)
    manager.add_student(s1)
    manager.add_student(s2)
    
    # Enroll Students
    manager.enroll_student(201, 101)
    manager.enroll_student(202, 102)
    manager.enroll_student(202, 101)
    
    
     # Show All Students
    print("\nAll Students Info:")
    manager.show_all_students()
    
    
    # Show All Teachers
    manager.show_all_teachers()

if __name__ == "__main__":
    main()