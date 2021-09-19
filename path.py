from enum import Enum
import random
from typing import List, NamedTuple, Callable, Optional
from math import sqrt

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class Location(NamedTuple):
    row: int
    column: int


class map:
    def __init__(self, rows: int = 20, columns: int = 10, sparseness: float = 0.2, start: Location = Location(0, 0), goal: Location = Location(19, 19)) -> None:
        # Initialize a random map for the algorithm to solve
        self._rows: int = rows
        self._columns: int = columns
        self.start: Location = start
        self.goal: Location = goal
        #Initialize a 2D array of type cell enumerator
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]

        #add in random blocked cells
        self._randomly_fill(rows, columns, sparseness)
        #set start and goal cells
        self._grid[start.row][start.column] = Cell.Start
        self._grid[goal.row][goal.column] = Cell.Goal


    def randomly_fill(self, rows: int, columns, int, sparseness: float):
        for row in range(rows):

