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

= Experiment 3
Each of the unoptimized sorting algorithms were tested with the same parameters.
- Length of list: 5000
- Number of runs: 10
- Number of swaps: [ 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]

The results show that selection sort behaves the same regardless of how many
swaps were performed. Bubble sort showed a small improvement when given a almost
sorted list. Insertion sort showed a major improvement when given a amost sorted
list.

#image("exp3_graph.png")

= Experiment 4
Each of the good sorting algorithms were tested with the same parameters
- Length of list: [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000 ]
- Number of runs: 10 each

Each of the good sorts showed a quasilinear time complexity. Heap sort takes the
longest which is probably due to the overhead of creating a heap. Quicksort
takes the shortest amount of time.

= Experiment 7
Recursive merge sort and iterative merge sort were tested with the following
parameters
- lengths: [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]
- Number of runs: 100 each
#image("exp7_graph.png")


The iterative merge sort was slightly more performant for small list sizes. The
recursive variant is more performant with large list sizes.

