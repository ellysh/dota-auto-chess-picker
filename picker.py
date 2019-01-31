#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

window = Tk()

window.title("Welcome to LikeGeeks app")

button = ttk.Button(window)
button.pack()

img = ImageTk.PhotoImage(Image.open("images/heroes.jpg"))
button.config(image = img)

window.mainloop()
