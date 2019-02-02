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

SPECIES_DESCRIPTION_1 = None
SPECIES_NUMBER_1 = None

SPECIES_DESCRIPTION_2 = None
SPECIES_NUMBER_2 = None

CLASS_DESCRIPTION = None
CLASS_NUMBER = None

BUTTONS = {}

def load_table(filename, table):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      table[line[0]] = [line[1], line[2]]

def load_pieces():
  global PIECES

  load_table(_PIECES_FILE, PIECES)

def load_species():
  global SPECIES

  load_table(_SPECIES_FILE, SPECIES)

def load_classes():
  global CLASSES

  load_table(_CLASSES_FILE, CLASSES)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = "gray")

def highlight_similarity(piece_name, index, color):
  global PIECES

  similarity = PIECES[piece_name][index]
  similarity_set = set(similarity.split('/'))

  for key, value in BUTTONS.iteritems():
    if set.intersection(set(PIECES[key][index].split('/')), \
                        similarity_set) \
        and key != piece_name:

      if value[0].cget("bg") == "gray":
        value[0].config(bg = color)
      else:
        value[0].config(bg = "#7742f4")

def highlight_species(piece_name):
  highlight_similarity(piece_name, 0, "green")

  highlight_similarity(piece_name, 1, "blue")

def button_click(piece_name):
  global BUTTONS
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global CLASS_DESCRIPTION
  global CLASS_NUMBER
  global PIECES
  global SPECIES
  global CLASSES

  reset_all_buttons()

  BUTTONS[piece_name][0].config(bg = "red")

  highlight_species(piece_name)

  species = PIECES[piece_name][0].split('/')
  SPECIES_NUMBER_1.config(text = SPECIES[species[0]][0])
  SPECIES_DESCRIPTION_1.config(text = SPECIES[species[0]][1])

  CLASS_NUMBER.config(text = CLASSES[PIECES[piece_name][1]][0])
  CLASS_DESCRIPTION.config(text = CLASSES[PIECES[piece_name][1]][1])

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
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global SPECIES_DESCRIPTION_2
  global SPECIES_NUMBER_2
  global CLASS_DESCRIPTION
  global CLASS_NUMBER

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

  color1 = Label(window, bg = "green", width = 4, height = 1)
  color1.grid(column = 0, row = 12)

  SPECIES_NUMBER_1 = Label(window, font=("Arial Bold", 12))
  SPECIES_NUMBER_1.grid(column = 1, row = 12, columnspan = 2)

  SPECIES_DESCRIPTION_1 = Label(window, font=("Arial Bold", 12))
  SPECIES_DESCRIPTION_1.grid(column = 3, row = 12, columnspan = 10)

  color2 = Label(window, bg = "green", width = 4, height = 1)
  color2.grid(column = 0, row = 13)

  SPECIES_NUMBER_2 = Label(window, font=("Arial Bold", 12))
  SPECIES_NUMBER_2.grid(column = 1, row = 13, columnspan = 2)

  SPECIES_DESCRIPTION_2 = Label(window, font=("Arial Bold", 12))
  SPECIES_DESCRIPTION_2.grid(column = 3, row = 13, columnspan = 10)

  color3 = Label(window, bg = "blue", width = 4, height = 1)
  color3.grid(column = 0, row = 14)

  CLASS_NUMBER = Label(window, font=("Arial Bold", 12))
  CLASS_NUMBER.grid(column = 1, row = 14, columnspan = 2)

  CLASS_DESCRIPTION = Label(window, font=("Arial Bold", 12))
  CLASS_DESCRIPTION.grid(column = 3, row = 14, columnspan = 10)

  color4 = Label(window, bg = "#7742f4", width = 4, height = 1)
  color4.grid(column = 0, row = 15)

  both_description = Label(window, text = "Both pieces and class matches", font=("Arial Bold", 12))
  both_description.grid(column = 1, row = 15, columnspan = 10)

  window.mainloop()

def main():
  load_pieces()

  load_species()

  load_classes()

  make_window()

if __name__ == '__main__':
  main()
