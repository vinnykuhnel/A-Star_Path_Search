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
    def __init__(self, rows: int = 20, columns: int = 20, sparseness: float = 0.2, start: Location = Location(0, 0), goal: Location = Location(19, 19)) -> None:
        # Initialize a random map for the algorithm to solve
        self._rows: int = rows
        self._columns: int = columns
        self.start: Location = start
        self.goal: Location = goal
        #Initialize a 2D array of type cell enumerator
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        #keep track of nodes expanded
        self.expanded: int = 0


        #add in random blocked cells
        self._randomly_fill(rows, columns, sparseness)
        #set start and goal cells
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL


    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    #Return a printable view of the maze
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([cell.value for cell in row]) + "\n"
        return output

    def goal_test(self, loc: Location) -> bool:
        return loc == self.goal

    #Check which moves can be taken given current location
    def successors(self, loc: Location) -> List[Location]:
        locations: List[Location] = []
        #check move right
        if loc.row + 1 < self._rows and self._grid[loc.row + 1][loc.column] != Cell.BLOCKED:
            locations.append(Location(loc.row + 1, loc.column))

        #check move left
        if loc.row - 1 >= 0 and self._grid[loc.row - 1][loc.column] != Cell.BLOCKED:
            locations.append(Location(loc.row - 1, loc.column))
        #check move up
        if loc.column + 1 < self._columns and self._grid[loc.row][loc.column + 1] != Cell.BLOCKED:
            locations.append(Location(loc.row, loc.column + 1))
        #check move down
        if loc.column -1 >= 0 and self._grid[loc.row][loc.column - 1] != Cell.BLOCKED:
            locations.append(Location(loc.row, loc.column - 1))

        return locations

    def manhattan(self, current: Location) -> float:
         xdist: int = abs(current.column - self.goal.column)
         ydist: int = abs(current.row - self.goal.row)
         return (xdist + ydist)

