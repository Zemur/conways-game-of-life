import colors
import pygame
import numpy as np


class GameOfLife:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=1,
                 active_color=colors.WHITE, inactive_color=colors.GREY):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.columns = self.height // self.scale
        self.rows = self.width // self.scale
        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def __num_alive_neighbors(self, x, y):
        """Return how many neighbors are alive."""
        neighbors = [(x - 1, y),      # left
                     (x + 1, y),      # right
                     (x, y - 1),      # up
                     (x, y + 1),      # down
                     (x - 1, y - 1),  # left, up
                     (x - 1, y + 1),  # left, down
                     (x + 1, y - 1),  # right, up
                     (x + 1, y + 1)]  # right, down
        return [self.grid[i, j] for (i, j) in neighbors
                if 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0])].count(True)

    def run(self):
        """Update and redraw the current grid state."""
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        """Draw the grid"""
        for row in range(self.rows):
            for col in range(self.columns):
                rect = [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset]
                if self.grid[row, col]:
                    color = self.active_color
                else:
                    color = self.inactive_color
                pygame.draw.rect(self.surface, color, rect)

    def update_grid(self):
        """Updating the grid based on Conway's game of life rules."""
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid

    def update_cell(self, x, y):
        """Update single cell based on Conway's game of life rules."""
        current_state = self.grid[x, y]
        alive_neighbors = self.__num_alive_neighbors(x, y)

        # Update the cell's state
        if current_state and alive_neighbors < 2:
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):
            return True
        elif current_state and alive_neighbors > 3:
            return False
        elif not current_state and alive_neighbors == 3:
            return True
        else:
            return current_state