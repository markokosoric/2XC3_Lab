from abc import ABC, abstractmethod
from typing import override

from final_project_part1 import DirectedWeightedGraph

class Graph(ABC):
    @abstractmethod
    def get_adj_nodes(self, node: int) -> list[int]:
        pass
    @abstractmethod
    def add_node(self, node: int):
        pass
    @abstractmethod
    def add_edge(self, start: int, end: int, w: float):
        pass
    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass
    @abstractmethod
    def w(self, node1: int, node2: int) -> float:
        pass
    @abstractmethod
    def get_nodes(self) -> list[int]: # not part of UML diagram but required for algo
        pass

class WeightedGraph(Graph):
    graph: DirectedWeightedGraph
    def __init__(self) -> None:
        super().__init__()
        self.graph = DirectedWeightedGraph()

    @override
    def get_adj_nodes(self, node: int) -> list[int]:
        return self.graph.adjacent_nodes(node)
    @override
    def add_node(self, node: int):
        self.graph.add_node(node)
    @override
    def add_edge(self, start: int, end: int, w: float):
        self.graph.add_edge(start, end, w);
    @override
    def get_num_of_nodes(self) -> int:
        return self.graph.number_of_nodes()
    @override
    def w(self, node1: int, node2: int) -> float:
        return self.graph.w(node1, node2)
    @override
    def get_nodes(self) -> list[int]:
        return list(self.graph.adj.keys());

class HeuristicGraph(WeightedGraph):
    _heuristic: dict[int, float]

    def __init__(self, h: dict[int, float]) -> None:
        super().__init__()
        self._heuristic = h;


    def get_heuristic(self) -> dict[int, float]:
        return self._heuristic
