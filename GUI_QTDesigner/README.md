	Some Python GUI examples with Qt Designer (Qt Creator)


##  Cheat Sheet Ubuntu 17.10

### Python 3

 * sudo apt install python3-pip
 * sudo apt  install python3-pyqt5

### Python 2

 * sudo apt install python-pip
 * sudo apt  install python-pyqt5

## For Qt5 Designer and utilities  (qtcreator in Ubuntu Linux)

 * sudo apt-get install qttools5-dev-tools
 * sudo apt-get install qtcreator
 * sudo apt install pyqt5-dev-tools


Run this command to make the Python code from the designer .ui file : pyuic5 -x firstgui.ui -o firstgui.py


## Git 
 * sudo apt install git
 * git clone https://github.com/jarleven/Python.git
 * git pull
 * git add 
 * git commit prog.py -m "Change comment" 
 * git push


## Make an executable

	pip3 install pyinstaller

	sudo find / -name pyinstaller

	~/.local/bin/pyinstaller prog.py

	~/.local/bin/pyinstaller --onefile prog.py

##  Cheat Sheet Windows 10

Will add stuff here later (25.Feb 2018)
C:\python>pyuic5 -x firstgui.ui -o firstgui.py

Run Python commands in WinPython by startring the "WinPython Command Prompt" found in the C:\WinPython-XXX folder.
Commands like pip3 install pyinstaller are accessible from the "WinPython Command Prompt".

## Resources

 * http://www.pyinstaller.org/
 * https://winpython.github.io/
 

## Inspiration and copy paste from the following sites

I hope I got to include most of the inspiration I found while googling for how to build a simple Python Qt GUI application.
I will try to add all sites I have used as examples and inspiration. (Will update this list 25.Feb 2018)


 * http://pyinstaller.readthedocs.io/en/stable/installation.html
 * https://askubuntu.com/questions/651461/where-is-qt5-designer
 * https://stackoverflow.com/questions/11720835/how-can-i-make-a-application-with-single-exe-file-using-python
