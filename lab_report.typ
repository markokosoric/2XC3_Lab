#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)



#align(center)[
  #text(size: 2em, weight: "bold")[Lab Report: Sorting Algorithms Analysis]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab 1]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick]

  #v(1em)

  #text(size: 1em)[February 1, 2026]
]

#pagebreak()

#outline()

#pagebreak()

#outline(target: figure.where(kind: image))

#pagebreak()

= Executive Summary

- Selection sort is the fastest among bad sorts, while bubble sort is the slowest.
- Optimized versions of bubble and selection sort show performance improvements, with bubble sort benefiting more significantly.
- Good sorts (merge, quick, heap) exhibit quasilinear time complexity, with quicksort being the fastest.
- For nearly sorted lists, insertion sort performs exceptionally well.
- Dual pivot quicksort outperforms standard quicksort for larger lists.
- Recursive merge sort is faster.
- For very small lists (size ≤ 41), insertion sort outperforms merge and quick sort due to lower overhead.

#pagebreak()

#show figure.where(
  kind: image,
): set figure.caption(position: top)

= Part 1

== Experiment 1
- List lengths: [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900 ]
- Number of runs: 10 each

#figure(image("exp1_graph.png"), caption: [Runtime of bubble, selection, and insertion sort as list size increases.])

The algorithm runs in quadratic time as the list length increases. Selection sort is the quickest and bubble sort is the slowest.


== Experiment 2
- List lengths: [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900 ]
- Number of runs: 10 each

#figure(image("exp2_bubble_graph.png", width: 75%), caption: [Runtime comparison of normal and optimized bubble sort.])

#figure(
  image("exp2_selection_graph.png", width: 75%),
  caption: [Runtime comparison of normal and optimized selection sort.],
)


Both algorithms show a measurable speed up. Bubble sort had a big speed up, while selection sort did not show a substantial speed up.

== Experiment 3
Each of the unoptimized sorting algorithms was tested with the same parameters.
- Length of list: 5000
- Number of runs: 10 each
- Number of swaps: [ 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]

The results show that selection sort behaves the same regardless of how many
swaps were performed. Bubble sort showed a small improvement when given a almost
sorted list. Insertion sort showed a major improvement when given a amost sorted
list.

#figure(image("exp3_graph.png"), caption: [Runtime of sorting algorithms with varying numbers of initial swaps.])

== Experiment 4
Each of the good sorting algorithms was tested with the same parameters
- Length of list: [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000 ]
- Number of runs: 10 each

Each of the good sorts showed a quasilinear time complexity. Heap sort takes the
longest, which is probably due to the overhead of creating a heap. Quicksort
takes the shortest amount of time.

#figure(image("exp4_graph.png"), caption: [Runtime of merge sort, quicksort, and heap sort for increasing list sizes.])

= Part 2

== Experiment 5
Each of the sorting algorithms was tested with the following parameters:
- Length of list: 2,000
- Number of swaps: [ 0, 1, 2, 4, 8, 16, 32, 64, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ]
- Number of runs: 100 each
#figure(
  image("exp5_graph.png"),
  caption: [Runtime of sorting algorithms with varying numbers of initial swaps on lists.],
)

The results show that quick sort initially performs poorly for small swaps because of the overhead of pivot selections and recursive partitioning, but becomes the fastest algorithm as the list becomes less sorted. Merge sort and heap sort maintain stable performance across all numbers of swaps.

== Experiment 6
Each of the sorting algorithms was tested with the following parameters:
- Length of lists: [ 100, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 80000, 160000, 200000, 500000 ]
- Number of runs: 10 each
#figure(
  image("exp6_graph.png"),
  caption: [Runtime comparison of standard quicksort and dual-pivot quicksort for increasing list sizes.],
)

The results show that dual quick sort is increasingly faster than normal quick sort as the length of the lists gets longer. This is probably because dual reduces the number of operations done on average by using two pivots.


== Experiment 7
Recursive merge sort and iterative merge sort were tested with the following
parameters
- lengths: [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 ]
- Number of runs: 100 each
#figure(
  image("exp7_graph.png"),
  caption: [Runtime comparison of iterative and recursive merge sort for increasing list sizes.],
)

The iterative merge sort was slightly more performant for small list sizes. The
recursive variant is more performant with large list sizes. This is due to how Python handles memory. Also, the runtime of merge sort is dominated by the linear merging and operations rather than the recursive splitting.

== Experiment 8
The following algorithms were tested with the following parameters:
- Length of lists: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41 ]
- Number of runs: 10,000 each
#figure(
  image("exp8_graph.png"),
  caption: [Runtime of insertion sort, merge sort, and quicksort for small list sizes (1-41).],
)

This experiment compares insertion sort with merge sort and quick sort on small list sizes from 1 to 41. The results show that insertion sort outperforms merge sort and quick sort for very small lists. This is because it does not require the extra overhead from recursive calls and can run using the same or fewer comparisons. As the list size increases, insertion's sort time complexity causes its runtime to grow much faster than the two other algorithms.

These results are important and practical because they show that asymptotic complexity is not the only thing that determines the performance for small inputs. For example, many sorting algorithms use a hybrid approach where they combine divide and conquer algorithms with insertion sort for small sublists. This takes advantage of insertion sort's efficiency on small lists while maintaining good overall performance on larger inputs.

#pagebreak()

= Appendix: Code Navigation

This appendix explains how to navigate the code for each experiment and implementation.

- `bad_sorts.py`: Contains implementations of bad sorting algorithms (bubble sort, selection sort, insertion sort). Used in Experiments 1, 2, 3, and 5.
- `good_sorts.py`: Contains implementations of good sorting algorithms (merge sort, quicksort, heap sort, dual pivot quicksort). Used in Experiments 4, 5, 6, 7, and 8.
- `bench.py`: The benchmarking script that runs the experiments and generates output files.
- `test_sort.py`: Contains unit tests for the sorting algorithms.
- Output files: `exp1_output.txt` through `exp8_output.txt` contain the raw data from each experiment.
- `temp.txt`: Temporary file used during benchmarking.

To run a specific experiment, modify `bench.py` to call the desired experiment function. The sorting implementations are in the respective .py files, and the benchmarking logic is in `bench.py`.
