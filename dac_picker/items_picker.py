#!/usr/bin/env python3

from tkinter import Tk, Label, Button, Frame
from PIL import ImageTk,Image
from pkg_resources import resource_filename
from .version import VERSION
from .database import Csv


_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_GREEN_COLOR = "#66ce54"
_YELLOW_COLOR = "#f9ef31"
_RED_COLOR = "#ff4f4f"

ITEMS = {}
BUTTONS = {}

ITEM_DESCRIPTION = None


def reset_all_buttons():
    global BUTTONS

    for key, value in BUTTONS.items():
      value[0].config(bg = _DEFAULT_COLOR)


def highlight_components(item_name):
    global ITEMS
    global _GREEN_COLOR
    global _YELLOW_COLOR
    global _RED_COLOR

    components = [component.strip() for component in ITEMS[item_name][1].split(',')]

    if not components:
        return

    for component in components:
        if not component:
            continue

        if BUTTONS[component][0].cget("bg") == _GREEN_COLOR:
            BUTTONS[component][0].config(bg = _YELLOW_COLOR)
        elif BUTTONS[component][0].cget("bg") != _RED_COLOR:
            BUTTONS[component][0].config(bg = _GREEN_COLOR)


def highlight_upgrades(item_name):
    global ITEMS
    global _AZURE_COLOR

    for key, value in ITEMS.items():
        if item_name in value[1] and BUTTONS[key][0].cget("bg") != _RED_COLOR:
            BUTTONS[key][0].config(bg = _AZURE_COLOR)


def button_click(item_name):
    global BUTTONS
    global ITEMS
    global ITEM_DESCRIPTION
    global _RED_COLOR

    reset_all_buttons()

    BUTTONS[item_name][0].config(bg = _RED_COLOR)

    ITEM_DESCRIPTION.config(text = ITEMS[item_name][0])

    highlight_components(item_name)

    highlight_upgrades(item_name)


def add_button(window, handler, item_name, tier, column, row):
    button = Button(window)
    button.grid(column = column, row = row)

    resource = resource_filename("dac_picker",
        "images/items/" + item_name + ".png")

    img = ImageTk.PhotoImage(Image.open(resource))
    tier_text = "* " * int(tier) if tier.isdigit() else tier

    button.config(image = img, command = lambda:handler(item_name),
        compound = "top", text = tier_text, font=("Arial Bold", 5),
        pady = 0, padx = 0)

    return button, img


def add_buttons(window):
    global BUTTONS
    global ITEMS

    row = 0
    column = 0

    for key, value in sorted(ITEMS.items()):
        BUTTONS[key] = add_button(window, button_click, key, value[2],
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

    window.title("Dota Auto Chess Items Picker " + VERSION)

    buttons_frame = Frame(height = 2, bd = 1, relief = "sunken")
    buttons_frame.pack(fill = "both", expand = True)

    add_buttons(buttons_frame)

    info_frame = Frame(height = 2, bd = 1, relief = "sunken")
    info_frame.pack(fill = "both", expand = True)

    ITEM_DESCRIPTION = Label(info_frame, font=("Arial Bold", 12),
        wraplength=400, anchor="nw", justify="left")

    ITEM_DESCRIPTION.grid(column = 0, row = 0, sticky = 'W', padx = (30, 0))

    window.mainloop()


def main():
    global ITEMS

    ITEMS = Csv.load("database/csv/items.csv", 3)

    make_window()


if __name__ == '__main__':
  main()
