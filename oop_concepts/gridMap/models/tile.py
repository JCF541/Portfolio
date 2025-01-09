class Tile:
    def __init__(self, terrain='grass', unit=None):
        self.terrain = terrain
        self.unit = unit  # Holds a Unit object or None

    def is_walkable(self):
        """Check if the tile can be walked on."""
        return self.terrain != 'water' and self.unit is None