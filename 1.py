from tkinter import *
from PIL import Image, ImageTk
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("500x500")
window.config(bg="lightblue")

rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

choices = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

user_label = Label(window, text="You", bg="lightblue", font=("Arial", 12))
user_label.pack()

user_choice_label = Label(window, bg="lightblue")
user_choice_label.pack()

comp_label = Label(window, text="Computer", bg="lightblue", font=("Arial", 12))
comp_label.pack()

comp_choice_label = Label(window, bg="lightblue")
comp_choice_label.pack()

result_label = Label(window, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

def play(user_choice):
    comp_choice = random.choice(["rock", "paper", "scissors"])

    user_choice_label.config(image=choices[user_choice])
    comp_choice_label.config(image=choices[comp_choice])

    if user_choice == comp_choice:
        result = "It's a Draw!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        result = "You Win"
    else:
        result = "You Lose"

    result_label.config(text=result)

btn_frame = Frame(window, bg="lightblue")
btn_frame.pack(pady=20)

Button(btn_frame, image=rock_img, command=lambda: play("rock")).grid(row=0, column=0, padx=10)
Button(btn_frame, image=paper_img, command=lambda: play("paper")).grid(row=0, column=1, padx=10)
Button(btn_frame, image=scissors_img, command=lambda: play("scissors")).grid(row=0, column=2, padx=10)

window.mainloop()