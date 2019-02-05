#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.3"
_PIECES_FILE = "database/csv/pieces.csv"
_SPECIES_FILE = "database/csv/species.csv"
_CLASSES_FILE = "database/csv/classes.csv"

_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_BLUE_COLOR = "#144593"
_GREEN_COLOR = "#71cc61"
_YELLOW_COLOR = "#f9ef31"
_PURPLE_COLOR = "#8757f9"
_RED_COLOR = "#ff4f4f"

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

def load_table(filename, table, max_column):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
      if max_column == 3:
        table[line[0]] = [line[1], line[2], line[3]]
      else:
        table[line[0]] = [line[1], line[2]]

def load_pieces():
  global PIECES

  load_table(_PIECES_FILE, PIECES, 3)

def load_species():
  global SPECIES

  load_table(_SPECIES_FILE, SPECIES, 2)

def load_classes():
  global CLASSES

  load_table(_CLASSES_FILE, CLASSES, 2)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_similarity(piece_name, index, first_color, second_color):
  global PIECES
  global _PURPLE_COLOR

  similarity_list = PIECES[piece_name][index].split('/')

  for key, value in BUTTONS.iteritems():
    check_similarity_list = PIECES[key][index].split('/')

    if key != piece_name:
      color = _DEFAULT_COLOR

      if similarity_list[0] in check_similarity_list:
        color = first_color
      elif 1 < len(similarity_list) \
           and similarity_list[1] in check_similarity_list:
        color = second_color

      if value[0].cget("bg") == _DEFAULT_COLOR:
        value[0].config(bg = color)
      elif color != _DEFAULT_COLOR:
        value[0].config(bg = _PURPLE_COLOR)

def highlight_species(piece_name):
  global _AZURE_COLOR
  global _BLUE_COLOR
  global _GREEN_COLOR
  global _YELLOW_COLOR

  highlight_similarity(piece_name, 0, _GREEN_COLOR, _YELLOW_COLOR)

  highlight_similarity(piece_name, 1, _AZURE_COLOR, _BLUE_COLOR)

def button_click(piece_name):
  global BUTTONS
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global SPECIES_DESCRIPTION_2
  global SPECIES_NUMBER_2
  global CLASS_DESCRIPTION
  global CLASS_NUMBER
  global PIECES
  global SPECIES
  global CLASSES
  global _RED_COLOR

  reset_all_buttons()

  BUTTONS[piece_name][0].config(bg = _RED_COLOR)

  highlight_species(piece_name)

  species = PIECES[piece_name][0].split('/')
  SPECIES_NUMBER_1.config(text = SPECIES[species[0]][0])
  SPECIES_DESCRIPTION_1.config(text = SPECIES[species[0]][1])

  if 1 < len(species):
    SPECIES_NUMBER_2.config(text = SPECIES[species[1]][0])
    SPECIES_DESCRIPTION_2.config(text = SPECIES[species[1]][1])
  else:
    SPECIES_NUMBER_2.config(text = "")
    SPECIES_DESCRIPTION_2.config(text = "")

  CLASS_NUMBER.config(text = CLASSES[PIECES[piece_name][1]][0])
  CLASS_DESCRIPTION.config(text = CLASSES[PIECES[piece_name][1]][1])

def add_button(window, button_click, piece, level, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/pieces/" + piece + ".png"))

  button.config(image = img, command = lambda:button_click(piece), \
                compound = TOP, text = '* ' * int(level), \
                font=("Arial Bold", 4), pady = 0, padx = 0)

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
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global SPECIES_DESCRIPTION_2
  global SPECIES_NUMBER_2
  global CLASS_DESCRIPTION
  global CLASS_NUMBER
  global _PURPLE_COLOR
  global _GREEN_COLOR
  global _YELLOW_COLOR
  global _AZURE_COLOR

  window = Tk()

  window.title("Dota Auto Chess Picker " + _VERSION)

  add_buttons(window)

  color1 = Label(window, bg = _GREEN_COLOR, width = 4, height = 1)
  color1.grid(column = 0, row = 12)

  SPECIES_NUMBER_1 = Label(window, font=("Arial Bold", 12))
  SPECIES_NUMBER_1.grid(column = 1, row = 12, columnspan = 2)

  SPECIES_DESCRIPTION_1 = Label(window, font=("Arial Bold", 12), \
                                wraplength=300, anchor=NW, justify=LEFT)
  SPECIES_DESCRIPTION_1.grid(column = 3, row = 12, columnspan = 10)

  color2 = Label(window, bg = _YELLOW_COLOR, width = 4, height = 1)
  color2.grid(column = 0, row = 13)

  SPECIES_NUMBER_2 = Label(window, font=("Arial Bold", 12))
  SPECIES_NUMBER_2.grid(column = 1, row = 13, columnspan = 2)

  SPECIES_DESCRIPTION_2 = Label(window, font=("Arial Bold", 12), \
                                wraplength=300, anchor=NW, justify=LEFT)
  SPECIES_DESCRIPTION_2.grid(column = 3, row = 13, columnspan = 10)

  color3 = Label(window, bg = _AZURE_COLOR, width = 4, height = 1)
  color3.grid(column = 0, row = 14)

  CLASS_NUMBER = Label(window, font=("Arial Bold", 12))
  CLASS_NUMBER.grid(column = 1, row = 14, columnspan = 2)

  CLASS_DESCRIPTION = Label(window, font=("Arial Bold", 12), \
                            wraplength=300, anchor=NW, justify=LEFT)
  CLASS_DESCRIPTION.grid(column = 3, row = 14, columnspan = 10)

  color4 = Label(window, bg = _PURPLE_COLOR, width = 4, height = 1)
  color4.grid(column = 0, row = 15)

  both_description = Label(window, text = "Both species and class \
matches", font=("Arial Bold", 12), wraplength=300, anchor=NW, \
    justify=LEFT)
  both_description.grid(column = 1, row = 15, columnspan = 10)

  window.mainloop()

def main():
  load_pieces()

  load_species()

  load_classes()

  make_window()

if __name__ == '__main__':
  main()
