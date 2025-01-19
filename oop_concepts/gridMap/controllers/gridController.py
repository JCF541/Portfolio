from models.unit import Unit

class GridController:
    def __init__(self, grid_map, view):
        self.grid_map = grid_map
        self.view = view

    def generate_map(self):
        """Generate the terrain map."""
        self.grid_map.generate_terrain()
        self.view.display_map(self.grid_map)

    def add_unit(self, x, y, name, initiative):
        """Add a unit to the grid."""
        unit = Unit(name, initiative)
        self.grid_map.place_unit(x, y, unit)
        self.view.display_map(self.grid_map)