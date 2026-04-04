from abc import ABC, abstractmethod
from typing import override

from astar import a_star
from final_project_part1 import DirectedWeightedGraph, bellman_ford, dijkstra
from graph import *

class ShortestPathFinder:
    _graph: Graph
    _algo: SPAlgorithm
    def __init__(self, graph: Graph, algorithm: SPAlgorithm) -> None:
        self._graph = graph;
        self._algo = algorithm;

    def calc_short_path(self, source: int, dest: int) -> float:
        return self._algo.calc_sp(self._graph, source, dest)

    def set_graph(self, graph: Graph):
        self._graph = graph
    def set_algorithm(self, algorithm: SPAlgorithm):
        self._algo = algorithm;


class SPAlgorithm(ABC):
    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass

class Dijkstra(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in graph.get_nodes():
            g.add_node(i);
        for i in graph.get_nodes():
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        dist = dijkstra(g, source);
        return dist[dest];


class Bellman_Ford(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in graph.get_nodes():
            g.add_node(i);
        for i in graph.get_nodes():
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        dist = bellman_ford(g, source)
        return dist[dest];

class A_Star(SPAlgorithm):
    @override
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        g = DirectedWeightedGraph();
        for i in graph.get_nodes():
            g.add_node(i);
        for i in graph.get_nodes():
            for n in graph.get_adj_nodes(i):
                g.add_edge(i, n, graph.w(i, n));
        if graph.get_heuristic == None: raise Exception("Graph does not have heuristic")  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        h: dict[int, float] = graph.get_heuristic();  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

        dist = a_star(g, source, dest, h);
        return dist[dest];

