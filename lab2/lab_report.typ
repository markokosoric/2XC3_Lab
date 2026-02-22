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
  ]
)
The data shows that the probability of finding a cycle follows a sigmoid curve
when plotted against edge count. The probability starts to rises as the number
of edges reaches around 50 and reaches probability 1 at around 150.

== Experiment 2
A graph with $n = 100$ nodes and $e in [100, 500]$ was generated 100 times. The
probability that the graph is connected was recorded. This procedure was
repeated for all integer values of $e$ within the experiment parameters.
#figure(
  image("experiment2_graph.png"),
  caption: [
    Probability of a graph being connected vs edge count
  ]
)
The data shows that the probability of the graph being connected is almost zero
when the edges is below 150. Once the amount of edges reaches around 350, it
becomes almost certain that the graph will be connected. This graph also follows
a sigmoid curve like the graph in experiment 1.

= Part 2
== Experiment Vertex Cover Approximations

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
    ]
  ),
  figure(
    image("experiment_MIS_MVC_correlation_graph2.png"),
    caption: [
      Plot of MIS and MCV sizes for 15 nodes
    ]
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
  ]
)


= Appendix
== Code Structure
