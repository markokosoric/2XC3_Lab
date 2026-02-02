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


Both algorithms show a measurable speed up. Bubble sort had a big speed up, while selection sort did not show a substantial speed up.

= Experiment 3
Each of the unoptimized sorting algorithms was tested with the same parameters.
- Length of list: 5000
- Number of runs: 10
- Number of swaps: [ 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]

The results show that selection sort behaves the same regardless of how many
swaps were performed. Bubble sort showed a small improvement when given a almost
sorted list. Insertion sort showed a major improvement when given a amost sorted
list.

#image("exp3_graph.png")

= Experiment 4
Each of the good sorting algorithms was tested with the same parameters
- Length of list: [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000 ]
- Number of runs: 10 each

Each of the good sorts showed a quasilinear time complexity. Heap sort takes the
longest, which is probably due to the overhead of creating a heap. Quicksort
takes the shortest amount of time.

#image("exp4_graph.png")

= Experiment 5
Each of the sorting algorithms was tested with the following parameters:
- Length of list: 2,000
- Number of swaps: [
  0,
  1,
  2,
  4,
  8,
  16,
  32,
  64,
  100,
  200,
  300,
  400,
  500,
  600,
  700,
  800,
  900,
  1000,
  ]
- Number of runs: 100 each
#image("exp5_graph.png")

The results show that quick sort initially performs poorly for small swaps because of the overhead of pivot selections and recursive partitioning, but becomes the fastest algorithm as the list becomes less sorted. Merge sort and heap sort maintain stable performance across all numbers of swaps.

= Experiment 6
Each of the sorting algorithms was tested with the following parameters:
- Length of lists: [
  100,
  1000,
  2000,
  5000,
  10000,
  20000,
  30000,
  40000,
  80000,
  160000,
  200000,
  500000
  ]
- Number of runs: 10 each
#image("exp6_graph.png")

The results show that dual quick sort is increasingly faster than normal quick sort as the length of the lists gets longer. This is probably because dual reduces the number of operations done on average by using two pivots.


= Experiment 7
Recursive merge sort and iterative merge sort were tested with the following
parameters
- lengths: [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]
- Number of runs: 100 each
#image("exp7_graph.png")


The iterative merge sort was slightly more performant for small list sizes. The
recursive variant is more performant with large list sizes. This is due to how Python handles memory. Also, the runtime of merge sort is dominated by the linear merging and operations rather than the recursive splitting.

= Experiment 8
The following algorithms were tested with the following parameters:
- Length of lists: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41 ]
- Number of runs: 10,000 each
#image("exp8_graph.png")

This experiment compares insertion sort with merge sort and quick sort on small list sizes from 1 to 41. The results show that insertion sort outperforms merge sort and quick sort for very small lists. This is because it does not require the extra overhead from recursive calls and can run using the same or fewer comparisons. As the list size increases, insertion's sort time complexity causes its runtime to grow much faster than the two other algorithms.

These results are important and practical because they show that asymptotic complexity is not the only thing that determines the performance for small inputs. For example, many sorting algorithms use a hybrid approach where they combine divide and conquer algorithms with insertion sort for small sublists. This takes advantage of insertion sort's efficiency on small lists while maintaining good overall performance on larger inputs.
