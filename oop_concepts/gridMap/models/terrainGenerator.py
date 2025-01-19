import random
import logging
from noise import pnoise2

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TerrainGenerator:
    def __init__(self, grid_map, config):
        self.grid_map = grid_map
        self.config = config

    def generate_terrain(self):
        logging.info("Starting terrain generation.")
        for terrain, settings in self.config.items():
            if terrain in ['grass', 'road']:
                continue
            logging.info(f"Generating terrain: {terrain}")
            if terrain == 'mountain':
                self._generate_edge_clusters(terrain, settings['threshold'], settings['scale'])
            elif terrain == 'water':
                self._generate_clustered_terrain(terrain, settings['threshold'], settings['scale'])
        logging.info("Terrain generation completed.")

    def _generate_clustered_terrain(self, terrain, threshold, scale):
        """Generate terrain clusters using Perlin noise and flood-fill."""
        seed = random.randint(0, 100)
        logging.info(f"Applying Perlin noise for {terrain} with seed={seed}, threshold={threshold}, scale={scale}.")
        for row in range(self.grid_map.height):
            for col in range(self.grid_map.width):
                noise_value = pnoise2(row / scale, col / scale, base=seed)
                if noise_value > threshold:
                    self._flood_fill(row, col, terrain, cluster_size=random.randint(5, 10))

    def _generate_edge_clusters(self, terrain, threshold, scale):
        """Generate mountains toward map edges."""
        seed = random.randint(0, 100)
        logging.info(f"Applying Perlin noise for {terrain} with seed={seed}, threshold={threshold}, scale={scale}.")
        for row in range(self.grid_map.height):
            for col in range(self.grid_map.width):
                # Edge proximity score to encourage mountain placement near edges
                edge_score = min(row, col, self.grid_map.height - row - 1, self.grid_map.width - col - 1)
                max_distance = min(self.grid_map.height, self.grid_map.width) // 3  # Mountain bias
                if edge_score <= max_distance:  # Favor edges
                    noise_value = pnoise2(row / scale, col / scale, base=seed)
                    if noise_value > threshold:
                        self._flood_fill(row, col, terrain, cluster_size=random.randint(4, 12))


    def _flood_fill(self, row, col, terrain, cluster_size):
        """Flood-fill algorithm to grow terrain clusters."""
        if cluster_size <= 0 or not (0 <= row < self.grid_map.height and 0 <= col < self.grid_map.width):
            return
        if self.grid_map.grid[row][col].terrain != 'grass':  # Only grow on default terrain
            return

        self.grid_map.grid[row][col].terrain = terrain
        cluster_size -= 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize direction growth
        for dx, dy in directions:
            self._flood_fill(row + dx, col + dy, terrain, cluster_size)
