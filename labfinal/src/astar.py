from . import min_heap
from labfinal.src.final_project_part1 import DirectedWeightedGraph


# From: https://en.wikipedia.org/wiki/A%2A_search_algorithm#Pseudocode
def a_star(G: DirectedWeightedGraph, s: int, d: int, h: dict[int, float]):
    pred: dict[int, int] = {}
    dist: dict[int,float] = {} #Distance dictionary

    Q = min_heap.MinHeap([])

    nodes = list(G.adj.keys())

    for node in nodes:
        dist[node] = float("inf")
        Q.insert(min_heap.Element(node, float("inf")))
    dist[s] = 0;
    Q.decrease_key(s, h[s])

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if current_node == d: return pred

        for neighbour in G.adj[current_node]:
            score = dist[current_node] + G.w(current_node, neighbour);
            if score < dist[neighbour]:
                pred[neighbour] = current_node
                dist[neighbour] = score;
                Q.decrease_key(neighbour, score + h[neighbour]);

    return pred

