#!/usr/bin/env python3

from tkinter import Tk, Label, Button, Frame
from PIL import ImageTk,Image
from pkg_resources import resource_filename
from .version import VERSION
from .database import Csv


_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_BLUE_COLOR = "#144593"
_GREEN_COLOR = "#66ce54"
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

SKILL_DESCRIPTION = None

BUTTONS = {}

def reset_all_buttons():
    global BUTTONS

    for key, value in BUTTONS.items():
        value[0].config(bg = _DEFAULT_COLOR)


def highlight_similarity(piece_name, index, first_color, second_color):
    global PIECES
    global _PURPLE_COLOR

    similarity_list = PIECES[piece_name][index].split('/')

    for key, value in BUTTONS.items():
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
    global SKILL_DESCRIPTION
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

    if PIECES[piece_name][1] in CLASSES.keys():
        CLASS_NUMBER.config(text = CLASSES[PIECES[piece_name][1]][0])
        CLASS_DESCRIPTION.config(text = CLASSES[PIECES[piece_name][1]][1])

    SKILL_DESCRIPTION.config(text = PIECES[piece_name][3])


def add_button(window, button_click, piece, level, column, row):
    button = Button(window)
    button.grid(column = column, row = row)

    resource = resource_filename("dac_picker", "images/pieces/" + piece + ".png")

    img = ImageTk.PhotoImage(Image.open(resource))

    button.config(image = img, command = lambda:button_click(piece),
                  compound = "top", text = '* ' * int(level),
                  font=("Arial Bold", 5), pady = 0, padx = 0)

    return button, img


def add_buttons(window):
    global BUTTONS
    global PIECES

    row = 0
    column = 0

    for key, value in sorted(PIECES.items()):
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
    global SKILL_DESCRIPTION
    global _PURPLE_COLOR
    global _GREEN_COLOR
    global _YELLOW_COLOR
    global _AZURE_COLOR
    global _RED_COLOR

    window = Tk()

    window.title("Dota Auto Chess Pieces Picker " + VERSION)

    buttons_frame = Frame(height = 2, bd = 1, relief = "sunken")
    buttons_frame.pack(fill = "both", expand = True)

    add_buttons(buttons_frame)

    info_frame = Frame(height = 2, bd = 1, relief = "sunken")
    info_frame.pack(fill = "both", expand = True)


    color1 = Label(info_frame, bg = _GREEN_COLOR, width = 4, height = 1)
    color1.grid(column = 0, row = 0)

    color2 = Label(info_frame, bg = _YELLOW_COLOR, width = 4, height = 1)
    color2.grid(column = 0, row = 1)

    color3 = Label(info_frame, bg = _AZURE_COLOR, width = 4, height = 1)
    color3.grid(column = 0, row = 2)

    color4 = Label(info_frame, bg = _PURPLE_COLOR, width = 4, height = 1)
    color4.grid(column = 0, row = 3)

    color5 = Label(info_frame, bg = _RED_COLOR, width = 4, height = 1)
    color5.grid(column = 0, row = 4)


    SPECIES_NUMBER_1 = Label(info_frame, font=("Arial Bold", 12))
    SPECIES_NUMBER_1.grid(column = 1, row = 0, sticky = 'W', padx = (10, 0))

    SPECIES_NUMBER_2 = Label(info_frame, font=("Arial Bold", 12))
    SPECIES_NUMBER_2.grid(column = 1, row = 1, sticky = 'W', padx = (10, 0))

    CLASS_NUMBER = Label(info_frame, font=("Arial Bold", 12))
    CLASS_NUMBER.grid(column = 1, row = 2, sticky = 'W', padx = (10, 0))


    SPECIES_DESCRIPTION_1 = Label(info_frame, font=("Arial Bold", 12),
        wraplength=300, anchor="nw", justify="left")

    SPECIES_DESCRIPTION_1.grid(column = 2, row = 0, sticky = 'W',
        padx = (10, 0))

    SPECIES_DESCRIPTION_2 = Label(info_frame, font=("Arial Bold", 12),
        wraplength=300, anchor="nw", justify="left")

    SPECIES_DESCRIPTION_2.grid(column = 2, row = 1, sticky = 'W', padx = (10, 0))

    CLASS_DESCRIPTION = Label(info_frame, font=("Arial Bold", 12),
        wraplength=300, anchor="nw", justify="left")

    CLASS_DESCRIPTION.grid(column = 2, row = 2, sticky = 'W', padx = (10, 0))

    both_description = Label(info_frame, text = "Both species and class matches",
        font=("Arial Bold", 12), wraplength=300, anchor="nw",
        justify="left")
    both_description.grid(column = 2, row = 3, sticky = 'W', padx = (10, 0))

    SKILL_DESCRIPTION = Label(info_frame, font=("Arial Bold", 12),
        wraplength=300, anchor="nw", justify="left")
    SKILL_DESCRIPTION.grid(column = 2, row = 4, sticky = 'W', padx = (10, 0))

    window.mainloop()


def main():
    global PIECES
    global SPECIES
    global CLASSES

    PIECES = Csv.load("database/csv/pieces.csv", 4)

    SPECIES = Csv.load("database/csv/species.csv", 2)

    CLASSES = Csv.load("database/csv/classes.csv", 2)

    make_window()


if __name__ == '__main__':
  main()
