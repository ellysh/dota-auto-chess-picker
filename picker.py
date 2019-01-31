#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk,Image

ABADDON_BUTTON = None
ALCHEMIST_BUTTON = None

def abaddon_click():
  global ABADDON_BUTTON

  ABADDON_BUTTON.config(bg = "green")

  print("abaddon_click")

def alchemist_click():
  print("alchemist_click")

def add_button(window, handler, hero_name, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/" + hero_name + ".png"))
  button.config(image = img, command = handler)

  return button, img

def make_window():
  global ABADDON_BUTTON

  window = Tk()

  window.title("Welcome to LikeGeeks app")

  ABADDON_BUTTON, abaddon_img = add_button(window, abaddon_click, "abaddon", 0, 0)

  ALCHEMIST_BUTTON, alchemist_img = add_button(window, alchemist_click, "alchemist", 1, 0)

  window.mainloop()

def main():
  make_window()

if __name__ == '__main__':
  main()
