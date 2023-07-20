# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

from collections import deque
from random import choice, randint


class Cell:
    __slots__ = ("row", "col", "visited", "walls")

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}


class Maze:
    __slots__ = ("rows", "cols", "grid", "stack", "directions", "opposite")

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.stack = deque()
        self.directions = (("top", -1, 0), ("right", 0, 1), ("bottom", 1, 0), ("left", 0, -1))
        self.opposite = {"top": "bottom", "right": "left", "bottom": "top", "left": "right"}

    def run(self, current):
        self.stack.append(current)
        while self.stack:
            current.visited = True
            neighbors = self.get_unvisited_neighbors(current)
            if neighbors:
                direction, next_cell = choice(neighbors)
                self.remove_wall(current, direction, next_cell)
                current = next_cell
                self.stack.append(current)
            else:
                current = self.stack.pop()

    def get_unvisited_neighbors(self, cell):
        neighbors = []
        for direction, row_offset, col_offset in self.directions:
            new_row, new_col = cell.row + row_offset, cell.col + col_offset
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                neighbor = self.grid[new_row][new_col]
                if not neighbor.visited:
                    neighbors.append((direction, neighbor))
        return neighbors

    def remove_wall(self, current, direction, next_cell):
        current.walls[direction] = False
        next_cell.walls[self.opposite[direction]] = False
        self.stack.append(next_cell)
        next_cell.visited = True


def main():
    for _ in range(30):
        size = randint(15, 40)
        rows, cols = size, size
        maze = Maze(rows, cols)
        maze.run(maze.grid[0][0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
