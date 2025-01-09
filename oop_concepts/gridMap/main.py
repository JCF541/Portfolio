from models.gridMap import GridMap
from views.gridView import GridView
from controllers.guiController import GridControllerWithGUI
from gui.board import BoardView
import tkinter as tk


if __name__ == "__main__":
    # Initialize Model, View, and Controller
    width, height = 10, 10
    grid_map = GridMap(width, height)
    view = GridView()
    root = tk.Tk()
    root.title("Tactical Board")

    board_view = BoardView(root, grid_map)
    controller = GridControllerWithGUI(grid_map, view, board_view)

    # Generate terrain and display the board
    controller.generate_map()

    # Place some units
    controller.add_unit(2, 3, "Knight", 10)
    controller.add_unit(5, 5, "Archer", 15)

    root.mainloop()