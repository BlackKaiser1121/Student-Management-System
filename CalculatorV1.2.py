from tkinter import *
from functools import partial
win = Tk()
res, btn_txt, row_num, col_num, expression = Label(win,width="10", text="0", fg="black", font=("impact", 25), anchor='e', justify='right'), ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/"], 0, 0, "0"
res.grid(row=0, column=0, columnspan=4, sticky="nsew") 
def Functions(value):
    global expression
    if value == "C":
        expression = "0"  
    elif value == "=":
        try:
            expression = str(eval(expression))
        except Exception as e:
            expression = "Error"
    else:
        if expression == "0":
            expression = value
        else:
            expression += value 
    res.config(text=expression)
for i in range(len(btn_txt)):
    Button(win, width=4, height=1, text=btn_txt[i], font=("impact", 25), command=partial(Functions, btn_txt[i])).grid(row=row_num + 1, column=col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.title("Calculator v1.2"), win.geometry("298x408+800+320"), win.mainloop()