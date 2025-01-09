import random
from .tile import Tile
class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Tile() for _ in range(width)] for _ in range(height)]

    def generate_terrain(self):
        """Randomly generates terrain types for each tile."""
        terrain_types = ['grass', 'water', 'mountain']
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col].terrain = random.choice(terrain_types)

    def place_unit(self, x, y, unit):
        """Places a unit on a specific tile."""
        if self.grid[y][x].unit is None:
            self.grid[y][x].unit = unit
        else:
            raise ValueError(f"Tile ({x}, {y}) is already occupied!")