class Student:
    def __init__(self, name, age, id_number, email, phone):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
        self.phone = phone

class StudentInfo:
    def __init__(self):
        self.all_students = []  

    def students_info(self, student):
        self.all_students.append(student) 

    def print_allstudents(self):
        for student in self.all_students:
            print(f"Name: {student.name}, ID: {student.id_number}")