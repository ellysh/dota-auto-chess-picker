#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk,Image

window = Tk()

window.title("Welcome to LikeGeeks app")

canvas = Canvas(window, width = 300, height = 300)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("images/heroes.jpg"))
canvas.create_image(20,20, anchor=NW, image=img)

window.mainloop()
