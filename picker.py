#!/usr/bin/env python

from tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.1"
_PIECES_FILE = "database/csv/pieces.csv"
_SPECIES_FILE = "database/csv/species.csv"
_CLASSES_FILE = "database/csv/classes.csv"

PIECES = {}
SPECIES = {}
CLASSES = {}

BUTTONS = {}

def load_pieces():
  global PIECES

  with open(_PIECES_FILE) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      PIECES[line[0]] = [line[1], line[2]]

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = "gray")

def button_click(piece_name):
  global BUTTONS

  reset_all_buttons()

  BUTTONS[piece_name][0].config(bg = "green")

  print("piece_name = %s" % piece_name)

def add_button(window, handler, piece_name, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open("images/" + piece_name + ".png"))
  button.config(image = img, command = lambda:handler(piece_name))

  return button, img

def make_window():
  global VERSION
  global PIECES
  global BUTTONS

  window = Tk()

  window.title("Dota Auto Chess Picker " + _VERSION)

  row = 0
  column = 0

  for piece in PIECES:
    BUTTONS[piece] = add_button(window, button_click, piece, row, column)

    row += 1

    if 10 < row:
      row = 0
      column += 1

  window.mainloop()

def main():
  load_pieces()

  #load_species()

  #load_classes()

  make_window()

if __name__ == '__main__':
  main()
