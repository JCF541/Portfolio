from .gridController import GridController

class GridControllerWithGUI(GridController):
    def __init__(self, grid_map, view, board_view):
        super().__init__(grid_map, view)
        self.board_view = board_view

    def generate_map(self):
        """Generate the terrain map and update the GUI."""
        self.grid_map.generate_terrain()
        self.board_view.display_board()

    def add_unit(self, x, y, name, initiative):
        """Add a unit to the grid and update the GUI."""
        super().add_unit(x, y, name, initiative)
        self.board_view.update_tile(x, y)
