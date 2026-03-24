from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Message box")
window.geometry("500x200")

def msg():
    messagebox.showwarning("Alert!","Stop! A virus has been found")

def show_warning():
    messagebox.showwarning("Watch out!", "A very weird file was found")

def show_error():
    messagebox.showerror("Oh no!", "System Crash Detected")
def ask_question():
    response = messagebox.askyesno("Confirm", "Do You really want to delete the file", "All the important files?")
    if response == True:
        print("User chose YES")
    else:
        print("User chose NO")

button_warning = Button(window, text = "Show warning", command=show_warning, bg= "red")

button_error = Button(window, text = "show error", command=show_error, bg= "yellow")
button_question = Button(window, text = "Show warning", command=ask_question, bg = "green")

button_scan = Button(window, text = "Scan for virus", command=msg, bg= "purple")

button_warning.place(x=40, y=80)
button_error.place(x=150, y=30)
button_question.place(x=40, y=80)
button_scan.place(x=150, y=80 )

window.mainloop()