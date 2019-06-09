# Dota Auto Chess Picker 1.3.6 version

Dota Auto Chess Picker is a utility for showing combinations of pieces and items for the [Dota Auto Chess](https://steamcommunity.com/sharedfiles/filedetails/?id=1613886175) custom game. You can use the picker during the game (as a hint) or for planning your strategies.

A current development state is available in the [`CHANGELOG.md`](CHANGELOG.md) file.

## Installation

You need two Python 3, Tkinter and Pillow modules to launch the Dota Auto Chess Picker.

### Windows

These are steps to install dac-picker on Windows:

1. Download the Python 3 distribution:<br/>
https://www.python.org/downloads/release/python-373/

2. Install Python 3.

3. Install the pip utility with the following command in the [command prompt](https://www.computerhope.com/issues/chusedos.htm):<br/>
`python get-pip.py`

4. Install Dota Auto Chess Picker:<br/>
`python -m pip install --user dac-picker`

This is an alternative way to install dac-picker from github repository:

1. Install the `pillow` module:<br/>
`python -m pip install pillow`

2. Install the `setuptools` module:<br/>
`python -m pip install setuptools`

3. Download the archive with the dac-picker and extract it:<br/>
https://github.com/ellysh/dota-auto-chess-picker/archive/master.zip

4. Change directory to the `dota-auto-chess-picker` and launch the command:<br/>
`python setup.py install --user`

In both variants, dac-picker will be installed to the following directory (example for Python 3.6 version):<br/>
`C:\Users\<username>\AppData\Roaming\Python\Python36\Sripts`

### Ubuntu

These are steps to install dac-picker on Linux:

1. Install the Python 3:<br/>
`sudo apt-get install python3`

2. Install the Tkinter module:<br/>
`sudo apt-get install python3-tk`

3. Install the pip package manager:<br/>
`sudo apt-get install python3-pip`

4. Install Dota Auto Chess Picker:<br/>
`pip3 install dac-picker`

Dac-picker will be installed to the `/usr/local/bin/` directory.

This is an alternative way to install dac-picker from github repository:

1. Install the `pillow` module:<br/>
`sudo apt-get install python3-pil.imagetk`

2. Install the `setuptools` module:<br/>
`pip install setuptools`

3. Download the archive with the `dota-auto-chess-picker` and extract it:<br/>
https://github.com/ellysh/dota-auto-chess-picker/archive/master.zip

4. Change directory to the `dac-picker` and launch the command:<br/>
`python setup.py install --user`

Dac-picker will be installed to the `~/.local/bin` directory.

## Usage

### Pieces Picker

The `dac-pieces-picker` script shows you all combinations of the pieces depending on their species and classes.

![Pieces Picker](dac_picker/images/readme/pieces-picker-window.png)

Start the `dac-pieces-picker` script and click on the piece icon. The green color highlights all pieces of the same species. If the piece has second species, then corresponding pieces are highlighted by the yellow color. Blue color highlights the pieces with the same class. Purple color matches the pieces with the same species and class.

You will see a brief description of the piece's skill near the red box.

Stars under each piece icon show its cost.

### Items Picker

The `dac-items-picker` script shows you combinations of items.

![Items Picker](dac_picker/images/readme/items-picker-window.png)

Start the `dac-items-picker` script and click on the item icon. The red color highlights the selected item. You will see a description of this item at the bottom of the window. If the item can be combined in the upgrade, it is marked by the blue color. The green color highlights all components (if they exist) of the selected item. If the upgrade consists of two similar items, the corresponding item icon is highlighted by the yellow color.

Let us consider the screenshot above. The select item is Maelstorm. You can combine it with Hyperstone for getting Mjollnir. So, Mjollnir is marked by a blue color. You can get Maelstorm by the combination of Javelin and Mithril Hammer. Thus, these two items are highlighted by the green color.

Stars under each item icon show its tier. The `U` letter means that this is an upgraded item.

### Combo Picker

The `dac-combo-picker` script shows you strong combinations of pieces for each phase of the game. Using these combinations you can build your own strategy. This script is recommended for advanced players.

![Combo Picker](dac_picker/images/readme/combo-picker-window.png)

You see three tabs when starting the script: "Earlygame", "Midgame" and "Lategame". On each tab, there are lines with recommended combos. There are three columns: name of the combo, the preferred line for pieces in this combo ("Front", "Back", "Mixed") and icons of pieces in this combo.

When you buy pieces of the specific combo you can press on corresponding icons. Then these pieces will be highlighted by the red color in all combos on all tabs. So, you can continue building your strategy considering the pieces which you already bought.

Also, the green color highlights all pieces with the same species as pieces which you already bought. The same way, blue color highlights all pieces with the same classes.

The combos are defined in the `combos.csv` database file.

This is the path to this file on Linux:<br/>
`~/.local/share/dac_picker/combos.csv`

This is the path to this file on Windows:<br/>
`C:\User\<username>\AppData\Local\dac_picker\combos.csv`

These are steps to add a new combo:

1. Open the CSV document. You can open this file in any text editor or MS/Libre Office application.
2. Add priority of your combo in the first column.
3. Add game phase of the combo in the second column.
4. Add the name of combo in the third column.
5. Add comma separated pieces of your combo in the fourth column. Use pieces names from the `pieces.csv` database file.
6. Save the modified `combos.csv` file.

Now the `dac-combo-picker` script shows your combo.

## Contacts

If you have any suggestions, bug reports or questions about usage of Dota Auto Chess Picker, please contact me via email petrsum@gmail.com.

## License

This project is distributed under the GPL v3.0 license
