# Dota Auto Chess Picker 0.5 version

Dota Auto Chess Picker is a utility to check combinations of pieces and items for the [Dota Auto Chess](https://steamcommunity.com/sharedfiles/filedetails/?id=1613886175) custom game.

A current development state is available in the [`CHANGELOG.md`](CHANGELOG.md) file.

## Installation

You need two Python 2.7, Tkinter and pillow modules to launch the Dota Auto Chess Picker.

### Windows

These are steps to install Python and required modules on Windows:

1. Download the archive with Dota Auto Chess Picker and extract it:<br/>
https://github.com/ellysh/dota-auto-chess-picker/archive/master.zip

2. Download the Python 2.7 distribution:<br/>
https://www.python.org/downloads/release/python-2715/

3. Install Python 2.7.

4. Install the pip utility with the following command in the command line:<br/>
`python get-pip.py`

5. Install the `pillow` module:<br/>
`pip install pillow`

### Linux

These are steps to install Python and required modules on Linux:

1. Download the archive with Dota Auto Chess Picker and extract it:<br/>
https://github.com/ellysh/dota-auto-chess-picker/archive/master.zip

2. Install the Tkinter module:<br/>
`sudo apt-get install python-tk`

3. Install the `pillow` module:<br/>
`pip install pillow`

## Usage

### Pieces Picker

The `pieces-picker.py` script shows you all combinations of the pieces depending on their species and classes.

![Pieces Picker](images/readme/pieces-picker-window.png)

Start the `pieces-picker.py` script and click on the piece icon. The green color will highlight all pieces of the same species. If the piece has second species, then corresponding pieces will be highlighted by the yellow color. Blue color highlights the pieces with the same class. Purple color matches the pieces with the same species and class.

Stars under each piece icon show its cost.

### Items Picker

The `items-picker.py` script shows you combinations of items.

![Items Picker](images/readme/items-picker-window.png)

Start the `items-picker.py` script and click on the item icon. The red color will highlight the selected item. You will see a description of this item at the bottom of the window. If the item can be combined in the upgrade, it will be marked by the blue color. The green color will highlight all components (if they exist) of the selected item.

Let us consider the screenshot above. The select item is Maelstorm. You can combine it with Hyperstone for getting Mjollnir. So, Mjollnir is marked by the blue color.  You can get Maelstorm by the combination of Javelin and Mithril Hammer. Thus, these two items are highlighted by the green color.

Stars under each item icon show its tier. The `U` letter means that this is an upgraded item.

### Combos Picker

The `combos-picker.py` script shows you combinations of pieces according to predefined strategies.

![Combos Picker](images/readme/combos-picker-window.png)

Start the script and click on the piece icon, which you have bought at the current round. The red color will highlight the selected piece. The green color will highlight all pieces which can make a combo with the selected one. You should follow the recommendation and click to the highlighted pieces when you buy them. Then you meet the recommended strategy.

The strategies are defined in the `database/docs/Database.odt` file. These are steps to add your own strategy:

1. Switch to the `COMBOS` sheet of the document.
2. Add the name of your combo in the first column.
3. Add comma separated pieces of your combo in the second column. Use pieces names from the `PIECES` sheet of the document.
4. Use the `database/ods2csv.sh` script for generating all CSV documents. If you do not have Bash, you can manually save the `COMBOS` sheet to the `database/csv` directory with the `combos.csv` name. Use the `;` as a separator for CSV document.

Now the `combos-picker.py` script will highlight your combo.

## Contacts

You can ask any questions about usage of Dota Auto Chess Picker via email petrsum@gmail.com.

## License

This project is distributed under the GPL v3.0 license
