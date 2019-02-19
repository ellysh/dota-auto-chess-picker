#!/usr/bin/env python

from Tkinter import *
from tkinter import ttk
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.7"
_PIECES_FILE = "database/csv/pieces.csv"
_COMBOS_FILE = "database/csv/combos.csv"

PIECES = {}
COMBOS = {}

BUTTONS = []

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
      if not line[1] in COMBOS.keys():
        COMBOS[line[1]] = []

      COMBOS[line[1]].append([line[0], line[2], line[3], line[4]])

def add_button(window, piece, level, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/pieces/" + piece + ".png"))

  button.config(image = img, \
                compound = TOP, text = '* ' * int(level), \
                font=("Arial Bold", 5), pady = 0, padx = 0)

  return button, img

def add_combos(window, game_phase):
  global BUTTONS
  global PIECES
  global COMBOS

  row = 0

  for combo in COMBOS[game_phase]:
    pieces = [x.strip() for x in combo[3].split(',')]

    column = 0
    for piece in pieces:
        BUTTONS.append(add_button(window, piece, PIECES[piece][2], \
                                  column, row))
        column += 1

    row += 1

def make_window():
  global VERSION

  window = Tk()

  window.title("Dota Auto Chess Strategy Picker " + _VERSION)

  notebook = ttk.Notebook(window)

  earlygame_page = ttk.Frame(notebook)
  notebook.add(earlygame_page, text="Earlygame")
  add_combos(earlygame_page, "Earlygame")

  midgame_page = ttk.Frame(notebook)
  notebook.add(midgame_page, text="Midgame")
  add_combos(midgame_page, "Midgame")

  lategame_page = ttk.Frame(notebook)
  notebook.add(lategame_page, text="Lategame")
  add_combos(lategame_page, "Lategame")

  notebook.pack(expand=1, fill="both")

  window.bind('<Escape>', lambda event, a = True: reset_buttons(a))

  #highlight_combos(CHOOSED_PIECES)

  window.mainloop()

def main():
  load_pieces()

  load_combos()

  make_window()

if __name__ == '__main__':
  main()
