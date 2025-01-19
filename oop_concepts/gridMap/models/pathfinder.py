import heapq
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PathPlanner:
    def __init__(self, grid_map, config):
        self.grid_map = grid_map
        self.config = config
        self.movement_costs = {'grass': 1, 'road': 0.5, 'mountain': 5, 'water': 10}

    def place_roads(self):
        """Place roads to connect all key points into a cohesive network."""
        logging.info("Starting road placement with structured approach.")
        
        # Retrieve all key points (player zones + a central zone)
        key_points = self._get_key_points()
        logging.info(f"Key points to connect: {key_points}")
        
        # Connect each pair of key points
        for i, start in enumerate(key_points):
            for end in key_points[i + 1:]:
                self._connect_points_with_astar(start, end)

        # Optionally smooth the road network
        self._smooth_road_network()

        logging.info("Road placement completed.")

    def _connect_points_with_astar(self, start, end):
        """Connect two points using A* pathfinding."""
        logging.info(f"Connecting {start} to {end} using A*.")
        open_set = []
        heapq.heappush(open_set, (0, start, None))  # (cost, (x, y), parent)
        came_from = {}
        g_score = {start: 0}

        while open_set:
            _, current, parent = heapq.heappop(open_set)
            x, y = current
            came_from[current] = parent

            if current == end:  # Reached the destination
                self._reconstruct_path(came_from, end)
                return

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if not self._is_valid_tile(nx, ny):
                    continue

                neighbor = (nx, ny)
                terrain = self.grid_map.grid[ny][nx].terrain
                cost = self.movement_costs.get(terrain, float('inf'))
                tentative_g_score = g_score[current] + cost

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score, neighbor, current))

    def _reconstruct_path(self, came_from, end):
        """Reconstruct and mark the road on the map."""
        current = end
        while current:
            x, y = current
            self.grid_map.grid[y][x].terrain = 'road'
            current = came_from[current]

    def _is_valid_tile(self, x, y):
        """Check if a tile is valid for road placement."""
        return 0 <= x < self.grid_map.width and 0 <= y < self.grid_map.height

    def _smooth_road_network(self):
        """Smooth road tiles by removing unnecessary deviations."""
        logging.info("Smoothing road network.")
        for y in range(self.grid_map.height):
            for x in range(self.grid_map.width):
                if self.grid_map.grid[y][x].terrain == 'road':
                    # Check neighboring tiles
                    neighbors = [
                        (x + dx, y + dy)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        if self._is_valid_tile(x + dx, y + dy)
                        and self.grid_map.grid[y + dy][x + dx].terrain == 'road'
                    ]
                    # Remove isolated road tiles
                    if len(neighbors) <= 1:
                        self.grid_map.grid[y][x].terrain = 'grass'

    def _get_key_points(self):
        """Retrieve all key points (player zones, central zones) for road placement."""
        player_zones = self._get_player_zone_centers()
        central_zone = self._get_random_central_point()
        return player_zones + [central_zone]

    def _get_player_zone_centers(self):
        """Retrieve the centers of player zones for road connections."""
        margin = 2
        zone_size = 3
        zones = [
            (margin + zone_size // 2, margin + zone_size // 2),  # Top-left
            (self.grid_map.width - margin - zone_size // 2, margin + zone_size // 2),  # Top-right
            (margin + zone_size // 2, self.grid_map.height - margin - zone_size // 2),  # Bottom-left
            (self.grid_map.width - margin - zone_size // 2, self.grid_map.height - margin - zone_size // 2),  # Bottom-right
        ]
        return zones

    def _get_random_central_point(self):
        """Generate a random central point for road generation."""
        return (
            random.randint(self.grid_map.width // 3, 2 * self.grid_map.width // 3),
            random.randint(self.grid_map.height // 3, 2 * self.grid_map.height // 3),
        )
