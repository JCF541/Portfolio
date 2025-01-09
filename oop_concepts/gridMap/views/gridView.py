
class GridView:
    def display_map(self, grid_map):
        """Displays the grid with terrain and units."""
        for row in grid_map.grid:
            row_display = []
            for tile in row:
                if tile.unit:
                    row_display.append(tile.unit.name[0].upper())  # Unit's initial
                else:
                    terrain_symbol = {
                        'grass': '.',
                        'water': '~',
                        'mountain': '^'
                    }
                    row_display.append(terrain_symbol[tile.terrain])
            print(" ".join(row_display))
        print()