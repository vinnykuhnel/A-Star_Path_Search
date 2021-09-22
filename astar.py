from heapq import heappush, heappop
from path import Location, Cell, map
import typing


class Node():
    def __init__(self, loc: Location, cost: float, heuristic: float, parent=None):
        self.location: Location = loc
        self.cost: float = cost
        self.heuristic: float = heuristic
        self.parent: Node = parent


class PriorityQueue():
    def __init__(self) -> None:
        self._container: List[Node] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: Node) -> None:
        heappush(self._container, item)

    def pop(self) -> Node:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)
class astar(start: Location, grid: map) -> Optional[Node]:
    frontier: PriorityQueue[Node] = PriorityQueue()
    frontier.push(Node(start, 0.0, map.manhattan_distance(start)))

    explored: Dict[Node, float] = {initial: 0.0}
    
    while not frontier.empty:
        current_node: Node = frontier.pop()
        current_loc: Location.loc
        
        if map.goal_test(current_loc):
            return current_node
        for child in map.successors(current_loc):
            new_cost: float = current_node.cost + 1
            
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, map.manhattan_heuristic(child)))
    return None


