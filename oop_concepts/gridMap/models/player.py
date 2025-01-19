class Player:
    def __init__(self, name):
        self.name = name
        self.units = []  # List of units belonging to the player

    def add_unit(self, unit):
        self.units.append(unit)