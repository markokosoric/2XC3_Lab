from . import min_heap
import random

class DirectedWeightedGraph:
    weights: dict[tuple[int, int], float]
    adj: dict[int, list[int]]

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1: int, node2: int) -> bool:
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node: int) -> list[int]:
        return self.adj[node]

    def add_node(self, node: int):
        self.adj[node] = []

    def add_edge(self, node1: int, node2: int, weight: float):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1: int, node2: int) -> float:
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]
        raise Exception("unknown weight")

    def number_of_nodes(self) -> int:
        return len(self.adj)


def dijkstra(G: DirectedWeightedGraph, source: int) -> dict[int, float]:
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist: dict[int, float] = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G: DirectedWeightedGraph, source: int) -> dict[int, float]:
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist: dict[int, float] = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def total_dist(dist: dict[int, float]) -> float:
    total: float = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n:int, upper: int) -> DirectedWeightedGraph:
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G: DirectedWeightedGraph) -> list[list[float]]:
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G: DirectedWeightedGraph) -> list[list[float]]:
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d


def dijkstra_approx(G, source, k):
    pred = {}
    dist = {}
    relax_count = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        relax_count[node] = 0

    dist[source] = 0
    Q.decrease_key(source, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        for neighbour in G.adj[current_node]:
            new_dist = dist[current_node] + G.w(current_node, neighbour)
            if relax_count[neighbour] < k and new_dist < dist[neighbour]:
                Q.decrease_key(neighbour, new_dist)
                dist[neighbour] = new_dist
                pred[neighbour] = current_node
                relax_count[neighbour] += 1

    return dist


def bellman_ford_approx(G, source, k):
    pred = {}
    dist = {}
    relax_count = {}
    nodes = list(G.adj.keys())

    for node in nodes:
        dist[node] = float("inf")
        relax_count[node] = 0
    dist[source] = 0

    for _ in range(G.number_of_nodes()):
        updated = False
        for node in nodes:
            for neighbour in G.adj[node]:
                new_dist = dist[node] + G.w(node, neighbour)
                if relax_count[neighbour] < k and new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    pred[neighbour] = node
                    relax_count[neighbour] += 1
                    updated = True
        if not updated:
            break

    return dist
