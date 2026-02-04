from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#Breadth First Search 2
def BFS2(G, node1, node2):
    Q = deque([node1])
    L = []
    marked = {node1 : node1}
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                marked[node2] = current_node
                L.append(node2)
                while marked[node] != node1:
                    node = marked[node]
                    L.append(node)
                L.append(node1)
                return list(reversed(L))
            if not node in marked:
                Q.append(node)
                marked[node] = current_node
    return []

#Breadth First Search 3
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : node1}
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not node in marked:
                Q.append(node)
                marked[node] = current_node
    return marked


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

# ========================================
# DFS implementations
# ========================================
def DFS2(G, node1, node2):
    return DFS2_aux(G, node1, node2, {}, [])
def DFS2_aux(G, node1, node2, m, p):
    print(m, p)
    m[node1] = True;
    p.append(node1);
    if node1 == node2:
        return p;
    for n in G.adj[node1]:
        if n in m and m[n]: continue
        r = DFS2_aux(G, n, node2, m, p)
        if r == []: continue
        else: return r;
    p.pop()
    return []

def DFS3(G, node1):
    return DFS3_aux(G, node1, {node1: None}, lambda n,m : 0)
def DFS3_aux(G, node1, m, inspect):
    inspect(node1, m);
    for n in G.adj[node1]:
        if n in m: continue
        m[n] = node1;
        DFS3_aux(G, n, m, inspect)
    return m;

# ========================================
# Graph properties
# ========================================
def has_cycle(G):
    cycle_found = False
    def check_cycle(node, connectivity):
        nonlocal cycle_found
        for n in G.adj[node]:
            if n in connectivity and connectivity[node] != n:
                cycle_found = True
    DFS3_aux(G, 0, {0: None}, check_cycle)
    return cycle_found

def is_connected(G):
    conn = DFS3(G, 1);
    return len(conn) == len(G.adj);

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


