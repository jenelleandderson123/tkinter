from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination Counter")
window.configure(bg = "purple")
window.geometry("500x300")

img = Image.open("image.jpg").resize((350,350))
img = ImageTk.PhotoImage

Label(window, image = img, bg = "light blue").place(x= 180, y = 20)
Label(window,
      text = "Hello!! Welcome to the Denomination Counter.",
      bg = "yellow").place(relx = 0.5, y= 340, anchor = CENTER)

def Topwin():
    top = Toplevel(window)
    top.title("Denomination Calculator")
    top.configure(bg = "red")
    top.geometry("600x350")

    Label(top, text = "Enter the total amount", bg = "light grey").place(x= 230, y= 50)
    entry = Entry(top)
    entry.place(x= 200, y = 80)
    Label(
        top,
        text = "Here are number notes for each denomination",
        bg = "yellow"
    ).place(x = 140, y = 170)
    denominations = [100, 150, 100]
    entries = []
    for i, value  in enumerate (denominations):
        Label(top, text = str(value), bg = "light grey").place(x = 270, y = 200 + i*30)
        e = Entry(top)
        e.place(x= 270, y= 200 + i*30)
        entries.append(e)
    def calculator():
        try:
            amount = int(entry.get())
            for i, value in enumerate(denominations):
                notes = amount // value
                amount %= value

                entries[i].delete(0,END)
                entries[i].insert(END, str(notes))
        except ValueError:
            messagebox.showerror("Please enter a valid number")
    Button(
        top,
        text = "calculate",
        command = calculator,
        bg = "red",
        fg = "purple"
    ).place(x = 2240, y = 120)

    def msg():
        if messagebox.showinfo(
            "Alert!",
            "Are you sure you want to calculate the denomination count?"
        ) == "ok":
            Topwin()
            
    Button(
        top,
        text = "Let's get started",
        command = msg,
        bg = "brown",
        fg = "white"
    ).place(x = 2240, y = 120)

window.mainloop()