from heapq import heappush, heappop
from path import Location, Cell, map
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
import sys

class Node(object):
    def __init__(self, loc: Location, cost: float, heuristic: float, parent=None):
        self.location: Location = loc
        self.cost: float = cost
        self.heuristic: float = heuristic
        self.parent: Node = parent

    def __lt__(self, other) -> bool:

        return (self.cost + self.heuristic) < (other.cost + other.heuristic)



class PriorityQueue():
    def __init__(self) -> None:
        self._container = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: Node) -> None:
        heappush(self._container, item)

    def pop(self) -> Node:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)



def astar(start: Location, grid: map) -> Node:
    frontier: PriorityQueue = PriorityQueue()
    frontier.push(Node(start, 0.0, grid.manhattan(start)))

    explored: Dict[Location, float] = {start: 0.0}
    
    while not frontier.empty:
        current_node = frontier.pop()
        current_loc = current_node.location
        
        if grid.goal_test(current_loc):
            return current_node
        for child in grid.successors(current_loc):
            new_cost: float = current_node.cost + 1
            
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, new_cost, grid.manhattan(child), current_node))
                grid.expanded = grid.expanded + 1
    return None


def constructPath(grid: map, node: Node) -> None:
    while node.parent:
        if grid._grid[node.location.row][node.location.column] == ' ':

            grid._grid[node.location.row][node.location.column] = Cell.PATH
        node = node.parent



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Please pass row and column number")
        exit()
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    
    randomMap: map = map(rows, columns, 0.1, Location(0, 0), Location(rows - 2, columns - 2))
    solutionNode: Node = astar(randomMap.start, randomMap)
    constructPath(randomMap, solutionNode)
    if sys.argv[3] == "print":
        print(randomMap)
    print("Nodes expanded: " + str(randomMap.expanded))
