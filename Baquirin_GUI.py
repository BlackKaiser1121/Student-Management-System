from tkinter import *
from functools import partial

from print_all_students import PrinAllStudents
from SearchStudent import searchStudent
from student import StudentInfo
from add_student import AddStudent

stu = StudentInfo()
printAll = PrinAllStudents(stu.allstudents) 
addStu = AddStudent(stu)
srch = searchStudent(stu)


attempts = 4
container = []
btn_txt = ["View User Information", "Search Student", "Add New Student", "View All Student", "Exit"]
def login(username, password):
    global attempts
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    if username == "admin" and password == "password": # eto muna pang login
        login_div.pack_forget()
        main_div.pack(side="left", fill="both", expand=True)
    else:
        attempts -= 1
        error_label.config(text=f"Username or Password is wrong, try again please. (attempts left:{attempts})", fg="red")
        if attempts == 0:
            blocked_screen()

def blocked_screen():
    login_div.pack_forget()
    blocked_div = Frame(win, bg="red")
    blocked_div.pack(side="top", fill="both", expand=True)
    
    Label(blocked_div, text="You are blocked from using this system my friend", font=("Helvetica Now Display", 24, "bold"), bg="red", fg="white").pack(pady=50)
    
    Label(blocked_div, text="Remember your username and password next time", font=("Century Gothic", 18), bg="red", fg="white").pack(pady=20)
    
def logout():
    main_div.pack_forget()
    login_screen()


def login_screen():
    global login_div, error_label, username_entry, password_entry
    
    login_div = Frame(win, bg="black")
    login_div.pack(side="top", fill="both", expand=True)

    Label(login_div, text="Malupit na Student Information System", font=("Helvetica Now Display", 30, "bold"), bg="black", fg="White").pack(pady=50)

    box = Frame(login_div, width=600, height=350, bg="white",bd=2, relief="solid")
    box.pack(pady=50)
    box.pack_propagate(False)
    
    Label(box, text="Login", font=("Century Gothic", 18, "bold"), bg="white").pack(pady=20)
    
    Label(box, text="Username:", font=("Century Gothic", 14), bg="white").pack()
    username_entry = Entry(box, font=("Century Gothic", 14))
    username_entry.pack(pady=5)

    Label(box, text="Password:", font=("Century Gothic", 14), bg="white").pack()
    password_entry = Entry(box, font=("Century Gothic", 14), show="*")
    password_entry.pack(pady=5)

    error_label = Label(box, text="", font=("Century Gothic", 12), bg="white")
    error_label.pack(pady=5)

    Button(box, text="Login", font=("Century Gothic", 14), bg="crimson", command= lambda: login(username_entry.get(), password_entry.get())).pack(pady=20)


def show_frame(frame, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    frame.pack(side="left", fill="x")
    
win = Tk() 
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")



#body
main_div = Frame(win, bg="black")

#menu_div
menu_div = Frame(main_div, bg="white")
menu_div.pack(side="left", fill="y")

#content_div
for i in range(len(btn_txt)):
    container.append(Frame(main_div, bg="black"))
    Label(container[i], text=btn_txt[i], font=("Helvetica Now Display", 18), bg="black", fg="white").grid(row=0, column=0, columnspan=5)





#Main Menu Text
Label(menu_div, width=15, text="Main Menu", font=("Helvetica Now Display", 18), pady=15, bg="white").grid(row=0, column=0)

btn_actions = [partial(show_frame, container[0], [container[1], container[2], container[3]]),
               partial(show_frame, container[1], [container[0], container[2], container[3]]),
               partial(show_frame, container[2], [container[1], container[0], container[3]]),
               partial(show_frame, container[3], [container[1], container[2], container[0]]),
               win.quit]


for i, (text, action) in enumerate(zip(btn_txt, btn_actions)):
    Button(menu_div, anchor="e", bg="crimson", text=text, width=21, font=("Helvetica Now Display", 14), padx=10, pady=15, command=action).grid(row=i+1, column=0)

addStu.show_reg_ui(container[2])

win.title("Student Information Systems ni Jared")
win.config(bg="black")
login_screen()
win.mainloop()