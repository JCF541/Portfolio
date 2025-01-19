import tkinter as tk

class BoardView:
    def __init__(self, root, grid_map):
        self.root = root
        self.grid_map = grid_map
        self.buttons = []

    def display_board(self):
        """Render the grid as a Tkinter GUI."""
        for row in range(self.grid_map.height):
            button_row = []
            for col in range(self.grid_map.width):
                tile = self.grid_map.grid[row][col]
                text = tile.unit.name[0].upper() if tile.unit else self._terrain_symbol(tile.terrain)
                button = tk.Button(
                    self.root,
                    text=text,
                    width=3,
                    height=1,
                    relief=tk.RIDGE,
                    bg=self._terrain_color(tile.terrain),
                )
                button.grid(row=row, column=col, sticky="nsew")
                button_row.append(button)
            self.buttons.append(button_row)

    def update_tile(self, x, y):
        """Update a specific tile based on its current state."""
        tile = self.grid_map.grid[y][x]
        text = tile.unit.name[0].upper() if tile.unit else self._terrain_symbol(tile.terrain)
        self.buttons[y][x].config(text=text, bg=self._terrain_color(tile.terrain))

    @staticmethod
    def _terrain_symbol(terrain):
        """Return a symbol to represent the terrain."""
        symbols = {'grass': '.', 'water': '~', 'mountain': '^', 'road': '#'}
        return symbols.get(terrain, '?')

    @staticmethod
    def _terrain_color(terrain):
        """Return a color for the terrain."""
        colors = {'grass': 'green', 'water': 'blue', 'mountain': 'gray', 'road': 'brown'}
        return colors.get(terrain, 'white')
