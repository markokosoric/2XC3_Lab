#show figure.where(
  kind: image,
): set figure.caption(position: top)

= Experiment 1


List lengths: 100,
200,
300,
400,
500,
600,
700,
800,
900,
1000,
1100,
1200,
1300,
1400,
1500,
1600,
1700,
1800,
1900,

\# of runs: 10

#image("exp1_graph.png")

The algorithm runs in quadratic time as the list length increases. Selection sort is the quickest and bubble sort is the slowest.

#pagebreak()

= Experiment 2

List lengths: 100,
200,
300,
400,
500,
600,
700,
800,
900,
1000,
1100,
1200,
1300,
1400,
1500,
1600,
1700,
1800,
1900,

\# of runs: 10

#figure(image("exp2_bubble_graph.png", width: 75%)),
caption: [normal vs. optomized bubble sort],
)

#figure(
  image("exp2_selection_graph.png", width: 75%),
  caption: [normal vs. optomized selection sort],
)


Both algorithms show a measurable speed up. Bubble sort had a big speed up while selection sort did not show a substantial speed up.
