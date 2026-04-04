from final_project_part1 import *
import matplotlib.pyplot as plt
import time


# Experiment 1:
# Vary the relaxation limit k for dijkstra_approx and compare its average
# total distance from the source against the exact Dijkstra algorithm.
def experiment_1(runs=1000, n=30, upper=100, source=0, ks=None):
    if ks is None:
        ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    data_exact = []
    data_approx = []

    for k in ks:
        total_exact = 0
        total_approx = 0

        for _ in range(runs):
            G = create_random_complete_graph(n, upper)
            total_exact += total_dist(dijkstra(G, source))
            total_approx += total_dist(dijkstra_approx(G, source, k))

        data_exact.append(total_exact / runs)
        data_approx.append(total_approx / runs)

    print("k values = " + str(ks))
    print("Exact Dijkstra average total distance = " + str(data_exact))
    print("Dijkstra Approx average total distance = " + str(data_approx))

    plt.figure()
    plt.plot(ks, data_exact, color='blue')
    plt.plot(ks, data_approx, color='red')
    plt.xlabel('Relaxation Limit k')
    plt.ylabel('Average Total Distance from Source')
    plt.legend(['Exact Dijkstra', 'Dijkstra Approx'])
    plt.title('Experiment 1: Dijkstra Approximation Quality')
    plt.tight_layout()
    plt.show()


# Experiment 2:
# Vary the relaxation limit k for bellman_ford_approx and compare its average
# total distance from the source against the exact Bellman-Ford algorithm.
def experiment_2(runs=1000, n=30, upper=100, source=0, ks=None):
    if ks is None:
        ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    data_exact = []
    data_approx = []

    for k in ks:
        total_exact = 0
        total_approx = 0

        for _ in range(runs):
            G = create_random_complete_graph(n, upper)
            total_exact += total_dist(bellman_ford(G, source))
            total_approx += total_dist(bellman_ford_approx(G, source, k))

        data_exact.append(total_exact / runs)
        data_approx.append(total_approx / runs)

    print("k values = " + str(ks))
    print("Exact Bellman-Ford average total distance = " + str(data_exact))
    print("Bellman-Ford Approx average total distance = " + str(data_approx))

    plt.figure()
    plt.plot(ks, data_exact, color='blue')
    plt.plot(ks, data_approx, color='green')
    plt.xlabel('Relaxation Limit k')
    plt.ylabel('Average Total Distance from Source')
    plt.legend(['Exact Bellman-Ford', 'Bellman-Ford Approx'])
    plt.title('Experiment 2: Bellman-Ford Approximation Quality')
    plt.tight_layout()
    plt.show()


# Experiment 3:
# Vary the number of nodes n and compare the average running time of the exact
# Dijkstra and Bellman-Ford algorithms on random complete graphs.
def experiment_3(runs=200, upper=100, source=0, sizes=None):
    if sizes is None:
        sizes = [5, 10, 15, 20, 25, 30, 35, 40]

    data_dijkstra = []
    data_bellman_ford = []

    for n in sizes:
        total_dijkstra_time = 0
        total_bellman_ford_time = 0

        for _ in range(runs):
            G = create_random_complete_graph(n, upper)

            start = time.perf_counter()
            dijkstra(G, source)
            total_dijkstra_time += time.perf_counter() - start

            start = time.perf_counter()
            bellman_ford(G, source)
            total_bellman_ford_time += time.perf_counter() - start

        data_dijkstra.append((total_dijkstra_time / runs) * 1000)
        data_bellman_ford.append((total_bellman_ford_time / runs) * 1000)

    print("sizes = " + str(sizes))
    print("Dijkstra times (ms) = " + str(data_dijkstra))
    print("Bellman-Ford times (ms) = " + str(data_bellman_ford))

    plt.figure()
    plt.plot(sizes, data_dijkstra, color='red')
    plt.plot(sizes, data_bellman_ford, color='green')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Average Running Time (ms)')
    plt.legend(['Dijkstra', 'Bellman-Ford'])
    plt.title('Experiment 3: Dijkstra vs Bellman-Ford Runtime')
    plt.tight_layout()
    plt.show()


# Experiment 4:
# Vary the relaxation limit k and compare the average running time of
# dijkstra_approx and bellman_ford_approx on random complete graphs.
def experiment_4(runs=2500, n=30, upper=100, source=0, ks=None):
    if ks is None:
        ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    data_dijkstra_approx = []
    data_bellman_ford_approx = []

    for k in ks:
        total_dijkstra_time = 0
        total_bellman_ford_time = 0

        for _ in range(runs):
            G = create_random_complete_graph(n, upper)

            start = time.perf_counter()
            dijkstra_approx(G, source, k)
            total_dijkstra_time += time.perf_counter() - start

            start = time.perf_counter()
            bellman_ford_approx(G, source, k)
            total_bellman_ford_time += time.perf_counter() - start

        data_dijkstra_approx.append((total_dijkstra_time / runs) * 1000)
        data_bellman_ford_approx.append((total_bellman_ford_time / runs) * 1000)

    print("k values = " + str(ks))
    print("Dijkstra Approx times (ms) = " + str(data_dijkstra_approx))
    print("Bellman-Ford Approx times (ms) = " + str(data_bellman_ford_approx))

    plt.figure()
    plt.plot(ks, data_dijkstra_approx, color='red')
    plt.plot(ks, data_bellman_ford_approx, color='green')
    plt.xlabel('Relaxation Limit k')
    plt.ylabel('Average Running Time (ms)')
    plt.legend(['Dijkstra Approx', 'Bellman-Ford Approx'])
    plt.title('Experiment 4: Approximation Runtime Comparison')
    plt.tight_layout()
    plt.show()


# Experiment 5:
# Vary the number of nodes n and measure the average running time of the
# mystery algorithm on random complete graphs.
def experiment_5(runs=200, upper=100, sizes=None):
    if sizes is None:
        sizes = [5, 10, 15, 20, 25, 30, 35, 40]

    data_mystery = []

    for n in sizes:
        total_mystery_time = 0

        for _ in range(runs):
            G = create_random_complete_graph(n, upper)

            start = time.perf_counter()
            mystery(G)
            total_mystery_time += time.perf_counter() - start

        data_mystery.append((total_mystery_time / runs) * 1000)

    print("sizes = " + str(sizes))
    print("Mystery times (ms) = " + str(data_mystery))

    plt.figure()
    plt.plot(sizes, data_mystery, color='purple')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Average Running Time (ms)')
    plt.legend(['Mystery'])
    plt.title('Experiment 5: Mystery Algorithm Runtime')
    plt.tight_layout()
    plt.show()


# Uncomment one experiment at a time to run it.
experiment_1()
# experiment_2()
# experiment_3()
# experiment_4()
# experiment_5()
