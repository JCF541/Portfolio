"""
Library Management Application
==============================
Entry point to launch the GUI.
"""

from tkinter import Tk
from gui.gui import AppGUI

if __name__ == "__main__":
    root = Tk()
    app = AppGUI(root)
    root.mainloop()
