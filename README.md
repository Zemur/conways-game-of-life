# Conway's Game of Life
Conway's Game of Life in Pygame.

Thanks to [agusrichard](https://github.com/agusrichard) for the jumping off point with his extremely informative [Nerd For Tech Article](https://medium.com/nerd-for-tech/lets-play-game-of-life-with-python-ec3e5ae00e6).

Agus' full code can be found [here](https://github.com/agusrichard/python-workbook/tree/master/game-of-life).

## How To Run
The easiest way to run the code is to simply install the requirements with `pip install -r requirements.txt` and running `python main.py`

## Changes made from the original

### Updated draw_grid()
`draw_grid()` was updated to only call `pygame.draw.rect()` a single time by setting the rect dimensions and using the condition to set the color to active or inactive ahead of time.

### Updated update_cells()
I added a new method to determine the number of alive neighbors:
```python
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
```
This will add all eight neighbors (or less when applicable) state to a list and return the number of `True` states.

### Added colors module
There were multiple times the same color was used throughout the code, so I placed them in a module in order to have a single source of truth across the project.
