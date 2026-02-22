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
== Experiment 2

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
