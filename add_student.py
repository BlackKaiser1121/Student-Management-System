from tkinter import *
from functools import partial
import tkinter.messagebox

class AddStudent:
    def __init__(self, student):
        self.student_info = student

    def add_student(self, name, age, id_number, email, phone):
        self.student_info.setName(name)
        self.student_info.setAge(age)
        self.student_info.setId_number(id_number)
        self.student_info.setEmail(email)
        self.student_info.setPhone(phone)
        stud_written = [name, age, id_number, email, phone]
        self.student_info.allstudents.append(stud_written)
        print(f"Added student {stud_written[0]} to the list.")
        print("\n","="*6, "Nothing follows", "="*6)
        self.write_to_file(stud_written)

    def write_to_file(self, data_to_write):
        with open("student_data.txt", "a+")as file:
            file.write(",".join(data_to_write) + "\n")
                
            


    def add_student_input(self):
        print("\n","="*6, "Add New Student", "="*6, "\n")
        name = input("Name: ")
        age = input("Age: ")
        id_number = input("ID Number: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        self.add_student(name, age, id_number, email, phone)
        
    def show_reg_ui(self, reg_frame):
        self.lblErrors = Label(reg_frame, text="", fg="red")
        self.lblErrors.grid(row=1, column=0, columnspan=5)
        self.reg_txt, self.reg_entry = ["Name", "Age", "ID Number", "Email", "Phone Number"], []
        for i in range(len(self.reg_txt)):
            Label(reg_frame, text=self.reg_txt[i], font=("Century Gothic", 14), width=13, bg="black", fg="white").grid(row=i+2, column=0)
            self.reg_entry.append(Entry(reg_frame, width = 40, font=("Century Gothic", 14)))
            self.reg_entry[i].grid(row=i+2, column=1, columnspan=3)
        reg_btn = Button(reg_frame, text="Register", font=("Century Gothic", 14), bg="crimson", command=self.check_entries)
        reg_btn.grid(columnspan=5)
        
    def check_entries(self):
        errors = []
        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get() == "":
                errors.append(f"{self.reg_txt[i]} is required.")
        if not errors:
            self.add_student(self.reg_entry[0].get(), self.reg_entry[1].get(), self.reg_entry[2].get(), self.reg_entry[3].get(), self.reg_entry[4].get())
            for entry in self.reg_entry:
                entry.delete(0, END)
            tkinter.messagebox.showinfo("Success", "Student added successfully!")
        else:
            self.lblErrors.config(text="\n".join(errors))
        
        