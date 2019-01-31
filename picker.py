#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def clicked():
  print("button was clicked")

def make_window():
  window = Tk()

  window.title("Welcome to LikeGeeks app")

  button = ttk.Button(window)
  button.pack()

  img = ImageTk.PhotoImage(Image.open("images/abaddon.png"))
  button.config(image = img, command = clicked)

  window.mainloop()

def main():
  make_window()

if __name__ == '__main__':
  main()
