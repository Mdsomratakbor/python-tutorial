# student_record_tuple.py


# List of students

student_list = []

def add_student(name, roll, age, department):
    student = (name, roll, age, department)
    print(type(student))
    student_list.append(student)
    print(f'Student {name} added successfully.\n')


def display_students():
    if not student_list:
        print('No student records available.\n')
        return

    print("\n--- Student Records ---")
    
    for index, student in enumerate(student_list, start = 1):
        name, roll, age, department = student
        print(f"{index}. Name: {name}, Roll: {roll}, Age: {age}, Department: {department}") 
    print()
def find_student_by_roll(roll):
    for student in student_list:
        if student[1] == roll:
            print(f"\nStudent Found: Name={student[0]}, Roll={student[1]}, Age={student[2]}, Dept={student[3]}\n") 
            return
        print("\nStudent not found.\n")

