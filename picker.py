#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk,Image

VERSION = "0.1"

PIECES = [
  "abaddon",
  "alchemist",
  "anti-mage",
  "axe",
  "batrider",
  "beastmaster",
  "bounty_hunter",
  "chaos_knight",
  "clockwerk",
  "crystal_maiden",
  "disruptor",
  "doom",
  "dragon_knight",
  "drow_ranger",
  "enchantress",
  "enigma",
  "gyrocopter",
  "juggernaut",
  "keeper_of_the_light",
  "kunkka",
  "lich",
  "lina",
  "lone_druid",
  "luna",
  "lycan",
  "medusa",
  "morphling",
  "natures_prophet",
  "necrophos",
  "ogre_magi",
  "omniknight",
  "phantom_assassin",
  "puck",
  "queen_of_pain",
  "razor",
  "sand_king",
  "shadow_fiend",
  "shadow_shaman",
  "slardar",
  "slark",
  "sniper",
  "techies",
  "templar_assassin",
  "terrorblade",
  "tidehunter",
  "timbersaw",
  "tinker",
  "tiny",
  "treant_protector",
  "troll_warlord",
  "tusk",
  "venomancer",
  "viper",
  "windranger",
  "witch_doctor",
]

BUTTONS = {}

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

  window.title("Dota Auto Chess Picker " + VERSION)

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
  make_window()

if __name__ == '__main__':
  main()
