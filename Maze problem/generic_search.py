from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
# from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self):
        return str(self._container)


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()  # FIFO

    def __repr__(self) -> str:
        return repr(self._container)


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        heappush(self._container, item)  # in by priority

    def pop(self) -> T:
        return heappop(self._container)  # out by priority

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        # print(self.cost + self.heuristic, other.cost + other.heuristic)
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __repr__(self):
        return repr(self.state) + ' heuristic: ' + repr(self.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    print(initial)
    # frontier is where we've yet to go
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored: Set[T] = {initial}

    # keep going while there is more to explore
    while not frontier.empty:
        print('\nfrontier..')
        print(frontier)

        current_node: Node[T] = frontier.pop()
        print('state')
        print(current_node.state)
        current_state: T = current_node.state
        # if we find the goal, we are done
        if goal_test(current_state):
            return current_node
        # check where we can go next and have not explored
        for child in successors(current_state):
            print('child')
            print(child)

            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
            print('explored')
            print(explored)
    return None  # went through everything and never found goal


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    print(initial)
    # frontier is where we've yet to go
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    # explored is where we have been
    explored: Set[T] = {initial}

    # keep going while is more to explore
    while not frontier.empty:
        print('\nfrontier..')
        print(frontier)

        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        print('state')
        print(current_node.state)
        # print(current_node.state)
        # if we found the goal, we've done
        if goal_test(current_state):
            return current_node
        # if we check where we can go next and haven't explored
        for child in successors(current_state):
            print('child')
            print(child)

            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
            print('explored')
            print(explored)
    return None  # went through everything and never found goal


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    print(initial)
    # frontier is where we have yet to go
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    # explored is where we have been
    explored: Dict[T, float] = {initial: 0.0}

    # keep going while is more to explore
    while not frontier.empty:
        print('\nA*\nfrontier..')
        print(frontier)

        # print(explored)
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        print('state')
        print(current_node.state)
        # print(current_node.state)
        # if we found the goal, we are done
        if goal_test(current_state):
            return current_node
        # check where we can go next and have not explored
        for child in successors(current_state):
            print('child')
            print(child)

            new_cost: float = current_node.cost + 1  # 1 assumes a grid, need a cost function for more sophisticated..

            if child not in explored or explored[child] > new_cost:

                # print(explored)
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
                print('explored')
                print(explored)

    return None  # went through everything and never found goal


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


