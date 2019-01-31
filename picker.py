#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def clicked():
  print("button was clicked")

def add_button(window, handler, hero_name):
  button = ttk.Button(window)
  button.pack()

  img = ImageTk.PhotoImage(Image.open("images/" + hero_name + ".png"))
  button.config(image = img, command = handler)

  return button, img

def make_window():
  window = Tk()

  window.title("Welcome to LikeGeeks app")

  abaddon_button, abaddon_img = add_button(window, clicked, "abaddon")

  window.mainloop()

def main():
  make_window()

if __name__ == '__main__':
  main()
