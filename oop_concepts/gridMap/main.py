from models.gridMap  import GridMap
from models.player import Player
from models.unit import Unit
from models.terrainGenerator import TerrainGenerator
from models.pathfinder import PathPlanner
from models.zoneGenerator import ZoneAllocator
from views.gridView import BoardView
import tkinter as tk

# Adjusted Terrain Configuration
TERRAIN_CONFIG = {
    'grass': {'threshold': None, 'scale': None},  # Default terrain
    'mountain': {'threshold': 0.5, 'scale': 12},
    'water': {'threshold': 0.35, 'scale': 8},
    'road': {'segments': 3, 'min_length': 7, 'max_length': 15},
}

def main():
    width, height = 15, 15
    grid_map = GridMap(width, height)

    # Terrain Generation
    terrain_generator = TerrainGenerator(grid_map, TERRAIN_CONFIG)
    terrain_generator.generate_terrain()

    # Road Placement
    path_planner = PathPlanner(grid_map, TERRAIN_CONFIG)
    path_planner.place_roads()

    # Reserve Player Zones
    zone_allocator = ZoneAllocator(grid_map)
    zone_allocator.reserve_player_zones()

    # Print Grid and Debug Information
    print("Generated Terrain Map:")
    grid_map.display_grid()

    # Visualize with Tkinter
    root = tk.Tk()
    root.title("Tactical Board")
    board_view = BoardView(root, grid_map)
    board_view.display_board()
    root.mainloop()

if __name__ == "__main__":
    main()
