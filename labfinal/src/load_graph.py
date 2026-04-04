from math import sin,pi,sqrt

from .final_project_part1 import DirectedWeightedGraph

# metric tensor at the center of london
def g(a: tuple[float,float], b: tuple[float,float]) -> float:
    return a[0]*b[0] + a[1]*b[1]*sin(51.5072 * (pi/180))


class LondonSubway:
    stations: dict[int, tuple[float, float]]
    graph: DirectedWeightedGraph

    def __init__(self) -> None:
        fd_stations = open("data/london_stations.csv")
        fd_connect  = open("data/london_connections.csv")
        _ = fd_stations.readline();
        _ = fd_connect.readline();

        g: DirectedWeightedGraph = DirectedWeightedGraph()
        stations: dict[int, tuple[float, float]] = {};

        for l in fd_stations.readlines():
            f = l.split(',')
            stations[int(f[0])] = (float(f[1]), float(f[2]));
            g.add_node(int(f[0]))

        for c in fd_connect.readlines():
            f = c.split(',')
            g.add_edge(int(f[0]), int(f[1]), float(f[3]))
            g.add_edge(int(f[1]), int(f[0]), float(f[3]))


        fd_stations.close();
        fd_connect.close();
        self.graph = g;
        self.stations = stations;

    def getHeuristic(self, node: int) -> dict[int, float]:
        h: dict[int, float] = {};
        dest = self.stations[node]
        for n in self.stations.keys():
            delta = (self.stations[n][0] - dest[0], self.stations[n][1] - dest[1])
            h[n] = sqrt(g(delta, delta))

        return h;

print(LondonSubway().getHeuristic(1))
