from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("500x300")

def Handle_Keypress(event):
    print(event.char)

window.bind("<Key>", Handle_Keypress)

def Handle_Click(event):
    print("\n The button was clicked")

button = Button(text = "Click Me!")
button.pack()

button.bind("<Button - 1>",Handle_Click)

window.mainloop()