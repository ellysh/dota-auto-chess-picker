#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.4"
_PIECES_FILE = "database/csv/pieces.csv"
_COMBOS_FILE = "database/csv/combos.csv"

_DEFAULT_COLOR = "#d9d9d9"
_GREEN_COLOR = "#66ce54"
_RED_COLOR = "#ff4f4f"

PIECES = {}
COMBOS = []

BUTTONS = {}

def load_pieces():
  global PIECES

  with open(_PIECES_FILE) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
     PIECES[line[0]] = [line[1], line[2], line[3]]

def load_combos():
  global COMBOS

  with open(_COMBOS_FILE) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      COMBOS.append(line[1])

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_combos(piece_name):
  # TODO: Implement this function
  pass

def button_click(piece_name):
  global BUTTONS
  global PIECES
  global _RED_COLOR

  reset_all_buttons()

  BUTTONS[piece_name][0].config(bg = _RED_COLOR)

  highlight_combos(piece_name)

def add_button(window, button_click, piece, level, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/pieces/" + piece + ".png"))

  button.config(image = img, command = lambda:button_click(piece), \
                compound = TOP, text = '* ' * int(level), \
                font=("Arial Bold", 5), pady = 0, padx = 0)

  return button, img

def add_buttons(window):
  global BUTTONS
  global PIECES

  row = 0
  column = 0

  for key, value in PIECES.iteritems():
    BUTTONS[key] = add_button(window, button_click, key, value[2], \
                              column, row)

    column += 1

    if 10 < column:
      column = 0
      row += 1

def make_window():
  global VERSION

  window = Tk()

  window.title("Dota Auto Chess Combos Picker " + _VERSION)

  add_buttons(window)

  window.mainloop()

def main():
  load_pieces()

  load_combos()

  make_window()

if __name__ == '__main__':
  main()
