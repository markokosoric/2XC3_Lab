#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)



#align(center)[
  #text(size: 2em, weight: "bold")[Final Lab Report]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab Final]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick Chen]

  #v(1em)

  #text(size: 1em)[April 4, 2026]
]

#pagebreak()

#outline()

#outline(title: "Figures", target: figure.where(kind: image))
#outline(title: "Tables", target: figure.where(kind: table))

#pagebreak()

= Executive Summary

#pagebreak()

= Part 1

== Experiment 1

This experiment investigates how limiting the number of relaxations in
Dijkstra's algorithm affects the quality of numbers for the shortest path
distances. Random complete graphs with 30 nodes and edge weights uniformly
distributed between 0 and 100 were generated. The source node was fixed to 0.
For each value of k (max number of relaxations) from 1 to 10, 1000 trials were
run where the distance from
the source node was computed using the Dijkstra and the Dijkstra approximation
algorithms. The average total distances were then plotted as a function of k.

#figure(
  image("results/part_1/experiment_1_graph.png"),
  caption: [
    Plot of Average Total Distance from Source Node for Dijkstra's Algorithm
  ],
)

The results indicate that for small values of k, the Dijkstra approximation
algorithm produces significantly larger total distances. This is because the
small values for k lead to insufficient relaxations meaning many shortest paths
are not discovered. As k increases, the Dijkstra approximation algorithm
results converge down to the value of the regular Dijkstra algorithm. This
demonstrates a trade-off in computational efficiency and accuracy because
smaller values of k provide faster but less accurate results, while larger
values provide slower but more accurate results.

== Experiment 2

This experiment investigates how limiting the number of relaxations in
Bellman Ford's algorithm affects the quality of numbers of the shortest path
distances. Random complete graphs with 30 nodes and edge weights uniformly
distributed between 0 and 100 were generated. The source node was fixed to 0.
For each value of k (max number of relaxations) from 1 to 10, 1000 trials were
run where the distance from the source node was computed using the Bellman Ford
and the Bellman Ford approximation algorithms. The average total distances were
then plotted as a function of k.

#figure(
  image("results/part_1/experiment_2_graph.png"),
  caption: [
    Plot of Average Total Distance from Source Node for
    Bellman Ford's Algorithm
  ],
)

The results show the same thing as the first experiment. Smaller values of k
provide faster but less accurate results and more accurate results as you
increase k. The results for Bellman-Ford's approximation algorithm converge
later than the same one for Dijkstra's. This is expected because Bellman-Ford's
relaxations are roughly proportional to E while Bellman-Ford's is
roughly proportional to $V dot E$.

== Experiment 3

This experiment investigates how the average running time of Dijkstra's and
Bellman Ford's algorithms scale with the size of the graphs. Random complete
graphs were generated with the number of nodes varying from 5 to 40 and edge
weights were uniformly distributed between 0 and 100. The source node was fixed
at 0. For each graph size, 200 trials were run and the run time for both
algorithms were measured. The average running times were plotted as a function
of the number of nodes.

#figure(
  image("results/part_1/experiment_3_graph.png"),
  caption: [
    Average Running Time of Dijkstra and Bellman-Ford vs Number of Nodes
  ],
)

The results demonstrate the average run times of both algorithms as the graph
size increases. Dijkstra's algorithm performs significantly better on graphs
with more nodes. However, the performance is quite similar on graphs with
minimal sizes. This difference is expected due to their theoretical time
complexities of $O(V dot E)$ for Bellman-Ford's algorithm and $O(E log V)$ for
Dijkstra's algorithm. Also, Dijkstra's algorithm uses a priority queue to
process nodes, while Bellman-Ford repeatedly scans all edges.
This highlights the importance of algorithm choice based
on graph size.

== Experiment 4

This experiment investigates how the relaxation limit affects the running time
of Dijkstra and Bellman-Ford algorithms. Random complete graphs with 30 nodes
were generated with edge weights uniformly distributed between 0 and 100. The
source node was fixed at 0. For each value of k (max number of relaxations)
ranging from 1 to 10, 2500 trials were run where the run time was measured for
each algorithm. The average run time was plotted as a function of k.

#figure(
  image("results/part_1/experiment_4_graph.png"),
  caption: [
    Average Running Time of Dijkstra Approx and Bellman-Ford Approx vs
    Relaxation Limit
  ],
)

The results demonstrate that both run times increase as k increases since more
relaxations are performed. However, Dijkstra's algorithm performs significantly
better. This is expected as it's theoretical average runtime is better than
Bellman-Ford's. In addition, Dijkstra's algorithm is much more stable as k
increases. This is expected because it requires fewer relaxations than
Bellman-Ford's. This experiment highlights how relaxations can affect runtimes.

