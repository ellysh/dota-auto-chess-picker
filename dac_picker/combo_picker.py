#!/usr/bin/env python3

from tkinter import ttk, Tk, Label, Button
from PIL import ImageTk,Image
from pkg_resources import resource_filename
from .version import VERSION
from .database import Csv


_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_GREEN_COLOR = "#66ce54"
_PURPLE_COLOR = "#8757f9"
_RED_COLOR = "#ff4f4f"

PIECES = {}
COMBOS = {}

PICKED_PIECES = set()
BUTTONS = []
WIDGETS = []


def reset_all_buttons():
    global BUTTONS
    global _DEFAULT_COLOR

    for button in BUTTONS:
        button[1].config(bg = _DEFAULT_COLOR)

def highlight_piece():
    global BUTTONS
    global _RED_COLOR
    global PICKED_PIECES

    if not PICKED_PIECES:
        return

    for button in BUTTONS:
        if button[0] in PICKED_PIECES:
            button[1].config(bg = _RED_COLOR)

def highlight_species():
    global PIECES
    global BUTTONS
    global _GREEN_COLOR
    global PICKED_PIECES

    if not PICKED_PIECES:
        return

    species = []
    for piece in PICKED_PIECES:
        species.extend(PIECES[piece][0].split('/'))

    for button in BUTTONS:
        button_species = PIECES[button[0]][0].split('/')

        if not set(species).isdisjoint(button_species):
            button[1].config(bg = _GREEN_COLOR)


def highlight_class():
    global PIECES
    global BUTTONS
    global _AZURE_COLOR
    global _PURPLE_COLOR

    if not PICKED_PIECES:
        return

    classes = []
    for piece in PICKED_PIECES:
        classes.extend(PIECES[piece][1].split('/'))

    for button in BUTTONS:
        button_classes = PIECES[button[0]][1].split('/')

        if not set(classes).isdisjoint(button_classes):
            if button[1].cget("bg") == _DEFAULT_COLOR:
                color = _AZURE_COLOR
            else:
                color = _PURPLE_COLOR

            button[1].config(bg = color)


def add_remove_picked_piece(piece_name):
    global PICKED_PIECES

    if piece_name in PICKED_PIECES:
        PICKED_PIECES.remove(piece_name)
    else:
        PICKED_PIECES.add(piece_name)


def button_click(piece_name):
    add_remove_picked_piece(piece_name)

    reset_all_buttons()

    highlight_species()

    highlight_class()

    highlight_piece()


def add_button(window, piece, level, column, row):
    button = Button(window)
    button.grid(column = column, row = row)

    resource = resource_filename("dac_picker", "images/pieces/" + piece + ".png")

    img = ImageTk.PhotoImage(Image.open(resource))

    button.config(image = img, command = lambda:button_click(piece),
        compound = "top", text = '* ' * int(level),
        font=("Arial Bold", 5), pady = 0, padx = 0)

    return [piece, button, img]


def sort_priority(val):
    return val[0]


def add_combos(window, game_phase):
    global BUTTONS
    global PIECES
    global COMBOS

    row = 0

    combos = COMBOS[game_phase]
    combos.sort(key = sort_priority)

    for combo in combos:
        name_label = Label(window, font=("Arial Bold", 10), text = combo[1])
        name_label.grid(column = 0, row = row)

        WIDGETS.append(name_label)

        line_label = Label(window, font=("Arial Bold", 10), text = combo[2])
        line_label.grid(column = 1, row = row)

        WIDGETS.append(line_label)

        pieces = [x.strip() for x in combo[3].split(',')]

        column = 2
        for piece in pieces:
            BUTTONS.append(add_button(window, piece, PIECES[piece][2],
                column, row))

            column += 1

        row += 1


def reset_picked_pieces():
    global BUTTONS
    global PICKED_PIECES

    PICKED_PIECES = set()

    reset_all_buttons()


def make_window():
    global VERSION

    window = Tk()

    window.title("Dota Auto Chess Strategy Picker " + VERSION)

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

    window.bind('<Escape>', lambda event: reset_picked_pieces())

    window.mainloop()


def main():
    global PIECES
    global COMBOS

    PIECES = Csv.load("database/csv/pieces.csv", 4)

    COMBOS = Csv.load_combos("database/csv/combos.csv")

    make_window()


if __name__ == '__main__':
  main()
