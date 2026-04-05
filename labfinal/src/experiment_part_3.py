import os
import time
from itertools import permutations
from math import isclose

import matplotlib.pyplot as plt

from astar import a_star
from final_project_part1 import dijkstra
from load_graph import LondonSubway


os.chdir(os.path.dirname(os.path.dirname(__file__)))


def generate_all_source_target_pairs(nodes):
    return list(permutations(sorted(nodes), 2))


same_line_pairs = [
    (9, 60, "Arnos Grove (9) -> Covent Garden (60)"),
    (7, 56, "Angel (7) -> Clapham South (56)"),
    (16, 24, "Barkingside (16) -> Bethnal Green (24)"),
]

adjacent_line_pairs = [
    (22, 28, "Belsize Park (22) -> Bond Street (28)"),
    (26, 193, "Blackhorse Road (26) -> Paddington (193)"),
    (12, 107, "Balham (12) -> Green Park (107)"),
]

multi_transfer_line_pairs = [
    (2, 175, "Aldgate (2) -> New Cross Gate (175)"),
    (26, 225, "Blackhorse Road (26) -> Shadwell (225)"),
    (60, 253, "Covent Garden (60) -> Surrey Quays (253)"),
]


def plot_route_comparison(route_pairs, title, strength, runs):
    london = LondonSubway()
    graph = london.graph

    labels = []
    dijkstra_times = []
    astar_times = []


    for source, target, label in route_pairs:
        labels.append(label)
        dijkstra_time = 0
        for _ in range(runs):
            start = time.perf_counter()
            dijkstra_dist = dijkstra(graph, source)
            dijkstra_time += (time.perf_counter() - start) * 1000
        dijkstra_times.append(dijkstra_time/runs)

        astar_time = 0
        heuristic = london.getHeuristic(target, strength)
        for _ in range(runs):
            start = time.perf_counter()
            astar_dist = a_star(graph, source, target, heuristic)
            astar_time += (time.perf_counter() - start) * 1000
        astar_times.append(astar_time/runs)

        print(label)
        print("Dijkstra average running time (ms) = " + str(dijkstra_time/runs))
        print("A* average running time (ms) = " + str(astar_time/runs))

        if not isclose(dijkstra_dist[target], astar_dist[target], rel_tol=1e-9, abs_tol=1e-9):
            print("Warning: shortest-path mismatch for " + label)

    x_positions = list(range(len(labels)))
    width = 0.35

    plt.figure(figsize=(12, 6))
    plt.bar([x - width / 2 for x in x_positions], dijkstra_times, width=width, color="red", label="Dijkstra")
    plt.bar([x + width / 2 for x in x_positions], astar_times, width=width, color="blue", label="A*")
    plt.xticks(x_positions, labels, rotation=10, ha="right")
    plt.ylabel("Average Running Time (ms)")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Experiment 1:
def experiment_1(strength=1.0):
    london = LondonSubway()
    graph = london.graph
    nodes = sorted(graph.adj.keys())
    pairs = generate_all_source_target_pairs(nodes)

    dijkstra_cache = {}
    dijkstra_runtime_by_source = {}
    heuristic_cache = {target: london.getHeuristic(target, strength) for target in nodes}

    for source in nodes:
        start = time.perf_counter()
        dijkstra_cache[source] = dijkstra(graph, source)
        dijkstra_runtime_by_source[source] = (time.perf_counter() - start) * 1000

    dijkstra_times = []
    astar_times = []
    mismatches = []

    for source, target in pairs:
        dijkstra_dist = dijkstra_cache[source]
        dijkstra_times.append(dijkstra_runtime_by_source[source])

        start = time.perf_counter()
        astar_dist = a_star(graph, source, target, heuristic_cache[target])
        astar_times.append((time.perf_counter() - start) * 1000)

        if not isclose(dijkstra_dist[target], astar_dist[target], rel_tol=1e-9, abs_tol=1e-9):
            mismatches.append((source, target, dijkstra_dist[target], astar_dist[target]))

    avg_dijkstra_time = sum(dijkstra_times) / len(dijkstra_times)
    avg_astar_time = sum(astar_times) / len(astar_times)

    print("number of stations = " + str(len(nodes)))
    print("number of source-target pairs = " + str(len(pairs)))
    print("Average Dijkstra running time (ms) = " + str(avg_dijkstra_time))
    print("Average A* running time (ms) = " + str(avg_astar_time))
    print("Shortest-path mismatches = " + str(len(mismatches)))

    if mismatches:
        print("First 5 mismatches = " + str(mismatches[:5]))

    plt.figure(figsize=(8, 6))
    algorithms = ["Dijkstra", "A*"]
    average_times = [avg_dijkstra_time, avg_astar_time]
    plt.bar(algorithms, average_times, color=["red", "blue"])
    plt.ylabel("Average Running Time (ms)")
    plt.title("Experiment 1: Average Runtime on the London Map")
    plt.tight_layout()
    plt.show()


# Experiment 2:
def experiment_2(strength=1.0):
    plot_route_comparison(same_line_pairs, "Experiment 2: Runtime for Trips on the Same Line", strength, 1000)


# Experiment 3:
def experiment_3(strength=1.0):
    plot_route_comparison(adjacent_line_pairs, "Experiment 3: Runtime for Trips on Adjacent Lines", strength, 1000)


# Experiment 4:
def experiment_4(strength=1.0):
    plot_route_comparison(multi_transfer_line_pairs, "Experiment 4: Runtime for Trips Requiring Several Transfers", strength, 1000)


# Uncomment one experiment at a time to run it.
# experiment_1()
# experiment_2()
# experiment_3()
experiment_4()
