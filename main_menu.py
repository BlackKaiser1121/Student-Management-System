from add_student import AddStudent
from SearchStudent import searchStudent
from student import Student, StudentInfo

attempts = 0
students = StudentInfo() 


def main_menu(name, students):
    search = searchStudent()

    while True:
        print(f"Welcome {name}!")
        print("\nPlease choose from the following option:\n1. View your information\n2. View other student's information\n3. Register a New Student\n4. Print all students in the list\n5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(f"Viewing information for {name}:")
    

        elif choice == 2:
            student_id = input("Enter the Student ID of the student you want to view: ")
            result = search.search_students(students.all_students, student_id) 
            print(f"\n{result}")

        elif choice == 3:
            add_stu = AddStudent(students)
            add_stu.input_new_student()

        elif choice == 4:
            print("All Students:")
            students.print_allstudents()

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")