== Mystery Algorithm

If correctness is the only concern, then all-pairs shortest path algorithm's for
graphs with non-negative edge weights can be computed by running Dijkstra's
algorithm once from every vertex. Since Dijkstra's algorithm is $Theta (V^2)$
for dense graphs, repeating it for all V vertices would give a total complexity
of
$Theta (V^3)$. For graphs that may contain negative edge weights the same thing
can be done but with Bellman-Ford's algorithm. Since Bellman-Ford's algorithm is
$Theta (V^3)$ for dense graph, repeating it for all V vertices would give a
total time complexity of $Theta (V^4)$.

#figure(
  image("results/part_1/experiment_5_graph.png"),
  caption: [
    Average Running Time of Mystery Algorithm vs Number of Nodes
  ],
)

The time complexity of the mystery function is $Theta (V^3)$ because it has
three nested loops, each running n times. The initialization is only
$Theta (V^3)$, so it is dominated by the nested loops.

#figure(
  image("results/part_1/experiment_6_graph.png"),
  caption: [
    Total Shortest Path Distances on Graphs with Negative Edge Weights using
    Mystery Algorithm
  ],
)

The mystery function is Floyd-Marshall's algorithm, which computes the shortest
path distance between every pair of vertices in graph. This algorithm sticks out
because it uses a matrix to represent the distances between nodes, and it uses a
triple nested loop. Also, Floyd-Marshall's algorithm does not work with negative
cycles. The graph in figure six tells us the algorithm is
Floyd-Marshall's because it clearly does not give the correct total distance for
graphs with negative cycles. The time complexity of this algorithm is $O (V^3)$.
This is not surprising given the graph from Figure 5. It is important to note
that this algorithm performs better than Bellman-Ford's all-pairs shortest path
solution but Floyd-Marshall's does not work with negative cycles.
Also, note that while Dijkstra's solution has the same time complexity
as Floyd-Marshall's, Dijkstra's solution does not work with negative edge
weights and Floyd-Marshall's does.

= Part 2

A\* is a shortest path algorithm that extends Dijkstra's algorithm by using a
heuristic function to guide the search towards the shortest path. The A\*
algorithm chooses the node with minimum cost:

$ f(n) = g(n) + h(n) $

where n is the next node on the path, g(n) is the cost of the cheapest path from
the source node to n and h(n) is an estimate from the heuristic function of the
path from n to the target node.

The issue with Dijkstra's algorithm is that it only explores nodes based on
the current distance from the source node. This can be inefficient because the
algorithm will explore unessecarly costly paths. The A\* algorithm addresses
this issue by incorporating a heuristic function that estimates the remaining
distance to the target node. By prioritizing nodes with a minimal
$f(n) = g(n) + h(n)$, it directs the search towards the target node and reduces
the amount of unessecary exploration.

To empirically compare Dijkstra's and A\*'s algorithm's, both algorithms should
be run on the same set of graphs with the same source and target nodes. Relevant
things to measure include, running time, number of nodes explored, the
number of relaxations done, and performance of different heuristics. Multiple
runs should be done for each independent variable to get consistent and reliable
averages.

If the heuristic was randomly generated, it would not provide useful guidance
towards the target node. In this case, A\* algorithm would perform similar or
worse to Dijkstra's algorithm as it's choice in the next node to explore will
be almost random. A bad heuristic function means the algorithm will explore more
unessecary nodes and do more relaxations thus reducing performance.

A\* algorithm is preferred when a fraction of the nodes need to be examined and
a good heuristic is provided. A common example is in GPS navigation systems
where only a single shortest path from a start position to an end position needs
to be calculated. In this example, heuristics such as Euclidean distance
provides a good estimate of the remaining cost (distance). This allows A\* to
reduce run time by exploring less unessecary nodes.

= Part 3
== Implementation
The London subway stations loaded into a weighted directed graph through the
use of a function that parses the stations and connections CSV. For each
connection, an edge was inserted into the graph for both directions of travel.

Since the size of London is relatively small compared to the earth, distances
can be approximated by assuming that the surrounding area is flat without needed
to take into account the curvature of the earth. Distances were calculated with
respect to the metric tensor $g$ at London's center ($theta, phi = 51.5 degree,
0.1 degree$). The heuristic $h$ was then calculated as the approximated distance
  between the two stations.
$
  g = mat(
    R^2, 0;
    0, R^2 sin^2(theta)
  ), wide h(bold(u), bold(v)) = sqrt(bold(u)^T g bold(v))
$

== Experiments
TODO

