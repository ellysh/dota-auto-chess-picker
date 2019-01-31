#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def abaddon_click():
  print("abaddon_click")

def alchemist_click():
  print("alchemist_click")

def add_button(window, handler, hero_name, column, row):
  button = ttk.Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/" + hero_name + ".png"))
  button.config(image = img, command = handler)

  return button, img

def make_window():
  window = Tk()

  window.title("Welcome to LikeGeeks app")

  abaddon_button, abaddon_img = add_button(window, abaddon_click, "abaddon", 0, 0)

  alchemist_button, alchemist_img = add_button(window, alchemist_click, "alchemist", 1, 0)

  window.mainloop()

def main():
  make_window()

if __name__ == '__main__':
  main()
