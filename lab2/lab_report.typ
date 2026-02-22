#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)

#align(center)[
  #text(size: 2em, weight: "bold")[Lab Report: Graph algorithms]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab 2]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick Chen]

  #v(1em)

  #text(size: 1em)[February 22, 2026]
]

#pagebreak()

#outline()

#outline(title: "Figures", target: figure.where(kind: image))

#pagebreak()

#show figure.where(
  kind: image,
): set figure.caption(position: top)

= Executive Summary
// TODO

= Part 1
== Experiment 1
A graph with $n = 100$ nodes and $e in [0, 200)$ was generated 100 times. The
probability of a cycle existing was recorded. This procedure was repeated for
all integer values of $e$ within the experiment parameters.
#figure(
  image("experiment1_graph.png"),
  caption: [
    Probability of a cycle existing vs edge count
  ],
)
The data shows that the probability of finding a cycle follows a sigmoid curve
when plotted against edge count. The probability starts to rise as the number
of edges reaches around 50 and reaches probability 1 at around 150.

== Experiment 2
A graph with $n = 100$ nodes and $e in [100, 500]$ was generated 100 times. The
probability that the graph is connected was recorded. This procedure was
repeated for all integer values of $e$ within the experiment parameters.
#figure(
  image("experiment2_graph.png"),
  caption: [
    Probability of a graph being connected vs edge count
  ],
)
The data shows that the probability of the graph being connected is almost zero
when the edges is below 150. Once the amount of edges reaches around 350, it
becomes almost certain that the graph will be connected. This graph also follows
a sigmoid curve like the graph in experiment 1.

= Part 2
== Experiment Vertex Cover Approximations

=== Experiment 1

For each edge count in $[1, 5, 10, 15, 20, 25, 28]$ on graphs with $n = 8$ nodes, I generated 1000 random graphs. For each graph I computed the total MVC and the total of each of the three approximations, then averaged the ratio $|A_i|/|"MVC"|$ per edge count.



#figure(
  image("experiment_approximations_1_graph.png"),
  caption: [
    Plot of Expected Approximation Performance for 8 Nodes
  ],
)

In this experiment, as the number of edges increases, the approximation ratios for approximation 2 and approximation 3 decrease toward 1. Approximation one stays close to 1 the whole time but trends slightly up.

The data suggests that denser graphs have larger MVCS, and larger graphs have more possible MVCs which is why the random picking approximations expected performance improve with increased edges. This also shows that the greedy approximation performs better than the random picking approximations.

=== Experiment 2

I fixed $e = 5$ edges and varied the node count over $[4, 5, 6, 7, 8]$. For each node count I generated 1000 random graphs, computed the toal MVC and the total of each of the three approximations, and averaged the ratio $|A_i|/|"MVC"|$ for the plot.

#figure(
  image("experiment_approximations_2_graph.png"),
  caption: [
    "Plot of Expected Approximation Performance for 5 Edges"
  ],
)

In this experiment, as the number of nodes increases while edges stay at 5, the expected approximation ratios for approximation 2 and approximation 3 increase. Approximation 1 stays near 1 again.

The result suggest that making more nodes makes the graph sparser. Sparse graphs are where random choice approximations can get worse in performance because they can waste picks more easily. This also shows that approximation 1's performance is largel independent of the number of nodes when the edges are fixed.

=== Experiment 3

For $n = 5$ nodes I enumerated all graphs by taking the powerset of the 10 possible edges, then grouped by edge count $e \in [1, 10]$. For each graph I computed the worst-case ratio for `approx1`, and for `approx2` and `approx3` I took the worst ratio across 100 random runs, then the worst over all graphs with the same $e$.

#figure(
  image("experiment_approximations_3_graph.png"),
  caption: [
    "Plot of Worst Case Approximation Performance for 5 Nodes"
  ],
)

To generate all graphs of size 5, I take all possible edge combinations for a 5 node graph and produce the powerset.

In this experiment, as the number of edges increase while nodes stay at 5, the worst case approximation ratio for approximation 2 and approximation 3 decrease to 1. Approximation 1 stays near or at one the whole time.

The results suggest that random choice algorithms perform the better as the number of edges increase. This also shows that greedy approximation algorithms are consistent when finding a minimum vertex cover.

== Experiment MIS-MVC Correlation
Data was collected for graphs with $n = 10$ nodes $e in [1, 54]$ edges
(inclusive). For a given edge amount, the average size of the maximum
independent subset and the average size of the minimal vertex cover over 1000
runs were collected. This was repeated for every integer amount of edges within
the experiment parameters. The experiment was then performed again with $n=15$
nodes and 10 runs each.

#grid(
  columns: 2,
  gutter: 2em,
  figure(
    image("experiment_MIS_MVC_correlation_graph.png"),
    caption: [
      Plot of MIS and MCV sizes for 10 nodes
    ],
  ),
  figure(
    image("experiment_MIS_MVC_correlation_graph2.png"),
    caption: [
      Plot of MIS and MCV sizes for 15 nodes
    ],
  ),
)

The data suggests that the MIS and MVC are correlated in way such that the sum
of the MIS and MVC is roughly constant and equal to $n$. The data also shows
that the maximum independent subset's size decreases with the edge count and the
minimum vertex cover's size increases with the edge count.

#figure(
  image("experiment_MIS_MVC_correlation_graph_with_sum.png"),
  caption: [
    Plot of MIS and MCV sizes for 10 nodes with sum
  ],
)


= Appendix
== Code Structure

- `graph.py`: Graph data structure, graph generators, MVC/MIS implementations, and approximation algorithms.
- `experiment.py`: Runs all experiments, collects data, and produces plots.
- `experiment1_output.txt` and `experiment2_output.txt`: Raw output for Part 1 experiments.
- `experiment_approximations_1_output.txt` through `experiment_approximations_3_output.txt`: Raw output for vertex cover approximation experiments.
- `experiment_MIS_MVC_correlation_output.txt` and `experiment_MIS_MVC_correlation_output2.txt`: Raw output for MIS-MVC correlation experiments.
- PNG figures: `experiment1_graph.png`, `experiment2_graph.png`, `experiment_approximations_1_graph.png`, `experiment_approximations_2_graph.png`, `experiment_approximations_3_graph.png`, `experiment_MIS_MVC_correlation_graph.png`, `experiment_MIS_MVC_correlation_graph2.png`, `experiment_MIS_MVC_correlation_graph_with_sum.png`.


== Code Navigation

To run a specific experiment, call the matching function in `experiment.py`.
