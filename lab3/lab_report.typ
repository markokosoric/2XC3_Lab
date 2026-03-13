#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)



#align(center)[
  #text(size: 2em, weight: "bold")[Lab Report: Binary Trees Analysis]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab 3]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick Chen]

  #v(1em)

  #text(size: 1em)[March 12, 2026]
]

#pagebreak()

#outline()

#pagebreak()

#outline(target: figure.where(kind: image))

#pagebreak()

= Executive Summary

- For random insertion orders with 10,000 nodes, the average difference in
  height between BSTs and RBTS is 15.196.
- RBT height stayed consistently lower because balancing operations prevent the
  worst-case growth seen in BSTs.
- For nearly sorted input (0 swaps), BSTs had the largest height gap versus
  RBTs. Increasing swaps reduced this gap toward 1.
- For X3Trees of degree $i$, height followed the recurrence $h(i) = 1 + h(i-2)$
  with closed form $h(i) = ceil(i/2) + 1$.
- The number of nodes in a degree-$i$ X3Tree matched the Fibonacci relation
  $F_(i+2)$.
- Since node count grows exponentially as a function of degree ($O(phi^d)$),
  X3Tree height as a function of nodes is $O(log(n))$.

#pagebreak()

= Part 1


== Expirement 1

Random lists of length 10,000 were generated. Each lisake a
Binary Search Tree and a Red-Black Tree using the same insertion order. After
building both trees, the difference

$ "BST height" - "RBT height" $

was calculated. This process was repeated 10,000, and the average difference

$ ("BST height" - "RBT height") / n $

was measured.

For lists of length 10,000, the average difference was 15.196. This shows that
binary search trees are consistently taller then red-black trees when inserting
a lot values in random order.

These results were expected since red-black trees are self-balancing, while
binary search trees depend on the insertion order which can cause them to be
very unbalanced.

However, there are cases where a binary search trees are better. BSTs are
simpler to implement and do not need rotations and recoloring operations. This
means when the number of inputs are smaller, BST insertions are slightly faster
and can still be relatively balanced compared to the red-black tree version.
This can be seen in Figure 1

#figure(
  image("experiment1_2_graph.png"),
  caption: [
    Plot of Average height of BSTs and RBTs on Varying Node Sizes
  ],
)

== Expirement 2

Random lists of length 50 were generated 10,000 times per run. Each run the list
would become more unsorted by performing an increasing number of random swaps
(swaps = [0,1,2,3,4,5,10,25,50,100]). The modified list was then inserted into
both a BST and RBT and the height difference

$ ("BST height" - "RBT height") / n $

was measured. The resulting graph plots number of swaps on the x-axis and
average difference on the y-axis.

#figure(
  image("experiment2_graph.png"),
  caption: [
    Plot of Average Difference in height between BSTs and RBTs on Varying
    Amounts of Random Swaps
  ],
)

When the list was perfectly sorted (0 swaps), the BST became very unbalanced and
produced the largest height difference compared to the red-black tree. As the
list became less sorted (\# swaps increased), the difference in height
decreased closer to 1.

The results were expected because BSTs performance highly depends on input
order. With a sorted list, the BST becomes similar to a linked list causing a
big height. In contrast, the RBT's performance stays similar regardless of input
order. As the list becomes less sorted, the BST structure becomes more balanced
because the order of values are more random.

= Part 2
== Experiment 3
A X3Tree was generated for all degrees $i in NN_0$ where $0 <= i <= 25$. The
height of the tree was recorded. Since X3Tree generation is deterministic, only
one tree was generated for each degree.
== Experiment 4
A X3Tree was generated for all degrees $i in NN_0$ where $0 <= i <= 25$. The
number of nodes in the tree was recorded. Since X3Tree generation is
deterministic, only one tree was generated for each degree.

== Results
#figure(
  table(
    columns: 3,
    stroke: none,
    column-gutter: 1em,
    row-gutter: -0.1em,
    [*Size*], [*Height*], [*Nodes*],
    table.hline(),
    [0], [1], [1],
    [1], [2], [2],
    [2], [2], [3],
    [3], [3], [5],
    [4], [3], [8],
    [5], [4], [13],
    [6], [4], [21],
    [7], [5], [34],
    [8], [5], [55],
    [9], [6], [89],
    [10], [6], [144],
    [11], [7], [233],
    [12], [7], [377],
    [13], [8], [610],
    [14], [8], [987],
    [15], [9], [1597],
    [16], [9], [2584],
    [17], [10], [4181],
    [18], [10], [6765],
    [19], [11], [10946],
    [20], [11], [17711],
    [21], [12], [28657],
    [22], [12], [46368],
    [23], [13], [75025],
    [24], [13], [121393],
    [25], [14], [196418],
    table.hline(),
  ),
  caption: [Results for experiment 3 (height) and experiement 4 (Nodes)],
)

== Conclusion
=== Height
For every increase of two to a X3Tree's degree, the height increases by one.
This is because the height of a X3Tree of degree $i$ is one plus the maximum
height of the children, and the child with the maximum height is the $(i-2)$.

Therefore, we have the recurrence relation
$
  h(i) = 1 + h(i-2)
$
Since the degree 0 X3Tree has height 1 and the degree 1 X3Tree has height 2, the
recurrence relation has solution
$
  h(i) = ceil(i/2) + 1
$

=== Number of nodes
The results show that the number of nodes for a tree of degree $i$ is the
Fibonacci number $F_(i+2)$. This is because the child with degree $i-4$ has
$F_(i)$ nodes and the sum of other nodes is equal to $F_(i-3) - 1$, therefore
the sum of all nodes is $F_(i-2)$

It is known that the sum of all Fibonacci numbers up to $n$ is equal to one less
than the $(n+2)$th Fibonacci number.
$
  sum_(i=1)^n F_i = F_(n+2) - 1
$

Since the sum of all nodes is
$
  "Nodes"(n) & = 1 + sum_(i = -1)^(n-2) "Nodes"(c) \
             & = 1 + sum_(i=1)^n F_i               & "Inductive hypothesis" \
             & = 1 + F_(i+2) - 1                   &   "Fibonacci Identity" \
             & = F_(i+2)
$
Since the base case is also fulfilled, the number of nodes in a degree $n$
X3Tree is $F_(n+2)$

=== Complexity bound on height
The complexity of the height of a X3Tree with respect to the complexity of the
number of nodes is as follows
$
  h("Nodes"^(-1)(n))
$
Since the number of nodes for a given degree $"Nodes"(d)$ is the Fibonacci, it
has growth $O(phi^d)$. This can be proven by examining the limiting behaviors of
the closed form of the Fibonacci function. Therefore the complexity of
$"Degree"(n) = "Nodes"^(-1)(n)$ with respect to nodes is $O(log_(phi) (n))$.
Since the complexity of height with respect to degree is linear, $h circle.small
"Degree"$ is $O(log_phi (n)) tilde.equiv O(log(n))$.



#pagebreak()

= Appendix
== Code Structure


- `tree.py`: RBT, BST, and X3Tree data structure.
- `experiment.py`: Runs all experiments, collects data, and produces plots.
- `experiment1_1_output.txt`, `experiment1_2_output.txt` and
  `experiment2_output.txt`: Text output for Part 1 experiments.
- PNG figures: `experiment1_2_graph.png`, `experiment2_graph.png`
- `lab_report.typ`: Code for the lab report document.

== Code Navigation
To run a specific experiment, modify `experiment.py` to call the desired
experiment function.
