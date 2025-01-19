import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ZoneAllocator:
    def __init__(self, grid_map):
        self.grid_map = grid_map

    def reserve_player_zones(self):
        logging.info("Reserving player zones.")
        margin = 2
        player_zone_size = 3
        zones = [
            (margin, margin),  # Top-left corner
            (self.grid_map.width - margin - player_zone_size, margin),  # Top-right
            (margin, self.grid_map.height - margin - player_zone_size),  # Bottom-left
            (self.grid_map.width - margin - player_zone_size, self.grid_map.height - margin - player_zone_size),  # Bottom-right
        ]

        for i, zone in enumerate(zones):
            logging.info(f"Reserving zone {i + 1} at {zone}.")
            x_start, y_start = zone
            for y in range(y_start, y_start + player_zone_size):
                for x in range(x_start, x_start + player_zone_size):
                    if 0 <= x < self.grid_map.width and 0 <= y < self.grid_map.height:
                        self.grid_map.grid[y][x].terrain = 'grass'
        logging.info("Player zones reserved.")
