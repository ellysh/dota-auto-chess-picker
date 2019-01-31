#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk,Image

BUTTONS = {}

def button_click(hero_name):
  #global BUTTONS

  #ABADDON_BUTTON.config(bg = "green")

  print("hero_name = %s" % hero_name)

def alchemist_click():
  print("alchemist_click")

def add_button(window, handler, hero_name, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/" + hero_name + ".png"))
  button.config(image = img, command = lambda:handler(hero_name))

  return button, img

def make_window():
  global BUTTONS

  window = Tk()

  window.title("Welcome to LikeGeeks app")

  BUTTONS["abaddon"] = add_button(window, button_click, "abaddon", 0, 0)

  BUTTONS["alchemist"] = add_button(window, button_click, "alchemist", 1, 0)

  window.mainloop()

def main():
  make_window()

if __name__ == '__main__':
  main()
