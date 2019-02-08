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

  window.title("Dota Auto Chess Picker " + _VERSION)

  add_buttons(window)

  window.mainloop()

def main():
  load_pieces()

  load_combos()

  make_window()

if __name__ == '__main__':
  main()
