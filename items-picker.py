#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.2"
_ITEMS_FILE = "database/csv/items.csv"
_DEFAULT_COLOR = "#d9d9d9"

ITEMS = {}
BUTTONS = {}

def load_table(filename, table):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      table[line[1]] = [line[2], line[3]]

def load_items():
  global ITEMS

  load_table(_ITEMS_FILE, ITEMS)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_items(item_name):
  pass

def button_click(item_name):
  global BUTTONS
  global ITEMS

  reset_all_buttons()

  BUTTONS[item_name][0].config(bg = "red")

  highlight_items(item_name)

def add_button(window, handler, item_name, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/items/" + item_name + ".png"))
  button.config(image = img, command = lambda:handler(item_name))

  return button, img

def make_window():
  global VERSION
  global ITEMS
  global BUTTONS

  window = Tk()

  window.title("Dota Auto Chess Picker " + _VERSION)

  row = 0
  column = 0

  for item in ITEMS:
    BUTTONS[item] = add_button(window, button_click, item, row, column)

    row += 1

    if 10 < row:
      row = 0
      column += 1

  window.mainloop()

def main():
  load_items()

  make_window()

if __name__ == '__main__':
  main()
