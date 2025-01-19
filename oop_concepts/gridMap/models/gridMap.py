import random
from noise import pnoise2  # Install with pip install noise
from .tile import Tile

class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Tile() for _ in range(width)] for _ in range(height)]

    def generate_terrain(self):
        """Improved terrain generation for balanced tactical gameplay."""
        # Step 1: Initialize all tiles as grass
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col].terrain = 'grass'

        # Step 2: Add natural features using Perlin noise
        self._apply_perlin_noise('mountain', threshold=0.6, scale=15)
        self._apply_perlin_noise('water', threshold=0.4, scale=10)

        # Step 3: Add strategic road networks
        self._place_roads()

        # Step 4: Reserve starting zones for players
        self._reserve_player_zones()

    def _apply_perlin_noise(self, terrain, threshold, scale):
        """Use Perlin noise to create clusters of terrain."""
        seed = random.randint(0, 100)
        for row in range(self.height):
            for col in range(self.width):
                noise_value = pnoise2(row / scale, col / scale, base=seed)
                if noise_value > threshold:
                    self.grid[row][col].terrain = terrain

    def _place_roads(self):
        """Create a connected road network."""
        road_segments = 3
        for _ in range(road_segments):
            start_x = random.randint(0, self.width - 1)
            start_y = random.randint(0, self.height - 1)
            length = random.randint(7, 15)
            x, y = start_x, start_y
            for _ in range(length):
                self.grid[y][x].terrain = 'road'
                direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
                x += direction[0]
                y += direction[1]
                if not (0 <= x < self.width and 0 <= y < self.height):
                    break

    def _reserve_player_zones(self):
        """Reserve zones for player starting positions."""
        margin = 2
        player_zone_size = 3
        zones = [
            (margin, margin),  # Top-left corner
            (self.width - margin - player_zone_size, margin),  # Top-right corner
            (margin, self.height - margin - player_zone_size),  # Bottom-left corner
            (self.width - margin - player_zone_size, self.height - margin - player_zone_size),  # Bottom-right corner
        ]

        for zone in zones:
            x_start, y_start = zone
            for y in range(y_start, y_start + player_zone_size):
                for x in range(x_start, x_start + player_zone_size):
                    if 0 <= x < self.width and 0 <= y < self.height:
                        self.grid[y][x].terrain = 'grass'

    def display_grid(self):
        """Print the grid to the console for debugging and show tile statistics."""
        terrain_count = {}
        for row in self.grid:
            line = "".join(self._terrain_symbol(tile.terrain) for tile in row)
            print(line)
            for tile in row:
                terrain_count[tile.terrain] = terrain_count.get(tile.terrain, 0) + 1
        print("\nTile Distribution:")
        for terrain, count in terrain_count.items():
            print(f"{terrain.capitalize()}: {count} tiles")

    @staticmethod
    def _terrain_symbol(terrain):
        """Return a symbol to represent the terrain."""
        symbols = {'grass': '.', 'water': '~', 'mountain': '^', 'road': '#'}
        return symbols.get(terrain, '?')
