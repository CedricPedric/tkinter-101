import tkinter
import tkinter as tk


window = tkinter.Tk()

window.geometry('300x300')
window.configure(bg='white')
window.title("Hello")




# box 1
box1 = tk.Label(
    window,
    text="Hello World!",
    bg="purple",
    fg="pink"
)

box1.pack(
    ipadx=100,
    ipady=100,
    expand=True
)

window.mainloop()
