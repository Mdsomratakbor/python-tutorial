import student_record_tuple as st
def run():
    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Find Student by Roll")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
                name = input("Enter name: ")
                roll = input("Enter roll number: ")
                age = int(input("Enter age: "))
                dept = input("Enter department: ")
                st.add_student(name, roll, age, dept)

        elif choice == "2":
                st.display_students()

        elif choice == "3":
                roll = input("Enter roll number to search: ")
                st.find_student_by_roll(roll)

        elif choice == "4":
                print("Exiting the program.")
                break
        else:
                print("Invalid choice. Please enter 1-4.\n")

# Run the program
if __name__ == "__main__":
    run()