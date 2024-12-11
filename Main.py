from student import StudentInfo, Student
from SearchStudent import searchStudent
from main_menu import main_menu
stu, srch = StudentInfo(), searchStudent()

# Create an instance of StudentInfo to hold all student data
students = StudentInfo()

# Student data list containing student information
student_data_list = [
    ["Louise", "19", "2023-2-00995", "2023-2-00995@lpunetwork.edu.ph", "09164470716"],
    ["Lhanz", "20", "2023-2-00714", "2023-2-00714@lpunetwork.edu.ph", "09121222122"],
    ["Nier", "64", "2023-2-01058", "2023-2-01058@lpunetwork.edu.ph", "09235185731"],
    ["Fiel", "19", "2023-2-01619", "2023-2-01619@lpunetwork.edu.ph", "09235184329"],
    ["Renzo", "22", "2023-2-02581", "2023-2-02581@lpunetwork.edu.ph", "09095837472"],
    ["Cyruz", "19", "2023-2-01019", "2023-2-01019@lpunetwork.edu.ph", "09095837472"],
    ["Cheilou", "19", "2023-2-00487", "2023-2-00487@lpunetwork.edu.ph", "09095837472"],
    ["Josh", "19", "2023-2-01226", "2023-2-01226@lpunetwork.edu.ph", "09095837472"],
    ["Shan", "20", "2023-2-01657", "2023-2-01657@lpunetwork.edu.ph", "09095837472"],
    ["Mark", "20", "2023-2-01443", "2023-2-01443@lpunetwork.edu.ph", "09095837472"]
]


for student_data in student_data_list:
    student = Student(student_data[0], int(student_data[1]), student_data[2], student_data[3], student_data[4])
    stu.students_info(student) 

attempts = 0

while True:
    login_check = input("Enter student ID: ")
    if login_check.lower() == "admin":
        while True:
            main_menu(login_check, students) 
            check = input("Do you want to try again? (Y/N): ")
            if check.lower() != 'y':
                break
        break
    else:
        attempts += 1
        print(f"You have {4 - attempts} attempts left.")
    if attempts > 3:
        print("You have exceeded the number of attempts. Goodbye!")
        break





    