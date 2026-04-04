from abc import ABC, abstractmethod
from typing import override

from labfinal.src.astar import a_star
from final_project_part1 import DirectedWeightedGraph, bellman_ford, dijkstra
from graph import *

class SPAlgorithm(ABC):
    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass

class Dijkstra(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in range(graph.get_num_of_nodes()):
            g.add_node(i);
        for i in range(graph.get_num_of_nodes()):
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        dist = dijkstra(g, source);
        return dist[dest];


class Bellman_Ford(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in range(graph.get_num_of_nodes()):
            g.add_node(i);
        for i in range(graph.get_num_of_nodes()):
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        dist = bellman_ford(g, source)
        return dist[dest];

class A_Star(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in range(graph.get_num_of_nodes()):
            g.add_node(i);
        for i in range(graph.get_num_of_nodes()):
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        if graph.get_heuristic == None: raise Exception("Graph does not have heuristic")  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        h: dict[int, float] = graph.get_heuristic();  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

        dist = a_star(g, source, dest, h);
        return dist[dest];

