#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.4"
_ITEMS_FILE = "database/csv/items.csv"

_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_GREEN_COLOR = "#66ce54"
_RED_COLOR = "#ff4f4f"

ITEMS = {}
BUTTONS = {}

ITEM_DESCRIPTION = None

def load_table(filename, table):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      table[line[1]] = [line[2], line[3], line[0]]

def load_items():
  global ITEMS

  load_table(_ITEMS_FILE, ITEMS)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_components(upgrade_name):
  global ITEMS
  global _GREEN_COLOR
  global _RED_COLOR

  for key, value in ITEMS.iteritems():
    upgrades = [upgrade.strip() for upgrade in ITEMS[key][1].split('/')]

    if upgrade_name in upgrades and BUTTONS[key][0].cget("bg") != _RED_COLOR:
      BUTTONS[key][0].config(bg = _GREEN_COLOR)

def highlight_items(item_name):
  global ITEMS
  global _AZURE_COLOR

  upgrades = [upgrade.strip() for upgrade in ITEMS[item_name][1].split('/')]
  for key, value in BUTTONS.iteritems():
    if key in upgrades:
      value[0].config(bg = _AZURE_COLOR)

  highlight_components(item_name)

def button_click(item_name):
  global BUTTONS
  global ITEMS
  global ITEM_DESCRIPTION
  global _RED_COLOR

  reset_all_buttons()

  BUTTONS[item_name][0].config(bg = _RED_COLOR)

  ITEM_DESCRIPTION.config(text = ITEMS[item_name][0])

  highlight_items(item_name)

def add_button(window, handler, item_name, tier, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/items/" + item_name + ".png"))
  tier_text = "* " * int(tier) if tier.isdigit() else tier

  button.config(image = img, command = lambda:handler(item_name), \
                compound = TOP, text = tier_text, font=("Arial Bold", 5), \
                pady = 0, padx = 0)

  return button, img

def add_buttons(window):
  global BUTTONS
  global ITEMS

  row = 0
  column = 0

  for key, value in ITEMS.iteritems():
    BUTTONS[key] = add_button(window, button_click, key, value[2], \
                              column, row)

    column += 1

    if 6 < column:
      column = 0
      row += 1

def make_window():
  global VERSION
  global BUTTONS
  global ITEM_DESCRIPTION

  window = Tk()

  window.title("Dota Auto Chess Picker " + _VERSION)

  add_buttons(window)

  ITEM_DESCRIPTION = Label(window, font=("Arial Bold", 12), \
                                wraplength=300, anchor=NW, justify=LEFT)
  ITEM_DESCRIPTION.grid(column = 0, row = 8, columnspan = 6)

  window.mainloop()

def main():
  load_items()

  make_window()

if __name__ == '__main__':
  main()
