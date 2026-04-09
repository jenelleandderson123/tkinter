from tkinter import *

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif length < 5:
        result_label.config(text="Weak Password", fg="red")
    elif 5 <= length < 8:
        result_label.config(text="Moderate Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

window = Tk()
window.title("Password Strength Checker")
window.geometry("400x250")
window.configure(bg="lightblue")

Label(window, text="Enter Password", font=("Arial", 14), bg="lightblue").pack(pady=10)

entry = Entry(window, show="*", width=25)
entry.pack(pady=5)

Button(window, text="Check Strength", command=check_strength).pack(pady=10)

result_label = Label(window, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)

window.mainloop()