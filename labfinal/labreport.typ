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

= Experiment 1

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
    Plot of Average height of BSTs and RBTs on Varying Node Sizes
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
